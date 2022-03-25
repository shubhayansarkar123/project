import os
import shutil
import time
import pathlib
import hashlib
from  datetime import datetime
from mulpro import *
from multiprocessing import Process
from automated_ledger.test_2 import Test
from automated_ledger.ocr_feeder.ocr_preprocessor import Preprocessor
from automated_ledger.source.sales import Sales
from automated_ledger.source.purchase import Purchase
from automated_ledger.source.chart_of_accounts import ChartOfAccounts
import pandas
import numpy
from automated_ledger.source.financial_statements import FinancialStatements
from automated_ledger.ocr_feeder.feeder import OCR_Feeder

from azureconfig import *

from renaming import *
from  validation import *
from textextraction import *
from rough import *



if __name__=="__main__":
    # for i in os.listdir('mixed_files/sales_849787ec859abe56b41bed1ea893ea77'):
    #     exttype = pathlib.Path(i).suffix
    #     # print()
    #     if (exttype in ['.jpg', '.jpeg']):

    #         oc=extractiontext.imgext(f'mixed_files/sales_849787ec859abe56b41bed1ea893ea77/{i}')
    #         print(oc)
    
    while True:
            path='sales'
            path1='purchase'
            p1 = Process(target=salesp(path))
            p1.start()
            p2 = Process(target=purchasep(path1))
            p2.start()

        # 
                    # break



                        
