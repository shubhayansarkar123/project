import os
import shutil
import time
import pathlib
import hashlib
from  datetime import datetime


# from ledger.ledger1 import *
# from ledger.ocr_feeder.ocr_preprocessor import Preprocessor
# from ledger.source.sales import Sales
# from ledger.source.purchase import Purchase
# from ledger.source.chart_of_accounts import ChartOfAccounts
# from ledger.source.financial_statements import FinancialStatements
# from ledger.ocr_feeder.feeder import OCR_Feeder
import pandas
import numpy
from azureconfig import *

from renaming import *
from  validation import *
from textextraction import *
from rough import *

blobforinvoice='DefaultEndpointsProtocol=https;AccountName=blobforinvoice;AccountKey=2uOdjZvVY0FGqZ+vPEGjm4JutnEpwv6iGiPe5Pn2W2goBIgOzo3XiLNXqQMhcIpx74Dy732rA48wcVPw+T5L5w==;EndpointSuffix=core.windows.net'
vitwostorage='DefaultEndpointsProtocol=https;AccountName=vitwouatstorage;AccountKey=68poQJY9EJyIFD2mmbOmAoiTEM1gTHaCWBK0OfclwoLFKxyXtcrAtiOPmpRMthMO1XBB6nL5aflpzprKEgOLtQ==;EndpointSuffix=core.windows.net'
uploadabl='DefaultEndpointsProtocol=https;AccountName=uploadable;AccountKey=a9hpbeMTgoKu7a3mxd5eF2DnJTyYS/mfaXr5bNPOVvu21UVGwQxcMcF1Fc7KM7tdTEBzq7ECk4YLiosn2Ux6zg==;EndpointSuffix=core.windows.net'

def salesp(path):

        
    # deleteblob('sales-output')

    bname=blobname('sales-input',cnstr=uploadabl)

    if len(bname)>0:

        # print(bname)
        # text = str(datetime.datetime.now()) 
        # uid = hashlib.md5(text.encode()).hexdigest()

        # # print(text,uid)
        # simg_n=[]
        # simg_t=[]
        # spdf_t=[]
        # spdf_n=[]
        # pimg_n=[]
        # pimg_t=[]
        # ppdf_t=[]
        # ppdf_n=[]

        # #paths of valid images and pdf....


        # path='sales'
        # path1='purchase'
        # di=f'fol_{uid}'
        # pat=f'{path}_{uid}'
        # pat1=f'{path1}_{uid}'
        # directory='extracted'
        # dirr=f'{directory}/{di}/{pat}'
        # dirr1=f'{directory}/{di}/{pat1}'


        # for f1 in os.listdir('sales'):
        #     os.remove(f'{path}/{f1}')
        # for f1 in os.listdir('purchase'):
        #     os.remove(f'{path1}/{f1}')

        for do in os.listdir(path): 
            bnam=blobname('sales-input',cnstr=uploadabl)
            for bn in bnam:
                if str(bn)==str(do):
                    delfile('sales-input',bn,cnstr=uploadabl)
                    break
                else:
                    downfile('sales-input',bn,path,cnstr=uploadabl)
                    with open(f'{path}/{bn}' ,'rb') as da:
                        addtoblob('sales-input-permanent',bn,da,cnstr=uploadabl)
                    delfile('sales-input',bn,cnstr=uploadabl)
                    text = str(datetime.datetime.now()) 
                    uid = hashlib.md5(text.encode()).hexdigest()

                    # print(text,uid)
                    simg_n=[]
                    simg_t=[]
                    spdf_t=[]
                    spdf_n=[]
                    pimg_n=[]
                    pimg_t=[]
                    ppdf_t=[]
                    ppdf_n=[]

                    #paths of valid images and pdf....



                    di=f'fol_{uid}'
                    pat=f'{path}_{uid}'
                    # pat1=f'{path1}_{uid}'
                    directory='extracted'
                    dirr=f'{directory}/{di}/{pat}'
                    # dirr1=f'{directory}/{di}/{pat1}'





                    #calling functions....
                    svalid=renamed_files.convert_filename(path,bn)
                    # pvalid=renamed_files.convert_filename(path1,)
                    # svalidimg,svalidpdf=validation.classifier(path)
                    # pvalidimg,pvalidpdf=validation.classifier(path1)
                    print("extraction started...")

                    if not os.path.exists(directory):
                        os.mkdir(directory)
                    if not os.path.exists(f'{directory}/{di}'):
                        os.mkdir(f'{directory}/{di}')
                    if not os.path.exists(dirr):
                        os.mkdir(dirr)

                    # if not os.path.exists(dirr1):
                    #     os.mkdir(dirr1)




                    for file in os.listdir(svalid):
                        exttype = pathlib.Path(file).suffix
                        if (exttype in ['.jpg', '.jpeg','.png']):
                            simg_n.append(file)
                            r=extractiontext.imgext(f'{svalid}/{file}')
                            l=(readex(r))
                            dd=pd.DataFrame(l)
                            dd.InvDate=pd.to_datetime(dd.InvDate)
                            dd.DueDate=pd.to_datetime(dd.DueDate)

                            # Subhayan
                            dd.to_csv(f'{dirr}/{file}_extracted.csv')
                            with open(f'{dirr}/{file}_extracted.csv','rb') as upl:
                                addtoblob('sales-output',f'{file[21:-(len(exttype))]}.csv',upl,cnstr=uploadabl)

                            # # Arnab
                            # dd.to_csv(f'{dirr}/{file}_extracted.csv')
                            # with open(f'{dirr}/{file}_extracted.csv','rb') as upl:
                            #     addtoblob('sales-output',f'{str(datetime.now())+str(numpy.random.normal(1))}.csv',upl,cnstr=uploadabl)

                                upl.close()
                            simg_t.append(r)

                        if (exttype in ['.pdf','.PDF']):
                            spdf_n.append(file)
                            r1=extractiontext.pdfext(f'{svalid}/{file}')

                            k=readex(r1)


                            dd1=pd.DataFrame(k)
                            dd1.InvDate=pd.to_datetime(dd1.InvDate)

                            dd1.DueDate=pd.to_datetime(dd1.DueDate)
                            dd1.to_csv(f'{dirr}/{file}_extracted.csv')

                            with open(f'{dirr}/{file}_extracted.csv','rb') as upl1:
                                addtoblob('sales-output',f'{file[21:-(len(exttype))]}.csv',upl1,cnstr=uploadabl)


                                upl1.close()

                            spdf_t.append(r1)









                    # for file2 in os.listdir(pvalid):
                    #     exttype = pathlib.Path(file2).suffix
                    #     if (exttype in ['.jpg', '.jpeg']):
                    #         pimg_n.append(file2)
                    #         r2=extractiontext.imgext(f'{pvalid}/{file2}')
                    #         l1=(readex(r2))
                    #         dd11=pd.DataFrame(l1)
                    #         dd11.InvDate=pd.to_datetime(dd11.InvDate)

                    #         dd11.DueDate=pd.to_datetime(dd11.DueDate)
                    #         dd11.to_csv(f'{dirr1}/{file2}_extracted.csv')
                    #         with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl2:
                    #             addtoblob('purchase-output',f'{file2[21:]}.csv',upl2)


                    #             upl2.close()

                    #         pimg_t.append(r2)
                    #     if (exttype in ['.pdf']):
                    #         ppdf_n.append(file2)
                    #         r4=extractiontext.pdfext(f'{pvalid}/{file2}')

                    #         k1=readex(r4)

                    #         dd111=pd.DataFrame(k1)
                    #         dd111.InvDate=pd.to_datetime(dd111.InvDate)

                    #         dd111.DueDate=pd.to_datetime(dd111.DueDate)
                    #         dd111.to_csv(f'{dirr1}/{file2}_extracted.csv')
                    #         with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl3:
                    #             addtoblob('purchase-output',f'{file2[21:]}.csv',upl3)


                    #             upl3.close()

                    #         ppdf_t.append(r4)





                    # pdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                    # 'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                    # 'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                    # 'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                    # 'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                    # 'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                    # 'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                    # 'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                    # 'Signature', 'HSNSAC'])
                    sdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                    'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                    'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                    'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                    'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                    'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                    'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                    'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                    'Signature', 'HSNSAC'])

                    for f in os.listdir(dirr):
                        d1=pd.read_csv(f'{dirr}/{f}')
                        sdf_format=sdf_format.append(d1,ignore_index=True)
                        with open(f"{dirr}/{f}","rb") as d:
                            addtoblob('sales-output-permanent',f,d,cnstr=uploadabl)
                            d.close()

                    # for f in os.listdir(dirr1):
                    #     d1=pd.read_csv(f'{dirr1}/{f}')
                    #     pdf_format=pdf_format.append(d1,ignore_index=True)
                    #     with open(f"{dirr1}/{f}","rb") as d:
                    #         addtoblob('purchase-output-permanent',f,d)
                    #         d.close() 
                    path_D='ledger/ocr_data/'
                    sdf_format.to_csv(path_D+'sales.csv')   
                    # sdf_format.to_csv(path+'purchase.csv')
                    # Test.main()   
                    print('done...........')
                    os.remove(f'{path}/{bn}') 
                    print("deleted")
                    break
    else:print('nothing to show in uploadable...')



