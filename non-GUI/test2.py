import platform, os, gzip

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
                            waitend = input("press enter to exit")
            if file.endswith(".gz"):
                with gzip.open(f"{root}{os.sep}{file}", 'r') as f:
                    data = f.readlines()
                    for line in data:
                        for cheat in cheats:
                            if bytes(cheat, "utf-8") in line:
                                if cheat in str(line, "utf-8"):
                                    print(f"Found suspicious log! looks like someone cheater!: {file}")
                                    waitend = input("press enter to exit")
chck_logs(["Server"])