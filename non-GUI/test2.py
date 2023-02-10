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
            if file.endswith('.txt'):
                with open(f"{root}{os.sep}{file}") as f:
                    # Do something with the file
                    lines = f.readlines() 
                    for line in lines:
                        if line.find(cheats) != -1:
                            print(line)
                    # Close the file
                    f.close()
            if file.endswith(".gz"):
                with gzip.open(f"{root}{os.sep}{file}", 'r') as f:
                    data = f.readlines()
                    for line in data:
                        for cheat in cheats:
                            if cheat in str(line, "utf-8"):
                                print(f"Found suspicious log! looks like someone cheater!: {file}")
                                break
chck_logs(["Server"])