def purchasep(path1):
    # deleteblob('purchase-output')
    bname=blobname('purchase-input',cnstr=uploadabl)

    if len(bname)>0:

        # print(bname)
        # text = str(datetime.datetime.now()) 
        # uid = hashlib.md5(text.encode()).hexdigest()

        # # print(text,uid)
        # simg_n=[]
        # simg_t=[]
        # spdf_t=[]
        # spdf_n=[]
        # pimg_n=[]
        # pimg_t=[]
        # ppdf_t=[]
        # ppdf_n=[]

        # #paths of valid images and pdf....


        # path='sales'
        # path1='purchase'
        # di=f'fol_{uid}'
        # pat=f'{path}_{uid}'
        # pat1=f'{path1}_{uid}'
        # directory='extracted'
        # dirr=f'{directory}/{di}/{pat}'
        # dirr1=f'{directory}/{di}/{pat1}'


        # for f1 in os.listdir('sales'):
        #     os.remove(f'{path}/{f1}')
        # for f1 in os.listdir('purchase'):
        #     os.remove(f'{path1}/{f1}')
            for do in os.listdir(path1): 
                bnam=blobname('purchase-input',cnstr=uploadabl)
                for bn in bnam:
                    if str(bn)==str(do):
                        delfile('purchase-input',bn,cnstr=uploadabl)
                        break
                    else:
                        downfile('purchase-input',bn,path1,cnstr=uploadabl)
                        with open(f'{path1}/{bn}' ,'rb') as da:
                            addtoblob('purchase-input-permanent',bn,da,cnstr=uploadabl)
                        delfile('purchase-input',bn,cnstr=uploadabl)
                        text = str(datetime.datetime.now()) 
                        uid = hashlib.md5(text.encode()).hexdigest()

                        # print(text,uid)
                        simg_n=[]
                        simg_t=[]
                        spdf_t=[]
                        spdf_n=[]
                        pimg_n=[]
                        pimg_t=[]
                        ppdf_t=[]
                        ppdf_n=[]

                        #paths of valid images and pdf....



                        di=f'fol_{uid}'
#                         pat=f'{path}_{uid}'
                        pat1=f'{path1}_{uid}'
                        directory='extracted'
#                         dirr=f'{directory}/{di}/{pat}'
                        dirr1=f'{directory}/{di}/{pat1}'


    


                        #calling functions....
                        pvalid=renamed_files.convert_filename(path1,bn)
                        # pvalid=renamed_files.convert_filename(path1,)
                        # svalidimg,svalidpdf=validation.classifier(path)
                        # pvalidimg,pvalidpdf=validation.classifier(path1)
                        print("extraction started...")
                        
                        if not os.path.exists(directory):
                            os.mkdir(directory)
                        if not os.path.exists(f'{directory}/{di}'):
                            os.mkdir(f'{directory}/{di}')
