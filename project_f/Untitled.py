import re
import pathlib
import pytesseract
import pdfplumber
import cv2
from PIL import Image
# def imgext(path):
#     img=cv2.imread(path)
#     # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     text = pytesseract.image_to_string(img)
#     # textdoc1=text
#     return text.lower()
def ocr_function(path):

    '''
    Parameters
    ----------
    path : address of input file

    Returns
    -------
    raw ocr text

    '''
    ## extracting file extension
    file_extension = pathlib.Path(path).suffix
    # print("File Extension: ",file_extension)

    # ----- PDF OCR -----
    if file_extension in ['.pdf']:      
        ## performing OCR for PDF
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
            ## loop ends
        ## if ends
        
    # ----- Image OCR -----
    elif file_extension in ['.jpg','.jpeg','.png']: ##added .png
        ## performing OCR for Images
        invoice = cv2.imread(path)
        ocr_extract = pytesseract.image_to_string(invoice)

    # ----- Exception -----
    else:
        raise Exception("Invalid file format, File extension: "+file_extension)
        
    return(ocr_extract.lower())
def imgext(path):
    # text = pytesseract.image_to_string(cv2.imread(path),lang='eng')
    # textdoc1=text
    # return textdoc1.lower()
    image1 = Image.open(path)
    im1 = image1.convert('RGB')
    im1.save(f'{path}.pdf')
    text=pdfext(f'{path}.pdf')
    return text
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
oc=ocr_function('purchase/IMG_20220303_165640.jpg.pdf')
print(oc)



