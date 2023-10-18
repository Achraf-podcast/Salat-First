import requests, datetime, pyautogui, keyboard, os, time
from bs4 import BeautifulSoup
import lxml
from itertools import zip_longest

adans = []
content = requests.get('https://lematin.ma/horaire-priere-safi.html').content
soup = BeautifulSoup(content, "lxml")

def sir_tsali():
    num = 0
    os.system('start adan.mp3')
    keyboard_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "`", "-", "=", "[", "]", "\\", ";", "'", ",", ".", "/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", '"', "<", ">", "?", "capslock", "space", "tab", "enter", "backspace", "escape", "shift", "ctrl", "alt", "win"]
    for l in keyboard_keys:
        keyboard.block_key(l)

    pyautogui.FAILSAFE = False
    while num != 3600:
        num += 1
        pyautogui.moveTo(0, 0)

    for l in keyboard_keys:
        keyboard.unblock_key(l)

def get_adans():
    global adans
    sobh = soup.find_all("div", {"class":"col-6 time"})[0].text
    dohr = soup.find_all("div", {"class":"col-6 time"})[2].text
    asr = soup.find_all("div", {"class":"col-6 time"})[3].text
    maghrib = soup.find_all("div", {"class":"col-6 time"})[4].text
    ichae = soup.find_all("div", {"class":"col-6 time"})[5].text

    adans.append(sobh.replace('\n', ''))
    adans.append(dohr.replace('\n', ''))
    adans.append(asr.replace('\n', ''))    
    adans.append(maghrib.replace('\n', ''))
    adans.append(ichae.replace('\n', ''))

get_adans()

while True:
    current_time = (datetime.datetime.now().time()).strftime("%H:%M")
    if "00:" in current_time:
        get_adans()
        print(adans)
    else:
        if current_time in adans:
            sir_tsali()
    time.sleep(60)
