import pytesseract
import shutil
import os
import random
import re
import pandas as pd
import pathlib
from collections import namedtuple
try:
    from PIL import Image
except ImportError:
    import Image
import cv2
import pdfplumber
# import 

punctuation='!#^*  |'
img_name=[]
img_txt=[]
pdf_name=[]
pdf_txt=[]

class extractiontext:
    def imgext(path):
        # text = pytesseract.image_to_string(cv2.imread(path),lang='eng')
        # textdoc1=text

        # return textdoc1.lower()
        image1 = Image.open(r'C:\')
        im1 = image1.convert('RGB')
        im1.save(r'C:\Users\Ron\Desktop\Test\myFirstImage.pdf')
    

    def pdfext(path):
        invoice = pdfplumber.open(path)
        ocr_extract = ""
        
        ## number of pages
        n_pages = len(invoice.pages)
        
        ## loop to read all pages
        for i in range(n_pages):
            ## selecting the i-th page
            page = invoice.pages[i]
            
            ## text extraction
            text = page.extract_text()
            ocr_extract = ocr_extract + text
        return ocr_extract.lower()

