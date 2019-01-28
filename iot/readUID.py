import os

def getUID():
    output = os.popen("sudo nfc-list").read()
    for line in output.splitlines():
        if "UID" not in line:
            continue
        substring = line.split(": ")[1]
        return substring

if __name__ == "__main__":
    getUID()

