
pip install pyinstaller
pip install click

python -m pyinstaller --onefile --add-data=../non-GUI/mcpcacconfig.py;mcpcacconfig.py ../non-GUI/mc-pc-ac.py
