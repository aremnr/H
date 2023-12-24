import pytesseract
from pytesseract import Output
import cv2
import os
import output_parser
import shutil


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
        img = cv2.imread(f"temp_imgs/{s}")
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