#                         if not os.path.exists(dirr):
#                             os.mkdir(dirr)

                        if not os.path.exists(dirr1):
                            os.mkdir(dirr1)


                        

                        # for file in os.listdir(svalid):
                        #     exttype = pathlib.Path(file).suffix
                        #     if (exttype in ['.jpg', '.jpeg']):
                        #         simg_n.append(file)
                        #         r=extractiontext.imgext(f'{svalid}/{file}')
                        #         l=(readex(r))
                        #         dd=pd.DataFrame(l)
                        #         dd.InvDate=pd.to_datetime(dd.InvDate)
                        #         dd.DueDate=pd.to_datetime(dd.DueDate)
                                
                        #         dd.to_csv(f'{dirr}/{file}_extracted.csv')
                        #         with open(f'{dirr}/{file}_extracted.csv','rb') as upl:
                        #             addtoblob('sales-output',f'{file[21:]}.csv',upl)

                            
                                    
                        #             upl.close()
                        #         simg_t.append(r)
                                
                        #     if (exttype in ['.pdf']):
                        #         spdf_n.append(file)
                        #         r1=extractiontext.pdfext(f'{svalid}/{file}')
                    
                        #         k=readex(r1)
                                
                                
                        #         dd1=pd.DataFrame(k)
                        #         dd1.InvDate=pd.to_datetime(dd1.InvDate)
                                
                        #         dd1.DueDate=pd.to_datetime(dd1.DueDate)
                        #         dd1.to_csv(f'{dirr}/{file}_extracted.csv')

                        #         with open(f'{dirr}/{file}_extracted.csv','rb') as upl1:
                        #             addtoblob('sales-output',f'{file[21:]}.csv',upl1)

                        
                        #             upl1.close()
                            
                        #         spdf_t.append(r1)

                    
                    
                    





                        for file2 in os.listdir(pvalid):
                            exttype = pathlib.Path(file2).suffix
                            if (exttype in ['.jpg', '.jpeg','.png']):
                                pimg_n.append(file2)
                                r2=extractiontext.imgext(f'{pvalid}/{file2}')
                                l1=(readex(r2,sal=False))
                                dd11=pd.DataFrame(l1)
                                dd11.InvDate=pd.to_datetime(dd11.InvDate)
                                
                                dd11.DueDate=pd.to_datetime(dd11.DueDate)
                                dd11.to_csv(f'{dirr1}/{file2}_extracted.csv')
                                with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl2:
                                    addtoblob('purchase-output',f'{file2[21:-(len(exttype))]}.csv',upl2,cnstr=uploadabl)

                                    
                                    upl2.close()

                                pimg_t.append(r2)
                            if (exttype in ['.pdf','.PDF']):
                                ppdf_n.append(file2)
                                r4=extractiontext.pdfext(f'{pvalid}/{file2}')
                    
                                k1=readex(r4,sal=False)
                                
                                dd111=pd.DataFrame(k1)
                                dd111.InvDate=pd.to_datetime(dd111.InvDate)
                            
                                dd111.DueDate=pd.to_datetime(dd111.DueDate)
                                dd111.to_csv(f'{dirr1}/{file2}_extracted.csv')
                                with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl3:
                                    addtoblob('purchase-output',f'{file2[21:-(len(exttype))]}.csv',upl3,cnstr=uploadabl)

                            
                                    upl3.close()
                                
                                ppdf_t.append(r4)


                        
                        
                    
                        pdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                        'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                        'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                        'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                        'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                        'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                        'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                        'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                        'Signature', 'HSNSAC'])
                        # sdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                        # 'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                        # 'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                        # 'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                        # 'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                        # 'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                        # 'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                        # 'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                        # 'Signature', 'HSNSAC'])
                        
                        # for f in os.listdir(dirr):
                        #     d1=pd.read_csv(f'{dirr}/{f}')
                        #     sdf_format=sdf_format.append(d1,ignore_index=True)
                        #     with open(f"{dirr}/{f}","rb") as d:
                        #         addtoblob('sales-output-permanent',f,d)
                        #         d.close()

                        for f in os.listdir(dirr1):
                            d1=pd.read_csv(f'{dirr1}/{f}')
                            pdf_format=pdf_format.append(d1,ignore_index=True)
                            with open(f"{dirr1}/{f}","rb") as d:
                                addtoblob('purchase-output-permanent',f,d,cnstr=uploadabl)
                                d.close() 
                        path_D='ledger/ocr_data/'
                        # sdf_format.to_csv(path_D+'sales.csv')   
                        pdf_format.to_csv(path_D+'purchase.csv')
                        # Test.main()   
                        print('done...........')
                        os.remove(f'{path1}/{bn}')
                        print("deleted") 
                        break
                    # break
                
                        
    else:print('nothing to show uploadable...')  


