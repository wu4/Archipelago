from test.bases import WorldTestBase

# nn  <C-5> <Cmd>exe "tabe \| setl nonu \| exe \"term overlay use venv/bin/activate.nu; python ./Generate.py\" \| startinsert"<CR>


class MyGameTestBase(WorldTestBase):
    game = "Cavern of Dreams"
