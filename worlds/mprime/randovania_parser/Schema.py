from schema import Schema, And, Or, Optional

Vector3 = Schema({
    "x": float,
    "y": float,
    "z": float
})


def forwarded_ConnectionData(x):
    ConnectionData.validate(x)


Template = Schema({
    "type": "template",
    "data": str
})

Logic = Schema({
    "type": Or("and", "or"),
    "data": {
        "comment": Or(str, None),
        "items": [forwarded_ConnectionData]
    }
})

Resource = Schema({
    "type": "resource",
    "data": {
        "type": Or("items", "tricks", "damage", "events", "misc"),
        "name": str,
        "amount": int,
        "negate": bool
    }
})

ConnectionData = Or(Template, Logic, Resource)

Event = Schema({
    "node_type": "event",

    "heal": False,
    "coordinates": Or(Vector3, None),
    "description": str,
    "layers": list[str],
    "extra": dict,
    "valid_starting_location": False,
    "connections": Or({}, {
        str: ConnectionData
    }),

    "event_name": str
})

Generic = Schema({
    "node_type": "generic",

    "heal": bool,
    "coordinates": None,
    "description": str,
    "layers": list,
    "extra": dict,
    "valid_starting_location": bool,
    "connections": Or({}, {
        str: ConnectionData
    }),
})

Pickup = Schema({
    "node_type": "pickup",

    "heal": bool,
    "coordinates": None,
    "description": str,
    "layers": list,
    "extra": dict,
    "valid_starting_location": False,
    "connections": Or({}, {
        str: ConnectionData
    }),

    "pickup_index": int,
    "location_category": Or("major", "minor")
})

DockType = Or(
    "door",
    "teleporter",
    "Teleporter",
    "morph_ball",
    "Missile Blast Shield",
    "Morph Ball Door",
    "Normal Door",
    "Ice Door",
    "Wave Door",
    "Plasma Door",
    "other",
    "Open Passage",
    "Closed Passage",
    "Permanently Locked",
    "Circular Door",
    "Square Door",
)

Dock = Schema({
    "node_type": "dock",

    "heal": bool,
    "coordinates": Or(Vector3, None),
    "description": str,
    "layers": list[str],
    "extra": dict,
    "valid_starting_location": bool,
    "connections": Or({}, {
        str: ConnectionData
    }),

    "dock_type": DockType,
    "default_connection": {
        "region": str,
        "area": str,
        "node": str
    },
    "default_dock_weakness": DockType,
    "exclude_from_dock_rando": bool,
    "incompatible_dock_weaknesses": list,
    "override_default_open_requirement": None,
    "override_default_lock_requirement": None,
})

Node = Or(Pickup, Generic, Event, Dock)

Area = Schema({
    "default_node": And(str, len),
    Optional("extra"): {
        "asset_id": int,
        "size_index": float,
        Optional("aabb"): list[float],
        Optional("unlocked_save_station"): bool,
    },
    "nodes": {
        str: Node
    }
})

Region = Schema({
    "name": And(str, len),
    Optional("extra"): dict,
    "areas": {
        str: Area
    }
})
