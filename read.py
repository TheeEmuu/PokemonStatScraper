from PIL import Image, ImageEnhance, ImageFilter
from PIL import ImageGrab
import cv2
import pyautogui as mouse

import json

import time

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\\Programs\\Tesseract\\tesseract.exe'

# # read from main screen
# for i in range(0, 3):
#     for i in range(0, 10):
#         w = ImageGrab.grab(bbox=(1100,65 + 80 * i,1250,85 + 80 * i))
#         w = pytesseract.image_to_string(w).strip().replace("\n\n"," ")
#     mouse.click(1450,900)
#     time.sleep(1)

def scrollDown():
    for i in range(0, 5):
        mouse.scroll(-5000)
    time.sleep(0.5)

def scrollUp():
    for i in range(0, 5):
        mouse.scroll(5000)
    time.sleep(0.5)

def getName():
    w = ImageGrab.grab(bbox=(1265,150,1500,175))
    name = pytesseract.image_to_string(w).strip().replace("\n\n"," ")
    return name

def splitData(str):
    x = str.split(" ")

    try:
        value = round(float(x.pop(len(x) - 1).strip("%"))/100, 3)
    except:
        value = -1
    
    name = " ".join(x)
    
    return {name : value}

def click(x, y):
    mouse.click(x, y)
    mouse.moveTo(1400,65)
    time.sleep(0.5)

toJson = []

click(1250, 100)

for k in range(0,3):
    current = {
        "name": "missingno",
        "partners" : [],
        "moves" : [],
        "ability" : [],
        "nature" : [],
        "item" : []
    }

    #name
    name = getName()
    current["name"] = name

    #partners
    scrollDown()
    if(name != getName()):
        for i in range(0,10):
            w = ImageGrab.grab(bbox=(1100, 110 + 80 * i, 1250, 135 + 80 * i))
            w = pytesseract.image_to_string(w).strip().replace("\n\n"," ")
            if(w != ""):
                current["partners"].append(w)
    else:
        for i in range(0,6):
            w = ImageGrab.grab(bbox=(1100, 435 + 80 * i, 1250, 510 + 80 * i))
            w = pytesseract.image_to_string(w).strip().replace("\n\n"," ")
            if(w != ""):
                current["partners"].append(w)
    scrollUp()


    #moves
    click(1135, 360)
    scrollDown()
    if(name != getName()):
        for i in range(0,10):
            w = ImageGrab.grab(bbox=(1100, 185 + 65 * i, 1550, 220 + 65 * i))
            w = pytesseract.image_to_string(w).strip().replace("\n\n"," ")
            if(w != ""):
                val = splitData(w)
                current["moves"].append(val)
    else:
        for i in range(0,8):
            w = ImageGrab.grab(bbox=(1100, 430 + 65 * i, 1550, 465 + 65 * i))
            w = pytesseract.image_to_string(w).strip().replace("\n\n"," ")
            if(w != ""):
                val = splitData(w)
                current["moves"].append(val)
    scrollUp()

    #abilites
    click(1230,360)
    for i in range(0,5):
        w = ImageGrab.grab(bbox=(1100, 435 + 65 * i, 1550, 465 + 65 * i))
        w = pytesseract.image_to_string(w).strip().replace("\n\n"," ")
        if(w != ""):
            val = splitData(w)
            current["ability"].append(val)

    #nature
    click(1325, 360)
    for i in range(0,5):
        w = ImageGrab.grab(bbox=(1100, 435 + 65 * i, 1550, 465 + 65 * i))
        w = pytesseract.image_to_string(w).strip().replace("\n\n"," ")
        if(w != ""):
            val = splitData(w)
            current["nature"].append(val)

    #item
    click(1425,360)
    for i in range(0,5):
        w = ImageGrab.grab(bbox=(1100, 435 + 65 * i, 1550, 465 + 65 * i))
        w = pytesseract.image_to_string(w).strip().replace("\n\n"," ")
        if(w != ""):
            val = splitData(w)
            current["item"].append(val)

    toJson.append(current)
    # with open("data.json") as json_file:
    #     feeds = json.load(json_file)

    # feeds.append(current)

    # with open("data.json", 'w') as json_file:
    #     json.dump(feeds, json_file, indent = 2)
    

    time.sleep(2)
    click(1552,186)


with open("data.json", 'w') as json_file:
    json.dump(toJson, json_file, indent=2)