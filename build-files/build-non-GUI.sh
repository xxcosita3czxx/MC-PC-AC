#! /bin/bash

pip install pyinstaller
pip install click

~/.local/bin/pyinstaller --onefile --add-data=../non-GUI/mcpcacconfig.py:mcpcacconfig.py ../non-GUI/mc-pc-ac.py