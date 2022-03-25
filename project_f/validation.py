# for classification of the pdf and jpg files to two groups,one which will consist of invoices which are valid and other group will contain invalid files
# to create two separate list to store the images of valid and invalid invoices 7/12/2021
import os

import glob2 as glob
import re
import pathlib
import pytesseract
import pdfplumber
import shutil
from timeit import default_timer as timer
import time
import datetime
import hashlib


# from imageprepro import *
# from pdfprepro import *

# pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



dir1='validation'
class validation():
    #clssifier which will validate the files ......
    def classifier(inputpath):
        # STEP 1: Check if `directory` exists
        if not os.path.exists(inputpath):
            print("STATUS: [ERROR] Specified directory does not exist")
        else:
            print("STATUS: [SUCCESS] (STEP 1) Speciifed directory exists...continuing...")
        # STEP 2: Check if `renamed directory` exists
        if not os.path.exists(dir1):
            print("STATUS: [ERROR] Specified directory does not exist...making it...")
            os.mkdir(dir1)
        else:
            print("STATUS: [SUCCESS] (STEP 2) Speciifed directory exists....continuing...")
        dir2=f'{dir1}/{inputpath}'
        os.mkdir(dir2)

        valid=f'{dir2}/valid'
        invalid=f'{dir2}/invalid'


        invalid_formats=f'{dir2}/invalid_formats'

        os.mkdir(valid)
        os.mkdir(invalid)

        os.mkdir(invalid_formats)

        originalpath=f'mixed_files/{inputpath}'
        # print(originalpath)
        print(f'....................validating <{len(os.listdir(originalpath))}> files.................')
        count=[]
        vi=0
        vp=0
        ip=0
        ii=0
        for i in (os.listdir(originalpath)):
            print(i)
            count.append(i)
            
           
            start=time.time()

            # print(len(os.listdir(inputpath)-i))
            exttype = pathlib.Path(i).suffix # taking the extensions from the given files from the path
            src=f'{originalpath}/{i}'
            # print(src)
            if (exttype in ['.jpg', '.jpeg','.png']):#image validation
                try:
                    text = pytesseract.image_to_string(src).lower()
                    print(text)
                    ### for invoice
                    
                    x = re.findall(
                        'bill|invoice|discount|invoice number|invoice date|due date|invoice amount|gst|pan|shipper|consignee|hsn|gstin|sac',
                        text)  # looking for the following keywords in the following text to classify the invoice as valid or not
                    if x:
                        shutil.copy(src,valid) # copying valid files to destination
                        print(f"{i} is valid image........")
                        vi=vi+1
                    else:
                        shutil.copy(src,invalid)# copying invalid files to destination
                        print(f"{i} is invalid image........")
                        ii=ii+1
                except:
                    pass
                    print('could  not read...')
                    
            elif (exttype in ['.pdf','.PDF']):#pdf validation
                try:
                    with pdfplumber.open(src) as pdf:
                        page = pdf.pages[0]
                        text = page.extract_text(x_tolerance=2, y_tolerance=0)
                        print(text)
                        
                        x = re.findall(
                            'bill|invoice|discount|invoice number|invoice date|due date|invoice amount|gst|pan|shipper|consignee|hsn|gstin|sac',
                            text)
                        if x:
                            shutil.copy(src,valid)# copying valid files to destination
                            print(f"{i} is valid pdf........")
                            vp=vp+1
                        else:
                            shutil.copy(src,invalid)# copying invalid files to destination
                            print(f"{i} is invalid pdf........")
                            ip=ip+1
                except:
                    pass
                    print('could  not read...')

            else:
                shutil.copy(src,invalid_formats)#for other invalid formats
                print(f"{i} is of an invalid format........")
                
            end=time.time()
            
            print(f"{len(count)} >>> execution time of {i} is {end-start} seconds")
            print(f"files left.......{len(os.listdir(originalpath))-(len(count))}")
        
        
            

        print('done validating......................')
        print(f"valid images >> {vi}")
        print(f"invalid images >> {ip}")
        print(f"valid pdfs >> {vp}")
        print(f"invalid pdfs >> {ip}")
        print(f"invalid formats >> {len(os.listdir(invalid_formats))}")
        return valid
