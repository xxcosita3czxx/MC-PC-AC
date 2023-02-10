import click
import time
import os
import platform
import mcpcacconfig
from colorama import *
from sys import argv, exit
import sys
import gzip
cheats = mcpcacconfig.CHEATS


def chck_logs(cheats):
    print("checking logs...")
    # Get a list of all the files in the folder
    if platform.system() == "Windows":
        os.chdir(str(os.environ["APPDATA"]))
    elif platform.system() == "Linux":
        os.chdir(str(os.environ["HOME"]))
    mclogdir = ".minecraft/logs/"
    # Iterate through the list and open each file
    if os.path.exists(mclogdir):
        for root, dirs, files in os.walk(mclogdir):
            for file in files:
                if file.endswith('.txt'):
                    if os.path.exists(file):
                        with open(file, "rb") as f:
                            # Do something with the file
                            lines = f.readlines() 
                            for line in lines:
                                if line.find(cheats) != -1:
                                    print(line)
                            # Close the file
                            f.close()
                if file.endswith(".gz"):
                    if os.path.exists(f"{root}/{file}"):
                        with gzip.open(f"{root}/{file}", 'rb') as f:
                            data = f.readlines()
                            for line in data:
                                for cheat in cheats:
                                    if cheat in str(line, "utf-8"):
                                        print(f"Found suspicious log! looks like someone cheater!: {file}")
                                        break
                    else:
                        print("error: Could not open")

chck_logs(cheats)