def salespa(path):
        
    # deleteblob('sales-output')

    bname=blobname('sales-input',cnstr=vitwostorage)

    if len(bname)>0:

        # print(bname)
        # text = str(datetime.datetime.now()) 
        # uid = hashlib.md5(text.encode()).hexdigest()

        # # print(text,uid)
        # simg_n=[]
        # simg_t=[]
        # spdf_t=[]
        # spdf_n=[]
        # pimg_n=[]
        # pimg_t=[]
        # ppdf_t=[]
        # ppdf_n=[]

        # #paths of valid images and pdf....


        # path='sales'
        # path1='purchase'
        # di=f'fol_{uid}'
        # pat=f'{path}_{uid}'
        # pat1=f'{path1}_{uid}'
        # directory='extracted'
        # dirr=f'{directory}/{di}/{pat}'
        # dirr1=f'{directory}/{di}/{pat1}'


        # for f1 in os.listdir('sales'):
        #     os.remove(f'{path}/{f1}')
        # for f1 in os.listdir('purchase'):
        #     os.remove(f'{path1}/{f1}')

        for do in os.listdir(path): 
            bnam=blobname('sales-input',cnstr=vitwostorage)
            for bn in bnam:
                if str(bn)==str(do):
                    delfile('sales-input',bn,cnstr=vitwostorage)
                    break
                else:
                    downfile('sales-input',bn,path,cnstr=vitwostorage)
                    with open(f'{path}/{bn}' ,'rb') as da:
                            addtoblob('sales-input-permanent',bn,da,cnstr=uploadabl)
                    delfile('sales-input',bn,cnstr=vitwostorage)
                    text = str(datetime.datetime.now()) 
                    uid = hashlib.md5(text.encode()).hexdigest()

                    # print(text,uid)
                    simg_n=[]
                    simg_t=[]
                    spdf_t=[]
                    spdf_n=[]
                    pimg_n=[]
                    pimg_t=[]
                    ppdf_t=[]
                    ppdf_n=[]

                    #paths of valid images and pdf....



                    di=f'fol_{uid}'
                    pat=f'{path}_{uid}'
                    # pat1=f'{path1}_{uid}'
                    directory='extracted'
                    dirr=f'{directory}/{di}/{pat}'
                    # dirr1=f'{directory}/{di}/{pat1}'





                    #calling functions....
                    svalid=renamed_files.convert_filename(path,bn)
                    # pvalid=renamed_files.convert_filename(path1,)
                    # svalidimg,svalidpdf=validation.classifier(path)
                    # pvalidimg,pvalidpdf=validation.classifier(path1)
                    print("extraction started...")

                    if not os.path.exists(directory):
                        os.mkdir(directory)
                    if not os.path.exists(f'{directory}/{di}'):
                        os.mkdir(f'{directory}/{di}')
                    if not os.path.exists(dirr):
                        os.mkdir(dirr)

                    # if not os.path.exists(dirr1):
                    #     os.mkdir(dirr1)




                    for file in os.listdir(svalid):
                        exttype = pathlib.Path(file).suffix
                        if (exttype in ['.jpg', '.jpeg','.png']):
                            simg_n.append(file)
                            r=extractiontext.imgext(f'{svalid}/{file}')
                            l=(readex(r))
                            dd=pd.DataFrame(l)
                            dd.InvDate=pd.to_datetime(dd.InvDate)
                            dd.DueDate=pd.to_datetime(dd.DueDate)

                            dd.to_csv(f'{dirr}/{file}_extracted.csv')
                            with open(f'{dirr}/{file}_extracted.csv','rb') as upl:
                                addtoblob('sales-output',f'{file[21:-(len(exttype))]}.csv',upl,cnstr=vitwostorage)



                                upl.close()
                            simg_t.append(r)

                        if (exttype in ['.pdf','.PDF']):
                            spdf_n.append(file)
                            r1=extractiontext.pdfext(f'{svalid}/{file}')

                            k=readex(r1)


                            dd1=pd.DataFrame(k)
                            dd1.InvDate=pd.to_datetime(dd1.InvDate)

                            dd1.DueDate=pd.to_datetime(dd1.DueDate)
                            dd1.to_csv(f'{dirr}/{file}_extracted.csv')

                            with open(f'{dirr}/{file}_extracted.csv','rb') as upl1:
                                addtoblob('sales-output',f'{file[21:-(len(exttype))]}.csv',upl1,cnstr=vitwostorage)


                                upl1.close()

                            spdf_t.append(r1)









                    # for file2 in os.listdir(pvalid):
                    #     exttype = pathlib.Path(file2).suffix
                    #     if (exttype in ['.jpg', '.jpeg']):
                    #         pimg_n.append(file2)
                    #         r2=extractiontext.imgext(f'{pvalid}/{file2}')
                    #         l1=(readex(r2))
                    #         dd11=pd.DataFrame(l1)
                    #         dd11.InvDate=pd.to_datetime(dd11.InvDate)

                    #         dd11.DueDate=pd.to_datetime(dd11.DueDate)
                    #         dd11.to_csv(f'{dirr1}/{file2}_extracted.csv')
                    #         with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl2:
                    #             addtoblob('purchase-output',f'{file2[21:]}.csv',upl2)


                    #             upl2.close()

                    #         pimg_t.append(r2)
                    #     if (exttype in ['.pdf']):
                    #         ppdf_n.append(file2)
                    #         r4=extractiontext.pdfext(f'{pvalid}/{file2}')

                    #         k1=readex(r4)

                    #         dd111=pd.DataFrame(k1)
                    #         dd111.InvDate=pd.to_datetime(dd111.InvDate)

                    #         dd111.DueDate=pd.to_datetime(dd111.DueDate)
                    #         dd111.to_csv(f'{dirr1}/{file2}_extracted.csv')
                    #         with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl3:
                    #             addtoblob('purchase-output',f'{file2[21:]}.csv',upl3)


                    #             upl3.close()

                    #         ppdf_t.append(r4)





                    # pdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                    # 'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                    # 'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                    # 'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                    # 'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                    # 'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                    # 'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                    # 'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                    # 'Signature', 'HSNSAC'])
                    sdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                    'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                    'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                    'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                    'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                    'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                    'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                    'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                    'Signature', 'HSNSAC'])

                    for f in os.listdir(dirr):
                        d1=pd.read_csv(f'{dirr}/{f}')
                        sdf_format=sdf_format.append(d1,ignore_index=True)
                        with open(f"{dirr}/{f}","rb") as d:
                            addtoblob('sales-output-permanent',f,d,cnstr=uploadabl)
                            d.close()

                    # for f in os.listdir(dirr1):
                    #     d1=pd.read_csv(f'{dirr1}/{f}')
                    #     pdf_format=pdf_format.append(d1,ignore_index=True)
                    #     with open(f"{dirr1}/{f}","rb") as d:
                    #         addtoblob('purchase-output-permanent',f,d)
                    #         d.close() 
                    path_D='automated_ledger/ocr_data/'
                    sdf_format.to_csv(path_D+'sales.csv')   
                    # sdf_format.to_csv(path+'purchase.csv')
                    # Test.main()   
                    print('done...........')
                    os.remove(f'{path}/{bn}') 
                    print("deleted")
                    break
    else:print('nothing to show vitwostorage.....')



