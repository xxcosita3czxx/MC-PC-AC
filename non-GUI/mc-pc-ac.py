import click
import time
import os
import platform
import mcpcacconfig
from colorama import *
from sys import argv, exit
import sys
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
    if platform.system() == "Windows":
        print("Checking ALL files, are you sure? (NOTE: this will take a while, and you should NOT close script)")
        selone=input("[Y]es/[N]o >> ")
        if selone.lower() == "y":
            if platform.system() == "Windows":
                names = cheats
                found = []
                for root, dirs, files in os.walk("C:/"):
                    print(Fore.RED+f">>3: {root}"+Fore.RESET)
                    for file in files:
                        print(Fore.RED+f">>#: {file}"+Fore.RESET)
                        if any(name in file for name in names):
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
                        if any(name in file for name in names):
                            file_path = os.path.join(root, file)
                            print(Fore.GREEN+f'Found file: {file_path}'+Fore.RESET)
                            found.append(file_path)

                print("Found files:")
                for file in found:
                    print(file_path)
def chck_deleted(cheats):
    if platform.system() == "Linux":
        os.chdir(str(os.environ["HOME"]))
        rbin=".local/share/Trash/files"
    elif platform.system() == "Windows":
        rbin="C:/$Recycle"
    else:
        print("mac os not support, this command failing")
        sys.exit("001")
    found = []
    names = cheats
    for root, dirs, files in os.walk(rbin):
        print(Fore.RED+f">>3: {root}"+Fore.RESET)
        for file in files:
            print(Fore.RED+f">>#: {file}"+Fore.RESET)
            if any(name in file for name in names):
                file_path = os.path.join(root, file)
                print(Fore.GREEN+f'Found file: {file_path}'+Fore.RESET)
                found.append(file_path)

    print("Found files:")
    for file in found:
        print(file_path)
def chck_minecraft(cheats):
    pass
def chck_logs(cheats):
    print("checking logs...")
    f = open("log.txt", "r")
    lines = f.readlines() 
    for line in lines:
        if line.find(cheats) != -1:
            print(line)
    # Close the file
    f.close()
def auto_chck():
    cheats = mcpcacconfig.CHEATS
    chck_reg(cheats)
    chck_files(cheats)
    chck_deleted(cheats)
    chck_minecraft(cheats)
    chck_logs(cheats)
## Main
@click.command()
@click.option("--auto", is_flag=True, help="Automaticaly checks in the whole system (Unstable, doesnt really work)")
@click.option("--files", is_flag=True, help="Will check the whole system drive including .minecraft")
@click.option("--deleted", is_flag=True, help="Checks the trash bin")
@click.option("--minecraft", is_flag=True, help="Deeply check .minecraft folder for files made by cheats")
@click.option("--reg", is_flag=True, help="Check in registry (WINDOWS ONLY)")
@click.option("--logs", is_flag=True, help="Scans logs for any suspicious things")
def main(auto, files, deleted, reg, logs, minecraft):
    if auto:
        auto_chck()
        sys.exit("000")
    elif files:
        chck_files(cheats)
        sys.exit("000")
    elif deleted:
        chck_deleted(cheats)
        sys.exit("000")
    elif reg:
        chck_reg(cheats)
        sys.exit("000")
    elif logs:
        chck_logs(cheats)
        sys.exit("000")
    elif minecraft:
        chck_minecraft(cheats)
        sys.exit("000")
    else:
        print("Nothing Selected, should i start auto checking?")
        sel = input("[Y]es/[N]o >> ")
        if sel == "Y" or sel == "y" or sel == "Yes" or sel == "yes":
            print("UNSTABLE, USE 'mc-pc-ac --auto' instead")
            # print("Start auto checking...")
            # auto_chck()
        elif sel == "N" or sel == "n" or sel == "No" or sell == "no":
            print ("nothin hapens, try 'mc-pc-ac --help' ")
            sys.exit("000")
        else:
            print(f"wtf wrong with you, you can choose only yes or no, not {sel}")
            sys.exit("000")
if __name__ == "__main__":
    main()
