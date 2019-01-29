import os
import webbrowser
import time
from pykeyboard import PyKeyboard

def getUID():
    output = os.popen("sudo nfc-list").read()
    for line in output.splitlines():
        if "UID" not in line:
            continue
        substring = line.split(": ")[1]
        return substring
    return "empty"

if __name__ == "__main__":
    currentUID = ""
    while True:
        time.sleep(1)
        UID = getUID()
        print UID
        if "64  e5  e2  89" in UID and currentUID != "64  e5  e2  89":
            print "here"
            currentUID = "64  e5  e2  89"
            webbrowser.open("https://docs.google.com/presentation/d/e/2PACX-1vRxFz9K9NYMrmvFVlhDRgtUuUsvoShpVMex0H7WhoiW_2pyyG_IX1UX5tCdBhWdXmcwQpC9UoWHpXJv/pub?start=true&loop=false&delayms=1000000", new=2)
            time.sleep(8)
            keyboard = PyKeyboard()
            keyboard.press_key(keyboard.control_l_key)
            keyboard.press_key(keyboard.shift_l_key)
            keyboard.tap_key("f")
            keyboard.release_key(keyboard.control_l_key)
            keyboard.release_key(keyboard.shift_l_key)
        if "a4  f0  e1  89" in UID and currentUID != "a4  f0  e1  89":
            print "here"
            currentUID = "a4  f0  e1  89"
            webbrowser.open("https://docs.google.com/presentation/d/e/2PACX-1vSjJkaVCnEQwqOBfsVvbiFsu76pwYNYSS9_abLpKRugYTGCOwHSIk7-01fVQ-GGLwMqYKfu5TI33ZWF/pub?start=true&loop=false&delayms=10000000", new=2)
            time.sleep(8)
            keyboard = PyKeyboard()
            keyboard.press_key(keyboard.control_l_key)
            keyboard.press_key(keyboard.shift_l_key)
            keyboard.tap_key("f")
            keyboard.release_key(keyboard.control_l_key)
            keyboard.release_key(keyboard.shift_l_key)
        if  "04  43  f0  72  97  3c  80" in UID and currentUID != "04  43  f0  72  97  3c  80":
            print "here"
            currentUID = "04  43  f0  72  97  3c  80"
            webbrowser.open("https://docs.google.com/presentation/d/e/2PACX-1vTL-FVxf6fnJtalTQLB9wJOP5xbS4HQrb-2rDNFrHne_5pwMilElLLBh6VtS9jV8Ta3sVFCQz-WaPCN/pub?start=true&loop=false&delayms=10000000", new=2)
            time.sleep(8)
            keyboard = PyKeyboard()
            keyboard.press_key(keyboard.control_l_key)
            keyboard.press_key(keyboard.shift_l_key)
            keyboard.tap_key("f")
            keyboard.release_key(keyboard.control_l_key)
            keyboard.release_key(keyboard.shift_l_key)
        if  "04  54  40  62  b1  32  80" in UID and currentUID != "04  54  40  62  b1  32  80":
            print "here"
            currentUID = "04  54  40  62  b1  32  80"
            webbrowser.open("https://docs.google.com/presentation/d/e/2PACX-1vQtUXpepAtAUCUgr_BKHEWZTWMrW3_ycJRMXZpnCesW3TUKufx-BgJGC3GS9J6gs2xzYJH7naG_F3ko/pub?start=true&loop=false&delayms=1000000&slide=id.p", new=2)
            time.sleep(8)
            keyboard = PyKeyboard()
            keyboard.press_key(keyboard.control_l_key)
            keyboard.press_key(keyboard.shift_l_key)
            keyboard.tap_key("f")
            keyboard.release_key(keyboard.control_l_key)
            keyboard.release_key(keyboard.shift_l_key)
        if  "04  11  6b  72  7e  44  80" in UID and currentUID != "04  11  6b  72  7e  44  80":
            print "here"
            currentUID = "04  11  6b  72  7e  44  80"
            webbrowser.open("https://docs.google.com/presentation/d/e/2PACX-1vTAMPNguq_O2g5CowSrEFJ5p15caAE_Go8e7uEuJ0Gu2qtgpUbMx6bZVONNmFuzuPrJpie9aayrKdcD/pub?start=true&loop=false&delayms=1000000&slide=id.g4de11de66b_0_125", new=2)
            time.sleep(8)
            keyboard = PyKeyboard()
            keyboard.press_key(keyboard.control_l_key)
            keyboard.press_key(keyboard.shift_l_key)
            keyboard.tap_key("f")
            keyboard.release_key(keyboard.control_l_key)
            keyboard.release_key(keyboard.shift_l_key)