def purchasepa(path1):
    # deleteblob('purchase-output')
    bname=blobname('purchase-input',cnstr=vitwostorage)

    if len(bname)>0:

        # print(bname)
        # text = str(datetime.datetime.now()) 
        # uid = hashlib.md5(text.encode()).hexdigest()

        # # print(text,uid)
        # simg_n=[]
        # simg_t=[]
        # spdf_t=[]
        # spdf_n=[]
        # pimg_n=[]
        # pimg_t=[]
        # ppdf_t=[]
        # ppdf_n=[]

        # #paths of valid images and pdf....


        # path='sales'
        # path1='purchase'
        # di=f'fol_{uid}'
        # pat=f'{path}_{uid}'
        # pat1=f'{path1}_{uid}'
        # directory='extracted'
        # dirr=f'{directory}/{di}/{pat}'
        # dirr1=f'{directory}/{di}/{pat1}'


        # for f1 in os.listdir('sales'):
        #     os.remove(f'{path}/{f1}')
        # for f1 in os.listdir('purchase'):
        #     os.remove(f'{path1}/{f1}')
            for do in os.listdir(path1): 
                bnam=blobname('purchase-input',cnstr=vitwostorage)
                for bn in bnam:
                    if str(bn)==str(do):
                        delfile('purchase-input',bn,cnstr=vitwostorage)
                        break
                    else:
                        downfile('purchase-input',bn,path1,cnstr=vitwostorage)
                        with open(f'{path1}/{bn}' ,'rb') as da:
                            addtoblob('purchase-input-permanent',bn,da,cnstr=uploadabl)
                        delfile('purchase-input',bn,cnstr=vitwostorage)
                        text = str(datetime.datetime.now()) 
                        uid = hashlib.md5(text.encode()).hexdigest()

                        # print(text,uid)
                        simg_n=[]
                        simg_t=[]
                        spdf_t=[]
                        spdf_n=[]
                        pimg_n=[]
                        pimg_t=[]
                        ppdf_t=[]
                        ppdf_n=[]

                        #paths of valid images and pdf....



                        di=f'fol_{uid}'
#                         pat=f'{path}_{uid}'
                        pat1=f'{path1}_{uid}'
                        directory='extracted'
#                         dirr=f'{directory}/{di}/{pat}'
                        dirr1=f'{directory}/{di}/{pat1}'


    


                        #calling functions....
                        pvalid=renamed_files.convert_filename(path1,bn)
                        # pvalid=renamed_files.convert_filename(path1,)
                        # svalidimg,svalidpdf=validation.classifier(path)
                        # pvalidimg,pvalidpdf=validation.classifier(path1)
                        print("extraction started...")
                        
                        if not os.path.exists(directory):
                            os.mkdir(directory)
                        if not os.path.exists(f'{directory}/{di}'):
                            os.mkdir(f'{directory}/{di}')
#                         if not os.path.exists(dirr):
#                             os.mkdir(dirr)

                        if not os.path.exists(dirr1):
                            os.mkdir(dirr1)


                        

                        # for file in os.listdir(svalid):
                        #     exttype = pathlib.Path(file).suffix
                        #     if (exttype in ['.jpg', '.jpeg']):
                        #         simg_n.append(file)
                        #         r=extractiontext.imgext(f'{svalid}/{file}')
                        #         l=(readex(r))
                        #         dd=pd.DataFrame(l)
                        #         dd.InvDate=pd.to_datetime(dd.InvDate)
                        #         dd.DueDate=pd.to_datetime(dd.DueDate)
                                
                        #         dd.to_csv(f'{dirr}/{file}_extracted.csv')
                        #         with open(f'{dirr}/{file}_extracted.csv','rb') as upl:
                        #             addtoblob('sales-output',f'{file[21:]}.csv',upl)

                            
                                    
                        #             upl.close()
                        #         simg_t.append(r)
                                
                        #     if (exttype in ['.pdf']):
                        #         spdf_n.append(file)
                        #         r1=extractiontext.pdfext(f'{svalid}/{file}')
                    
                        #         k=readex(r1)
                                
                                
                        #         dd1=pd.DataFrame(k)
                        #         dd1.InvDate=pd.to_datetime(dd1.InvDate)
                                
                        #         dd1.DueDate=pd.to_datetime(dd1.DueDate)
                        #         dd1.to_csv(f'{dirr}/{file}_extracted.csv')

                        #         with open(f'{dirr}/{file}_extracted.csv','rb') as upl1:
                        #             addtoblob('sales-output',f'{file[21:]}.csv',upl1)

                        
                        #             upl1.close()
                            
                        #         spdf_t.append(r1)

                    
                    
                    





                        for file2 in os.listdir(pvalid):
                            exttype = pathlib.Path(file2).suffix
                            if (exttype in ['.jpg', '.jpeg','.png']):
                                pimg_n.append(file2)
                                r2=extractiontext.imgext(f'{pvalid}/{file2}')
                                l1=(readex(r2,sal=False))
                                dd11=pd.DataFrame(l1)
                                dd11.InvDate=pd.to_datetime(dd11.InvDate)
                                
                                dd11.DueDate=pd.to_datetime(dd11.DueDate)
                                dd11.to_csv(f'{dirr1}/{file2}_extracted.csv')
                                with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl2:
                                    addtoblob('purchase-output',f'{file2[21:-(len(exttype))]}.csv',upl2,cnstr=vitwostorage)

                                    
                                    upl2.close()

                                pimg_t.append(r2)
                            if (exttype in ['.pdf','.PDF']):
                                ppdf_n.append(file2)
                                r4=extractiontext.pdfext(f'{pvalid}/{file2}')
                    
                                k1=readex(r4,sal=False)
                                
                                dd111=pd.DataFrame(k1)
                                dd111.InvDate=pd.to_datetime(dd111.InvDate)
                            
                                dd111.DueDate=pd.to_datetime(dd111.DueDate)
                                dd111.to_csv(f'{dirr1}/{file2}_extracted.csv')
                                with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl3:
                                    addtoblob('purchase-output',f'{file2[21:-(len(exttype))]}.csv',upl3,cnstr=vitwostorage)

                            
                                    upl3.close()
                                
                                ppdf_t.append(r4)


                        
                        
                    
                        pdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                        'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                        'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                        'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                        'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                        'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                        'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                        'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                        'Signature', 'HSNSAC'])
                        # sdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                        # 'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                        # 'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                        # 'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                        # 'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                        # 'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                        # 'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                        # 'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                        # 'Signature', 'HSNSAC'])
                        
                        # for f in os.listdir(dirr):
                        #     d1=pd.read_csv(f'{dirr}/{f}')
                        #     sdf_format=sdf_format.append(d1,ignore_index=True)
                        #     with open(f"{dirr}/{f}","rb") as d:
                        #         addtoblob('sales-output-permanent',f,d)
                        #         d.close()

                        for f in os.listdir(dirr1):
                            d1=pd.read_csv(f'{dirr1}/{f}')
                            pdf_format=pdf_format.append(d1,ignore_index=True)
                            with open(f"{dirr1}/{f}","rb") as d:
                                addtoblob('purchase-output-permanent',f,d,cnstr=uploadabl)
                                d.close() 
                        path_D='automated_ledger/ocr_data/'
                        # sdf_format.to_csv(path_D+'sales.csv')   
                        pdf_format.to_csv(path_D+'purchase.csv')
                        # Test.main()   
                        print('done...........')
                        os.remove(f'{path1}/{bn}') 
                        print("deleted")
                        break
                    # break
                
                        
    else:print('nothing to show in vitowstorage....')  
