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

if platform.system() == "Windows":
    import winreg
else:
    print("Non-Windows operating system detected. Not importing registry dependencies!")
def chck_reg(cheats):
    '''Check in registry (WINDOWS ONLY)'''
    pass
def chck_files(cheats):
    print("Checking whole system")
    '''Will check the whole system drive including .minecraft'''
    print("Checking ALL files, are you sure? (NOTE: this will take a while(depending on your pc speed), and you should NOT close script)")
    selone=input("[Y]es/[N]o >> ")
    if selone.lower() == "y":
        if platform.system() == "Windows":
            names = cheats
            found = []
            for root, dirs, files in os.walk("C:/"):
                print(Fore.RED+f">>3: {root}"+Fore.RESET)
                for file in files:
                    print(Fore.RED+f">>#: {file}"+Fore.RESET)
                    if any(name.lower() in file.lower() for name in names):
                        file_path = os.path.join(root, file)
                        print(Fore.GREEN+f'Found file: {file_path}'+Fore.RESET)
                        found.append(file_path)

            print("Found files:")
            for file in found:
                print(file_path)
        elif platform.system() == "Linux":
            found = []
            names = cheats
            for root, dirs, files in os.walk("/"):
                print(Fore.RED+f">>3: {root}"+Fore.RESET)
                for file in files:
                    print(Fore.RED+f">>#: {file}"+Fore.RESET)
                    if any(name.lower() in file.lower() for name in names):
                        file_path = os.path.join(root, file)
                        print(Fore.GREEN+f'Found file: {file_path}'+Fore.RESET)
                        found.append(file_path)

            print("Found files:")
            for file in found:
                print(file_path)
        waitend = input("press enter to exit")
    else:
        print("Aborting...")
def chck_deleted(cheats):
    if platform.system() == "Linux":
        os.chdir(str(os.environ["HOME"]))
        rbin=".local/share/Trash/files"
    elif platform.system() == "Windows":
        rbin="C:\$Recycle"
    else:
        sys.exit("001")
    found = []
    names = cheats
    for root, dirs, files in os.walk(rbin):
        print(Fore.RED+f">>3: {root}"+Fore.RESET)
        for file in files:
            print(Fore.RED+f">>#: {file}"+Fore.RESET)
            if any(name.lower() in file.lower() for name in names):
                file_path = os.path.join(root, file)
                print(Fore.GREEN+f'Found file: {file_path}'+Fore.RESET)
                found.append(file_path)

    print("Found files:")
    for file in found:
        print(file_path)
    input("press enter to exit")

def chck_minecraft(cheats):
    pass
def chck_logs(cheats):
    print("checking logs...")
    if platform.system() == "Windows":
        os.chdir(str(os.environ["APPDATA"]))
    elif platform.system() == "Linux":
        os.chdir(str(os.environ["HOME"]))
    files = ".minecraft/logs/"
    # Iterate through the list and open each file
    for root, dirs, files in os.walk(files):
        for file in files:
            if file.endswith('.log'):
                with open(f"{root}{os.sep}{file}", "rb") as f:
                    lines = f.read()
                    for cheat in cheats:
                        if lines.find(bytes(cheat, "utf-8")) != -1:
                            print(f"Found suspicious log! looks like someone cheater!: {file}")
            if file.endswith(".gz"):
                with gzip.open(f"{root}{os.sep}{file}", 'r') as f:
                    data = f.readlines()
                    for line in data:
                        for cheat in cheats:
                            if bytes(cheat, "utf-8") in line:
                                if cheat in str(line, "utf-8"):
                                    print(f"Found suspicious log! looks like someone cheater!: {file}")
    input("press enter to exit")
## Main
@click.command()
@click.option("--files", is_flag=True, help="Will check the whole system drive including .minecraft")
@click.option("--deleted", is_flag=True, help="Checks the trash bin")
@click.option("--minecraft", is_flag=True, help="Deeply check .minecraft folder for files made by cheats")
@click.option("--reg", is_flag=True, help="Check in registry (WINDOWS ONLY)")
@click.option("--logs", is_flag=True, help="Scans logs for any suspicious things")
def main(files, deleted, reg, logs, minecraft):
    if files:
        chck_files(cheats)
    elif deleted:
        chck_deleted(cheats)
    elif reg:
        chck_reg(cheats)
    elif logs:
        chck_logs(cheats)
    elif minecraft:
        chck_minecraft(cheats)
    else:
        print("Nothing Selected, should i start auto check for the whole system?")
        sel = input("[Y]es/[N]o >> ")
        if sel == "Y" or sel == "y" or sel == "Yes" or sel == "yes":
            chck_files(cheats)
            
        elif sel == "n" or sel == "No" or sel == "no":
            print ("nothin hapens, try 'mc-pc-ac --help' ")
        else:
            print(f"wtf wrong with you, you can choose only yes or no, not {sel}")
if __name__ == "__main__":
    main()
