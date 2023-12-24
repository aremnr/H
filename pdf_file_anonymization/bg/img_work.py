import pytesseract
from pytesseract import Output
import cv2
import os
import output_parser
import shutil
import numpy as np

def start():
    if not(os.path.isdir("Output")):
        os.mkdir("Output")
    if not(os.path.isdir("temp_imges_for_pdf")):
        os.mkdir("temp_imges_for_pdf")

def pdf():
    start()
    PageNumber = 0
    PagesList = []
    for a,b,files in os.walk("temp_imgs/"):
        del(a)
        del(b)
    
    for s in sorted(files):
        filter = ["Фамилия", "Имя", "Отчество","Год", "Месяц", "Дату и место рождения", "Семейное положение", "Социальное положение", "Имущественное положение", "Образование", "Профессию", "Доходы", "семейное, социальное, имущественное положение", "Дата выдачи"]
        filter_r = [*filter, "(при", "наличии)", "(при наличии)", "при наличии", "", '\0', "\n", ]
        img = cv2.imread(f"temp_imgs/{s}")
        d = pytesseract.image_to_data(img, output_type=Output.DICT, lang="rus")
        n_boxes = len(d['level'])
        flag = False
        check = 0
        for i in range(n_boxes-3):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            if d["text"][i] in filter:
                flag = True
                check = 3  
            elif flag and d["text"][i] not in filter_r and check >=0:
                temp = i
                while(d["text"][temp] != "" and temp+1<len(d["text"])):
                    temp+=1
                    h = max(h, d["height"][temp])
                w = (d["left"][temp]+d["width"][temp]-x)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)
                flag = False  
            check-=1
            if (not(check)):
                falg = False
        cv2.imwrite(f'temp_imges_for_pdf/output_img{PageNumber}.png', img)
        PagesList.append(f'output_img{PageNumber}.png')
        PageNumber+=1
    
    output_parser.convert_to_pdf(PagesList)

def img(path):
    start()
    img = cv2.imread(path)
    d = pytesseract.image_to_data(img, output_type=Output.DICT, lang="rus")
    n_boxes = len(d['level'])
    flag = False
    for i in range(n_boxes-1):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        if ((d["text"][i] == "Фамилия" and d["text"][i+1] != "Имя") or (d["text"][i] == "Имя" and d["text"][i+1] != "Отчество") or (d["text"][i] == "Отчество" and d["text"][i+1] != "(при")):
            flag = True  
        elif flag:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), -1)
            flag = False
    cv2.imwrite(f'Outut/output_img.png', img)
    shutil("temp_imgs")
    if (os.path.isdir("temp_imges_for_pdf")):
        shutil.rmtree("temp_imges_for_pdf")