def salespb(path):
        
    # deleteblob('sales-output')

    bname=blobname('sales-input',cnstr=blobforinvoice)

    if len(bname)>0:

        # print(bname)
        # text = str(datetime.datetime.now()) 
        # uid = hashlib.md5(text.encode()).hexdigest()

        # # print(text,uid)
        # simg_n=[]
        # simg_t=[]
        # spdf_t=[]
        # spdf_n=[]
        # pimg_n=[]
        # pimg_t=[]
        # ppdf_t=[]
        # ppdf_n=[]

        # #paths of valid images and pdf....


        # path='sales'
        # path1='purchase'
        # di=f'fol_{uid}'
        # pat=f'{path}_{uid}'
        # pat1=f'{path1}_{uid}'
        # directory='extracted'
        # dirr=f'{directory}/{di}/{pat}'
        # dirr1=f'{directory}/{di}/{pat1}'


        # for f1 in os.listdir('sales'):
        #     os.remove(f'{path}/{f1}')
        # for f1 in os.listdir('purchase'):
        #     os.remove(f'{path1}/{f1}')

        for do in os.listdir(path): 
            bnam=blobname('sales-input',cnstr=blobforinvoice)
            for bn in bnam:
                if str(bn)==str(do):
                    delfile('sales-input',bn,cnstr=blobforinvoice)
                    break
                else:
                    downfile('sales-input',bn,path,cnstr=blobforinvoice)
                    with open(f'{path}/{bn}' ,'rb') as da:
                        addtoblob('sales-input-permanent',bn,da,cnstr=uploadabl)
                    delfile('sales-input',bn,cnstr=blobforinvoice)
                    text = str(datetime.datetime.now()) 
                    uid = hashlib.md5(text.encode()).hexdigest()

                    # print(text,uid)
                    simg_n=[]
                    simg_t=[]
                    spdf_t=[]
                    spdf_n=[]
                    pimg_n=[]
                    pimg_t=[]
                    ppdf_t=[]
                    ppdf_n=[]

                    #paths of valid images and pdf....



                    di=f'fol_{uid}'
                    pat=f'{path}_{uid}'
                    # pat1=f'{path1}_{uid}'
                    directory='extracted'
                    dirr=f'{directory}/{di}/{pat}'
                    # dirr1=f'{directory}/{di}/{pat1}'





                    #calling functions....
                    svalid=renamed_files.convert_filename(path,bn)
                    # pvalid=renamed_files.convert_filename(path1,)
                    # svalidimg,svalidpdf=validation.classifier(path)
                    # pvalidimg,pvalidpdf=validation.classifier(path1)
                    print("extraction started...")

                    if not os.path.exists(directory):
                        os.mkdir(directory)
                    if not os.path.exists(f'{directory}/{di}'):
                        os.mkdir(f'{directory}/{di}')
                    if not os.path.exists(dirr):
                        os.mkdir(dirr)

                    # if not os.path.exists(dirr1):
                    #     os.mkdir(dirr1)




                    for file in os.listdir(svalid):
                        exttype = pathlib.Path(file).suffix
                        if (exttype in ['.jpg', '.jpeg','.png']):
                            simg_n.append(file)
                            r=extractiontext.imgext(f'{svalid}/{file}')
                            l=(readex(r))
                            dd=pd.DataFrame(l)
                            dd.InvDate=pd.to_datetime(dd.InvDate)
                            dd.DueDate=pd.to_datetime(dd.DueDate)

                            dd.to_csv(f'{dirr}/{file}_extracted.csv')
                            with open(f'{dirr}/{file}_extracted.csv','rb') as upl:
                                addtoblob('sales-output',f'{file[21:-(len(exttype))]}.csv',upl,cnstr=blobforinvoice)



                                upl.close()
                            simg_t.append(r)

                        if (exttype in ['.pdf','.PDF']):
                            spdf_n.append(file)
                            r1=extractiontext.pdfext(f'{svalid}/{file}')

                            k=readex(r1)


                            dd1=pd.DataFrame(k)
                            dd1.InvDate=pd.to_datetime(dd1.InvDate)

                            dd1.DueDate=pd.to_datetime(dd1.DueDate)
                            dd1.to_csv(f'{dirr}/{file}_extracted.csv')

                            with open(f'{dirr}/{file}_extracted.csv','rb') as upl1:
                                addtoblob('sales-output',f'{file[21:-(len(exttype))]}.csv',upl1,cnstr=blobforinvoice)


                                upl1.close()

                            spdf_t.append(r1)









                    # for file2 in os.listdir(pvalid):
                    #     exttype = pathlib.Path(file2).suffix
                    #     if (exttype in ['.jpg', '.jpeg']):
                    #         pimg_n.append(file2)
                    #         r2=extractiontext.imgext(f'{pvalid}/{file2}')
                    #         l1=(readex(r2))
                    #         dd11=pd.DataFrame(l1)
                    #         dd11.InvDate=pd.to_datetime(dd11.InvDate)

                    #         dd11.DueDate=pd.to_datetime(dd11.DueDate)
                    #         dd11.to_csv(f'{dirr1}/{file2}_extracted.csv')
                    #         with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl2:
                    #             addtoblob('purchase-output',f'{file2[21:]}.csv',upl2)


                    #             upl2.close()

                    #         pimg_t.append(r2)
                    #     if (exttype in ['.pdf']):
                    #         ppdf_n.append(file2)
                    #         r4=extractiontext.pdfext(f'{pvalid}/{file2}')

                    #         k1=readex(r4)

                    #         dd111=pd.DataFrame(k1)
                    #         dd111.InvDate=pd.to_datetime(dd111.InvDate)

                    #         dd111.DueDate=pd.to_datetime(dd111.DueDate)
                    #         dd111.to_csv(f'{dirr1}/{file2}_extracted.csv')
                    #         with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl3:
                    #             addtoblob('purchase-output',f'{file2[21:]}.csv',upl3)


                    #             upl3.close()

                    #         ppdf_t.append(r4)





                    # pdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                    # 'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                    # 'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                    # 'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                    # 'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                    # 'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                    # 'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                    # 'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                    # 'Signature', 'HSNSAC'])
                    sdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                    'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                    'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                    'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                    'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                    'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                    'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                    'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                    'Signature', 'HSNSAC'])

                    for f in os.listdir(dirr):
                        d1=pd.read_csv(f'{dirr}/{f}')
                        sdf_format=sdf_format.append(d1,ignore_index=True)
                        with open(f"{dirr}/{f}","rb") as d:
                            addtoblob('sales-output-permanent',f,d,cnstr=uploadabl)
                            d.close()

                    # for f in os.listdir(dirr1):
                    #     d1=pd.read_csv(f'{dirr1}/{f}')
                    #     pdf_format=pdf_format.append(d1,ignore_index=True)
                    #     with open(f"{dirr1}/{f}","rb") as d:
                    #         addtoblob('purchase-output-permanent',f,d)
                    #         d.close() 
                    path_D='ledger/ocr_data/'
                    sdf_format.to_csv(path_D+'sales1.csv')   
                    # sdf_format.to_csv(path+'purchase.csv')
                    # Test.main()   
                    print('done...........')
                    os.remove(f'{path}/{bn}') 
                    print("deleted")
                    break
    else:print('nothing to show blobforinvoice.....')



