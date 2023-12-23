import pytesseract
from pytesseract import Output
import cv2
import pathlib
import os

def main():
    
    img = cv2.imread(f"/home/ar/Documents/Hachaton/temp_imgs/out0.png")
    d = pytesseract.image_to_data(img, output_type=Output.DICT, lang="rus")
    n_boxes = len(d['level'])
    while(d["text"].count("")>0 or d["text"].count(" ")>0 or d["text"].count("  ")>0):
        if d["text"].count("")>0:
            i = d["text"].index("")
        elif d["text"].count(" ")>0:
            i = d["text"].index(" ")
        elif d["text"].count("  ")>0:
            i = d["text"].index("  ")
        elif d["text"].count("-")>0:
            i = d["text"].index("-")
        d["level"].pop(i)
        d['left'].pop(i)
        d['top'].pop(i)
        d['width'].pop(i)
        d['height'].pop(i)
        d["text"].pop(i)
        
    n_boxes = len(d['level'])
    flag = False
    for i in range(n_boxes-1):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        if ((d["text"][i] == "Фамилия" and d["text"][i+1] != "Имя") or (d["text"][i] == "Имя" and d["text"][i+1] != "Отчество") or (d["text"][i] == "Отчество" and d["text"][i+1] != "(при")):
           flag =  True  
        elif flag:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), -1)
            flag = False
    print(d["text"])
    cv2.imshow('img', img)
    cv2.waitKey(0)
    exit()

        






