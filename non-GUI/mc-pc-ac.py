import click
import time
import os
import winreg
import mcpcacconfig
def chck_reg(cheats):
    pass
def chck_files(cheats):
    pass
def chck_deleted(cheats):
    rbin="C:\$Recycle"
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
@click.option("--auto", is_flag=True)
@click.option("--files", is_flag=True)
@click.option("--deleted", is_flag=True)
@click.option("--minecraft", is_flag=True)
@click.option("--reg", is_flag=True)
@click.option("--logs", is_flag=True)
def main(auto, files, deleted, reg, logs):
    cheats = mcpcacconfig.CHEATS
    if auto:
        auto_chck(cheats)
    elif files:
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
        print("Nothing Selected, should i start auto checking?")
        sel = input("[Y]es/[N]o >> ")
        if sel == "Y" or "y" or "Yes" or "yes":
            print("Start auto checking...")
            auto_check(cheats)
    