def purchasepb(path1):
    # deleteblob('purchase-output')
    bname=blobname('purchase-input',cnstr=blobforinvoice)

    if len(bname)>0:

        # print(bname)
        # text = str(datetime.datetime.now()) 
        # uid = hashlib.md5(text.encode()).hexdigest()

        # # print(text,uid)
        # simg_n=[]
        # simg_t=[]
        # spdf_t=[]
        # spdf_n=[]
        # pimg_n=[]
        # pimg_t=[]
        # ppdf_t=[]
        # ppdf_n=[]

        # #paths of valid images and pdf....


        # path='sales'
        # path1='purchase'
        # di=f'fol_{uid}'
        # pat=f'{path}_{uid}'
        # pat1=f'{path1}_{uid}'
        # directory='extracted'
        # dirr=f'{directory}/{di}/{pat}'
        # dirr1=f'{directory}/{di}/{pat1}'


        # for f1 in os.listdir('sales'):
        #     os.remove(f'{path}/{f1}')
        # for f1 in os.listdir('purchase'):
        #     os.remove(f'{path1}/{f1}')
            for do in os.listdir(path1): 
                bnam=blobname('purchase-input',cnstr=blobforinvoice)
                for bn in bnam:
                    if str(bn)==str(do):
                        delfile('purchase-input',bn,cnstr=blobforinvoice)
                        break
                    else:
                        downfile('purchase-input',bn,path1,cnstr=blobforinvoice)
                        with open(f'{path1}/{bn}' ,'rb') as da:
                            addtoblob('purchase-input-permanent',bn,da,cnstr=uploadabl)
                        delfile('purchase-input',bn,cnstr=blobforinvoice)
                        text = str(datetime.datetime.now()) 
                        uid = hashlib.md5(text.encode()).hexdigest()

                        # print(text,uid)
                        simg_n=[]
                        simg_t=[]
                        spdf_t=[]
                        spdf_n=[]
                        pimg_n=[]
                        pimg_t=[]
                        ppdf_t=[]
                        ppdf_n=[]

                        #paths of valid images and pdf....



                        di=f'fol_{uid}'
#                         pat=f'{path}_{uid}'
                        pat1=f'{path1}_{uid}'
                        directory='extracted'
