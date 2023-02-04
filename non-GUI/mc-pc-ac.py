import click
import time
import os
import platform
import mcpcacconfig

if platform.system() == "Windows":
    import winreg
else:
    print("Non-Windows operating system detected. Not importing registry dependencies!")

def chck_reg(cheats):
    '''Check in registry (WINDOWS ONLY)'''
    pass
def chck_files(cheats):
    '''Will check the whole system drive including .minecraft'''
    if platform.system() == "Windows":
        print("Checking ALL files, are you sure? (NOTE: this will take a while, and you should NOT close script)")
        selone=input("y/n: ")
        if selone.lower() == "y":
            if platform.system() == "Windows":
                names = cheats
                for root, dirs, files in os.walk("C:/"):
                    for file in files:
                        if file in names:
                            file_path = os.path.join(root, file)
                            print(f'Found file: {file_path}')
            elif platform.system() == "Linux":
                names = cheats
                for root, dirs, files in os.walk("/"):
                    for file in files:
                        if file in names:
                            file_path = os.path.join(root, file)
                            print(f'Found file: {file_path}')
def chck_deleted(cheats):
    if platform.system() == "Linux":
        rbin="~/.local/share/trash"
    elif platform.system() == "Windows":
        rbin="C:\$Recycle"
    else:
        print("mac os not support, this command failing")
        exit("001")
    names = cheats
    for root, dirs, files in os.walk(rbin):
        for file in files:
            if file in names:
                file_path = os.path.join(root, file)
                print(f'Found file: {file_path}')
def chck_minecraft(cheats):
    pass
def chck_logs(cheats):
    pass
def auto_chck(cheats):
    chck_reg(cheats)
    chck_files(cheats)
    chck_deleted(cheats)
    chck_minecraft(cheats)
    chck_logs(cheats)
## Main

@click.command()
@click.option("--auto", is_flag=True, help="Automaticaly checks in the whole system")
@click.option("--files", is_flag=True, help="Will check the whole system drive including .minecraft")
@click.option("--deleted", is_flag=True, help="Checks the trash bin")
@click.option("--minecraft", is_flag=True, help="Deeply check .minecraft folder for files made by cheats")
@click.option("--reg", is_flag=True, help="Check in registry (WINDOWS ONLY)")
@click.option("--logs", is_flag=True, help="Scans logs for any suspicious things")
def main(auto, files, deleted, reg, logs, minecraft):
    cheats = mcpcacconfig.CHEATS
    if auto:
        auto_chck(cheats)
        exit("000")
    elif files:
        chck_files(cheats)
        exit("000")
    elif deleted:
        chck_deleted(cheats)
        exit("000")
    elif reg:
        chck_reg(cheats)
        exit("000")
    elif logs:
        chck_logs(cheats)
        exit("000")
    elif minecraft:
        chck_minecraft(cheats)
        exit("000")
    else:
        print("Nothing Selected, should i start auto checking?")
        sel = input("[Y]es/[N]o >> ")
        if sel == "Y" or "y" or "Yes" or "yes":
            print("Start auto checking...")
            auto_chck(cheats)
        elif sel == "N" or "n" or "No" or "no":
            print ("nothin hapens, try 'mc-pc-ac.py --help' ")
            exit("002")
        else:
            print(f"wtf wrong with you, you can choose only yes or no, not {sel}")
            exit("003")
if __name__ == "__main__":
    main()