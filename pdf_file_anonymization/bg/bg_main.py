import PDF_processing
import IMG_processing
import argparse
import os
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help = 'File path')
    parser.add_argument('-f', help='File format')
    return parser

def start_pdf(path):
    PDF_processing.pdf_processing(path)

def start_png(path):
    IMG_processing.img_processing(path)

if __name__ == "__main__":
    parser = create_parser()
    pars_args = parser.parse_args()
    path = pars_args.p
    format = pars_args.f
    serv_var = os.path.dirname(__file__)
    os.chdir(serv_var)
    if (format == "png" or format == "jpg"):
        start_png(path)
    if (format == "pdf"):
        start_pdf(path)