#                         dirr=f'{directory}/{di}/{pat}'
                        dirr1=f'{directory}/{di}/{pat1}'


    


                        #calling functions....
                        pvalid=renamed_files.convert_filename(path1,bn)
                        # pvalid=renamed_files.convert_filename(path1,)
                        # svalidimg,svalidpdf=validation.classifier(path)
                        # pvalidimg,pvalidpdf=validation.classifier(path1)
                        print("extraction started...")
                        
                        if not os.path.exists(directory):
                            os.mkdir(directory)
                        if not os.path.exists(f'{directory}/{di}'):
                            os.mkdir(f'{directory}/{di}')
#                         if not os.path.exists(dirr):
#                             os.mkdir(dirr)

                        if not os.path.exists(dirr1):
                            os.mkdir(dirr1)


                        

                        # for file in os.listdir(svalid):
                        #     exttype = pathlib.Path(file).suffix
                        #     if (exttype in ['.jpg', '.jpeg']):
                        #         simg_n.append(file)
                        #         r=extractiontext.imgext(f'{svalid}/{file}')
                        #         l=(readex(r))
                        #         dd=pd.DataFrame(l)
                        #         dd.InvDate=pd.to_datetime(dd.InvDate)
                        #         dd.DueDate=pd.to_datetime(dd.DueDate)
                                
                        #         dd.to_csv(f'{dirr}/{file}_extracted.csv')
                        #         with open(f'{dirr}/{file}_extracted.csv','rb') as upl:
                        #             addtoblob('sales-output',f'{file[21:]}.csv',upl)

                            
                                    
                        #             upl.close()
                        #         simg_t.append(r)
                                
                        #     if (exttype in ['.pdf']):
                        #         spdf_n.append(file)
                        #         r1=extractiontext.pdfext(f'{svalid}/{file}')
                    
                        #         k=readex(r1)
                                
                                
                        #         dd1=pd.DataFrame(k)
                        #         dd1.InvDate=pd.to_datetime(dd1.InvDate)
                                
                        #         dd1.DueDate=pd.to_datetime(dd1.DueDate)
                        #         dd1.to_csv(f'{dirr}/{file}_extracted.csv')

                        #         with open(f'{dirr}/{file}_extracted.csv','rb') as upl1:
                        #             addtoblob('sales-output',f'{file[21:]}.csv',upl1)

                        
                        #             upl1.close()
                            
                        #         spdf_t.append(r1)

                    
                    
                    





                        for file2 in os.listdir(pvalid):
                            exttype = pathlib.Path(file2).suffix
                            if (exttype in ['.jpg', '.jpeg','.png']):
                                pimg_n.append(file2)
                                r2=extractiontext.imgext(f'{pvalid}/{file2}')
                                l1=(readex(r2,sal=False))
                                dd11=pd.DataFrame(l1)
                                dd11.InvDate=pd.to_datetime(dd11.InvDate)
                                
                                dd11.DueDate=pd.to_datetime(dd11.DueDate)
                                dd11.to_csv(f'{dirr1}/{file2}_extracted.csv')
                                with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl2:
                                    addtoblob('purchase-output',f'{file2[21:-(len(exttype))]}.csv',upl2,cnstr=blobforinvoice)

                                    
                                    upl2.close()

                                pimg_t.append(r2)
                            if (exttype in ['.pdf','.PDF']):
                                ppdf_n.append(file2)
                                r4=extractiontext.pdfext(f'{pvalid}/{file2}')
                    
                                k1=readex(r4,sal=False)
                                
                                dd111=pd.DataFrame(k1)
                                dd111.InvDate=pd.to_datetime(dd111.InvDate)
                            
                                dd111.DueDate=pd.to_datetime(dd111.DueDate)
                                dd111.to_csv(f'{dirr1}/{file2}_extracted.csv')
                                with open(f'{dirr1}/{file2}_extracted.csv','rb') as upl3:
                                    addtoblob('purchase-output',f'{file2[21:-(len(exttype))]}.csv',upl3,cnstr=blobforinvoice)

                            
                                    upl3.close()
                                
                                ppdf_t.append(r4)


                        
                        
                    
                        pdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                        'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                        'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                        'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                        'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                        'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                        'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                        'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                        'Signature', 'HSNSAC'])
                        # sdf_format=pd.DataFrame(columns=['Unnamed: 0', 'Title', 'InvNo', 'InvDate', 'DueDate', 'Particulars',
                        # 'Qty', 'Amount', 'cgst_percentage', 'sgst_percentage',
                        # 'igst_percentage', 'cgst_amt', 'sgst_amt', 'igst_amt',
                        # 'SubTotalexclTax', 'DiscountAmount', 'DueAmount', 'TotalAmount',
                        # 'Remarks', 'IFSC', 'bank_account_no', 'bankname', 'branchname',
                        # 'billtoaddress', 'billtopin', 'shiptoaddress', 'seller_gstin',
                        # 'billTo_gstin', 'shipTo_gstin', 'statecode', 'customername',
                        # 'selleremailid', 'customeremailid', 'customermobileno', 'PAN',
                        # 'Signature', 'HSNSAC'])
                        
                        # for f in os.listdir(dirr):
                        #     d1=pd.read_csv(f'{dirr}/{f}')
                        #     sdf_format=sdf_format.append(d1,ignore_index=True)
                        #     with open(f"{dirr}/{f}","rb") as d:
                        #         addtoblob('sales-output-permanent',f,d)
                        #         d.close()

                        for f in os.listdir(dirr1):
                            d1=pd.read_csv(f'{dirr1}/{f}')
                            pdf_format=pdf_format.append(d1,ignore_index=True)
                            with open(f"{dirr1}/{f}","rb") as d:
                                addtoblob('purchase-output-permanent',f,d,cnstr=uploadabl)
                                d.close() 
                        path_D='ledger/ocr_data/'
                        # sdf_format.to_csv(path_D+'sales.csv')   
                        pdf_format.to_csv(path_D+'purchase1.csv')
                        # Test.main()   
                        print('done...........')
                        os.remove(f'{path1}/{bn}') 
                        print("deleted")
                        break
                    # break
                
                        
    else:print('nothing to show in blobfor invoice.....')  
