from .json_parsing import RandovaniaData, LocationTuple, NodeInfo
from typing import Optional

def get_unnecessary_connection_chains(data: RandovaniaData, nodes: dict[LocationTuple, NodeInfo]) -> dict[tuple[LocationTuple, LocationTuple], list[LocationTuple]]:
    nv = NodeVisitor(data, nodes)
    return nv.full_chains

SHIP_LOC = ("Ship", "Landing Site", "Tallon Overworld")
CREDITS_LOC = ("Teleporter to Credits", "Metroid Prime Lair", "Impact Crater")

class NodeVisitor:
    remaining: set[LocationTuple]
    nodes: dict[LocationTuple, NodeInfo]
    host_nodes: dict[LocationTuple, tuple[list[LocationTuple], list[LocationTuple]]]
    seen_host_nodes: set[LocationTuple]
    full_chains: dict[tuple[LocationTuple, LocationTuple], list[LocationTuple]]
    
    data: RandovaniaData

    def __init__(self, data: RandovaniaData, nodes: dict[LocationTuple, NodeInfo]) -> None:
        self.nodes = nodes
        self.host_nodes = {}
        self.seen_host_nodes = set()
        self.full_chains = {}
        self.data = data

        def refresh_remaining():
            self.remaining = set(k for k, v in nodes.items() if not v.items_every_room)

        refresh_remaining()
        while self.remaining:
            loc = self.remaining.pop()
            node = self.nodes[loc]

            if self.is_host_node(loc, node):
                self.host_nodes[loc] = self.get_connections(loc)

        for loc, node in self.host_nodes.items():
            if loc[0] == "Ship":
                print(loc)
                print("incoming: ", node[0])
                print("outgoing: ", node[1])

        self.traverse_host(SHIP_LOC)

    def is_host_node(self, node_loc: LocationTuple, node: NodeInfo) -> bool:
        if node_loc == SHIP_LOC or node_loc == CREDITS_LOC or node.is_important():
            return True

        incoming, outgoing = self.get_connections(node_loc)
        unique_connections = set((*incoming, *outgoing))
        return len(unique_connections) != 2
    
    def get_unique_connections(self, node_loc: LocationTuple) -> set[LocationTuple]:
        incoming, outgoing = self.get_connections(node_loc)
        return set((*incoming, *outgoing))

    def get_connections(self, node_loc: LocationTuple) -> tuple[list[LocationTuple], list[LocationTuple]]:
        conn = self.data.connections
        return (
            list(conn.incoming.get(node_loc, {}).keys()),
            list(conn.outgoing.get(node_loc, {}).keys()),
        )
        
        
        
    def traverse_host(self, host_loc: LocationTuple):
        if host_loc in self.seen_host_nodes: return

        self.seen_host_nodes.add(host_loc)

        incoming, outgoing = self.host_nodes[host_loc]
        for initial_connection_name in outgoing:
            self.traverse_forward(host_loc, host_loc, initial_connection_name)
        
    def traverse_forward(self, host_loc: LocationTuple, prev_loc: LocationTuple, node_loc: LocationTuple, accum: Optional[list[LocationTuple]] = None):
        if accum is None:
            accum = []
        node = self.nodes[node_loc]
        if self.is_host_node(node_loc, node):
            other_host_loc = node_loc
            if (host_loc, other_host_loc) in self.full_chains.keys() or (other_host_loc, host_loc) in self.full_chains.keys():
                return

            other_host_in_connections, other_host_out_connections = self.host_nodes[other_host_loc]
            if prev_loc in other_host_out_connections:
                if len(accum) > 0:
                    self.full_chains[(host_loc, other_host_loc)] = accum

            self.traverse_host(other_host_loc)
        else:
            incoming, outgoing = self.get_connections(node_loc)
            if prev_loc in outgoing:
                outgoing.remove(prev_loc)
                if len(outgoing) == 1:
                    next_loc = outgoing[0]
                    accum.append(node_loc)
                    self.traverse_forward(host_loc, node_loc, next_loc, accum)