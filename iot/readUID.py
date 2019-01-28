import os
import webbrowser
import time

def getUID():
    output = os.popen("sudo nfc-list").read()
    for line in output.splitlines():
        if "UID" not in line:
            continue
        substring = line.split(": ")[1]
        return substring

if __name__ == "__main__":
    while True:
        time.sleep(1)
        UID = getUID()
        currentUID = ""
        if UID == "64 e5 e2 89" and currentUID != "64 e5 e2 89":
            currentUID = "64 e5 e2 89"
            webbrowser.open("https://docs.google.com/presentation/d/e/2PACX-1vRxFz9K9NYMrmvFVlhDRgtUuUsvoShpVMex0H7WhoiW_2pyyG_IX1UX5tCdBhWdXmcwQpC9UoWHpXJv/pub?start=true&loop=false&delayms=1000000", new=2)
        if UID == "a4 f0 e1 89" and currentUID != "a4 f0 e1 89":
            currentUID = "a4 f0 e1 89"
            webbrowser.open("https://docs.google.com/presentation/d/e/2PACX-1vSjJkaVCnEQwqOBfsVvbiFsu76pwYNYSS9_abLpKRugYTGCOwHSIk7-01fVQ-GGLwMqYKfu5TI33ZWF/pub?start=true&loop=false&delayms=10000000", new=2)
        if UID == "04 43 f0 72 97 3c 80" and currentUID != "04 43 f0 72 97 3c 80":
            currentUID = "04 43 f0 72 97 3c 80"
            webbrowser.open("https://docs.google.com/presentation/d/e/2PACX-1vTL-FVxf6fnJtalTQLB9wJOP5xbS4HQrb-2rDNFrHne_5pwMilElLLBh6VtS9jV8Ta3sVFCQz-WaPCN/pub?start=true&loop=false&delayms=10000000", new=2)


