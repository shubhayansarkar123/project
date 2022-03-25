import pytesseract
import shutil
import os
import random
import re
import requests
import pandas as pd
import numpy as np
import pathlib
import Levenshtein as lev
from textextraction import *
# from imageocr import *
from collections import namedtuple
try:
    from PIL import Image
except ImportError:
    import Image


                
        
# def reex(text):
#     tds=0
#     dis=0
    
#     tot=0
#     du=0
#     sgs=0
#     igs=0
#     cgs=0
#     descript=''
#     Billno=''
#     Billdate=''
#     Duedate=''
#     Totalbillamount=''
#     Dueamount=''
#     Status=''
#     Sellername=''
#     Pan=''
#     Selleraddress=''
#     Selleremail=''
#     Sellerphno=''
#     Sellergstin=''
#     Buyergstin=''
#     Hsnsac=''
#     Items=''
#     Description=''
#     Billingmode=''
#     Duration=''
#     Itemqty=''
#     Itemprice=''
#     Subtotaltax=''
#     Taxamount=''#taxamount=cgst+sgst or igst
#     Taxpercentage=''
#     Taxdate=''
#     Taxtype=''
#     Taxtype=''
#     Sellerbankaccountno=''
#     Sellerifsccode=''
#     text=text.replace("|","")
#     text=text.replace("  "," ")
#     inv_re=re.findall(r'[a-z]+[-/]\d+[-/]\d+[-/]\d+|\d{9}',text,re.MULTILINE)
#     try:
#         try:
#             Billno=inv_re[0]
#         except:
#             Billno=inv_re[0]   
#     except:pass 
#     # dt=[]
#     # To find dates
#     # dates_re=re.findall(r'\d+[./-]\w+[./-]\d{4}', text)
#     match=re.findall(r'\d+[-/ ].[a-z,\d]+[-/ ]+20+\d{2}', text)
#     try:
#         try:
#             Billdate=match[0]
#             Duedate=match[1]
#         except:
#             Billdate=match[0]
#     except:
#         pass

#     #Particulars,isgt,amount
#     l=[]
#     Q=[]


#     #gstin permanent
#     g=[]

#     gstin = re.findall(r"\d{2}[a-z]{5}\d{4}[a-z]{1}\d{1}[z]{1}\w{1}", text)
#     gstin = [gst.upper() for gst in gstin]
#     for gt in gstin:
#         g.append(gt)
#     ggt=np.unique(g)

#     try:
#         try:
#             Sellergstin,Buyergstin=ggt[1],ggt[0]

#         except:
#             Sellergstin=ggt[1]
#     except: pass
#     # extract PAN from GSTIN
#     Pan = Sellergstin[2:13]
#     #ifsc permanent
#     ifsc = re.findall(r"[a-z]{4}[0]\w{6}",text)

#     for ia in ifsc:
#         ia=ia.upper()
#         # Retrieve Bank Info
#         url = f'https://ifsc.razorpay.com/{ia}'
#         bank_info=requests.get(url).json()
#         if bank_info=='Not Found':
#             continue
#         else:
#             # Filter-out necessary info
#             Sellerifsccode=ia
#             # BankName,BranchName=bank_info['BANK'],bank_info['BRANCH']
#     # REGEX for email
#     email = re.findall(r"\S+[@].+[. a-z,0-9]+.com", text)
#     try:
#         Selleremail=email[0]
#     except:pass
#     match=re.findall(r'\d{11,18}',text)
#     try:
#         st=" "
#         Sellerbankaccountno=st.join(match)
#     except:pass
    
#     #hsnsac
#     try:
#         hsc=[]
#         hscd=[]
#         hsd=pd.read_csv('hsd.csv',encoding='cp1252')
#         # try:
#         # text=text.spli('\n')
#         hscode=re.findall(r'\d{4,8}',text)
#         # print(hscode)



#             # print(hscode)
#         for hc in hscode:
#             Str1=str(hc)

#             for i,j in zip(hsd['hsnsac'],hsd['cols']):
#                 Str2=str(i)
#                 Ratio = lev.ratio(Str1,Str2)
#                 # print(Ratio,i,j)
#                 if Ratio==1:
#                     hsc.append(i)
#                     hscd.append(j)
#                     # print(Ratio,i)
#         Hsnsac=hsc
#         Description=hscd
#         print(Hsnsac,Description)
        
#     except:pass
#     df1=pd.read_csv('better_dataset.csv')
#     for t in text.split('\n'):
#         Str1=str(t)

#         ra=.5
#         for i in (df1['des_amt']):
#             Str2=str(i)

#             Ratio1 = lev.ratio(Str1,Str2)

#             if Ratio1>=ra:
#                 print("parti.........")
#                 print(Ratio1,t)
#                 if t==descript:
#                     pass
#                 else:
#                     descript=descript+" " +t
#                 # print(descript)
#     #amounts............
#     text1=text.replace(",",'')
#     text1=text.replace('inr','')
#     text2=text1.lstrip()

#     #print(text2)

#     #trailing zeroes : #splitted lines and ending only with trailing zeroes are considered as amt mi8 backfire
#     amt_re=re.compile(r'\.\d\d')
#     #amt_re=re.compile(r'\.\d\d$')   # $ ends in 0.00 hence some amount lines are not getting captured.
#     lines=text2.split("\n")
#     price=re.findall(r'[\d,]+\.\d{2}',text2)
#     Tds_re=re.findall(r"tds adjustment.*", text2)
#     dd=re.findall(r'due amount.*|amount due.*|total amount due.*|total due amount.*',text2)
#     total_re=re.findall(r'total invoice amount.*|invoice amount',text2)
#     pl=[]
#     npl=[]
#     for i in price:
#         s=i.replace(",","")
#         s=float(s)
#         pl.append(s)
#     nnp=np.unique(pl)
#     npl.append(nnp)
#     dis_re=re.findall(r'discount.*',text2)
#     for disc in dis_re:
#         for pr in pl:
#             if str(pr) in disc:
#     #             print(pr)
#                 if pr==max(pl):
#                     dis+=pr
#     #                 print(dis)
#                     pl.remove(pr)
                
#                 else:
#                     dis+=pr
#     #             print(dis)    
    
#     if dis!=0:
#         print('discunt...',dis)
#         for npr in npl[0]:
#     #         print(npr)
#             for tt in total_re:
#                 if str(npr) in tt:
#                     print(npr,tt)
#                     tot=npr
#                     break
                
#             for d in dd:
#                 if str(npr) in d:
#                     print(npr,d)
#                     du=npr
#                     break
                

                        

                                
#     else:
#         try:
#             tot=max(npl[0])
#         except:pass                        


#     for i in Tds_re:
#         for npr in npl[0]:
#             if str(npr) in i:
#                 tds=i                              

#     # print('total...',to)
#     # print('due...',du)
#     if du==0:
#         x=tot
#     else:x=du
#     # print(x)           
#     y=eval(input(print("Enter the % tax leveied:")))

                
#     taxable_Amt=x/(1+(y/100))
#     Value_of_goods=taxable_Amt+dis
#     total_tax=x-taxable_Amt

#     Subtotaltax=taxable_Amt+tds
#     Dueamount=du
#     Taxamount=total_tax
#     Taxpercentage=y
#     Totalbillamount=x
#     print(Value_of_goods,dis,x,y,tds,taxable_Amt,total_tax)
        
#     #finalcodetoappendanyforamtofpdforimageinvoice
#     line_items=[]
#     fields=('Billno','Billdate','Duedate','Totalbillamount','Dueamount','status','sellername','pan','selleraddress','sellerphonenumber','selleremailaddress','sellergstin','buyergstin','hsnsaccode','items','description','billingmode','duration','itemqty','itemprice','Subtotalexcltax','Taxamount','Taxpercentage','taxdate','taxtype','sellerbankaccountnumber','sellerifsccode','descript')
#     Inv1=namedtuple('Inv1',fields, defaults=(None,) * len(fields))
#     line_items.append(Inv1(Billno,Billdate,Duedate,Totalbillamount,Dueamount,Status,Sellername,Pan,Selleraddress,Sellerphno,Selleremail,Sellergstin,Buyergstin,Hsnsac,Items,Description,Billingmode,Duration,Itemqty,Itemprice,Subtotaltax,Taxamount,Taxpercentage,Taxdate,Taxtype,Sellerbankaccountno,Sellerifsccode,descript))
#     return(line_items)




def readex(text,sal=True):
    dis=0
    tot=0
    du=0
    tds=0
    gst_null=0
    SubT=0
    Title=''

    InvNo=''
    InvDate=''
    DueDate='' 
    Desc=''
    Qty=''
    Amount=''
    cgst_percentage=''
    sgst_percentage=''
    igst_percentage=''
    cgst_amt=''
    sgst_amt=''
    igst_amt=''
    SubTotalexclTax=''
    DiscountAmount=''
    DueAmount=''
    TotalAmount=''
    Remarks=''
    IFSC=''
    bank_account_no=''
    BankName=''
    BranchName=''
    billToAddress=''
    bill_to_pin=''
    shipToAddress=''
    ship_to_pin=''
    GSTINofCustomer=''
    statecode=''
    Vendor=''
    customername=''
    selleremailid=''
    customeremailid=''
    customermobileno=''
    pan=''
    sign=''
    hsnsac=''

    seller_gstin=''
    billTo_gstin=''
    shipTo_gstin=''

    # text = pytesseract.image_to_string(Image.open()).lower()
    text=text.replace("|","")
    text=text.replace("  "," ")
    # print(text)
    #finding specific features using re
    address_re=re.compile(r'Fuel Surcharge')
    shipment_re=re.compile(r'discount')
    hsn_re=re.compile(r'[hsn]+\s+\d{6}')
    hsn_no=re.compile(r'[hsn]?\s\d{6}')
    signed_re=re.compile(r'^signed: .*')

    #identify the invoice number :
    # inv_re=re.findall(r'[a-z/]+\d+[-/]+[\w]|\d{9}|[a-z]+/\d{2}-\d{2}/\d{3}', text)
    # # inv_re1=re.findall(r'[a-z/]+[\d/]+[-/\d]+[\w]+',text)
    # inv_re=re.findall(r'[a-z]+/[\w-]+/\d+|\w{10}|\d{13}|\d{9}',text)

    # print(inv_re)
    # InvNo=inv_re[0]

    # inv_re=re.findall(r'[a-z]+[-/]\d+[-/]\d+[-/]\d+|\d{9}',text)
    # try:
    #     InvNo=inv_re[0]
    # except:pass

    mn=[]
#[\w]+[-/]\d+[-/]\d+[-/]\d+|\w{2}\d{8}|\d{9}|d{10}|[a-z]+[\/-]+[\w\d]+[/\-]+[\d\w]+
    inv_re=re.findall(r'[\w]+[-/]\d+[-/]\d+[-/]\d+|\w{2}\d{8}|\d{9}|d{10}|[a-z]+[\/-]+[\w\d]+[/\-]+[\d\w]+',text)
    inv_no=re.findall(r'invoice no.*|invoice number.*|inv no.*|bill no.*|bill number.*',text)
    if len(inv_no)!=0:
        for i in range(len(inv_no)):
            i=inv_no[i]
    #         print(i)
            for ino in i.split(' '):
                for j  in inv_re:
        #             print(j)

                    if str(j) in str(ino):
        #                 print(i)

                        mn.append(ino)
                        
                        break

                    try:    
                        InvNo=mn[0]
                    except:pass
                    else:
                        try:
                            InvNo=inv_re[0]  
                        except:pass      
    else:
        try:
            InvNo=(inv_re[0])
        except:pass

    print(InvNo)
    print(inv_no,inv_re)
    match=re.findall(r'\d+[-/.].[a-z,\d]+[-/.]+20+\d{2}', text)
    try:
        try:
            InvDate=match[0]
            DueDate=match[1]
        except:
            InvDate=match[0]
    except:pass








    #signed permanent
    signed_re=re.compile(r"signed:\s+([a-z.]+)")
    for line in text.split('\n'):
        g=signed_re.search(line)
        if g:
            sign=g.group(1)

    #gstin permanent
    g=[]

    gstin = re.findall(r"\d{2}[a-z]{5}\d{4}[a-z]{1}\d{1}[z]{1}\w{1}", text)
    gstin = [gst.upper() for gst in gstin]
    for gt in gstin:
        g.append(gt)
    ggt=np.unique(g)

    try:
        # if sal:
        if len(ggt)==2:
            seller_gstin,billTo_gstin,shipTo_gstin=ggt[0],ggt[1],ggt[1]
        elif len(ggt)==1:
            seller_gstin=ggt[0]
        # else:
        #     if len(ggt)==2:
        #         seller_gstin,billTo_gstin,shipTo_gstin=ggt[1],ggt[0],ggt[0]
        #     elif len(ggt)==1:
        #         seller_gstin=ggt[1]

    except: pass

    #pan permanent
    # extract PAN from GSTIN
    pan = seller_gstin[2:13]

    #statecode permamnent
    statecode=seller_gstin[0:2]

    #bill ship pin
    # try:
    #     bill_to_pin=seller_gstin[0:2]
    #     ship_to_pin=billTo_gstin[0:2]
    # except:pass

    #ifsc permanent
    ifsc = re.findall(r"[a-z]{4}[0][a-z0-9]{6}",text)
    
    # print(text)

    for ia in ifsc:
        ia=ia.upper()
        # Retrieve Bank Info
        url = f'https://ifsc.razorpay.com/{ia}'
        bank_info=requests.get(url).json()
        if bank_info=='Not Found':
            continue
        else:
            # Filter-out necessary info
            IFSC=ia
            BankName,BranchName=bank_info['BANK'],bank_info['BRANCH']


        
    email = re.findall(r"\S+[@].+[. a-z,0-9]+.com", text)
    try:
        try:
            selleremailid,customeremailid=email[0],email[1]
        except:
            selleremailid=email[0]
    except:pass
    # match=re.findall(r'\d{11,18}',text)
    # st=" "
    # bank_account_no=st.join(match)
    #acc no
    atch=re.findall(r'account number.*|account.*|act no.*|ack no.*|account no.*',text)
    acno=re.findall(r'\d{11,18}',text)
    for i in atch:
        for j in acno:
            if j in i:
                bank_account_no=j
                # print(bank_account_no)

    #hsnsac
    # try:
    # hsnsac=''
    print('1')
    hsc=[]
    hscd=[]
    hsd=pd.read_csv(r'hsd.csv',encoding='cp1252')
    try:
        print('2')
        hscod=re.findall(r'hsn.*|sac.*|hsn code.*|sac code.*',text)
        hscodes=re.findall(r'\d{4,8}',text)
    #     print(hscod,hscodes)
        for i in hscod:
            for j in hscodes:
                if j in i:
                    Str1=str(j)
                    for cd,de in zip(hsd['hsnsac'],hsd['cols']):
                        Str2=str(cd)
                        if Str1==Str2:

                            hsc.append(cd)
                            hscd.append(de)
                            # print(Ratio,i)
        hsnsac=hsc
        Desc=hscd
    #     print(hsnsac)
        if not hsnsac:

    #     except:
            print('3')
            amt_re=re.compile(r'\.\d\d$')
            l=[]
            for line in text.split('\n'):
            #     print(line)
                if amt_re.search(line):
            #         print(line)
                    hscodes=re.findall(r'\d{4,8}',line)
            #         print(hscode)
                    l.append(hscodes)
            hscode=[]
            for lis in l:
                for code in lis:
                    hscode.append(code)





            for hc in hscode:
                Str1=str(hc)

                for i,j in zip(hsd['hsnsac'],hsd['cols']):
                    Str2=str(i)
                    Ratio = lev.ratio(Str1,Str2)
                    # print(Ratio,i,j)
                    if Ratio==1:
                        hsc.append(i)
                        hscd.append(j)
                        print(Ratio,i)
            hsnsac=hsc
            Desc=hscd


    except:
        pass
        
#amounts............
    text1=text.replace(",",'')
    text1=text.replace('inr','')
    text2=text1.lstrip()

    #print(text2)

    #trailing zeroes : #splitted lines and ending only with trailing zeroes are considered as amt mi8 backfire
    amt_re=re.compile(r'\.\d\d')
    #amt_re=re.compile(r'\.\d\d$')   # $ ends in 0.00 hence some amount lines are not getting captured.
    lines=text2.split("\n")
    price=re.findall(r'[\d,]+\.\d{2}|[\d,]+\d',text2)
    Tds_re=re.findall(r"tds adjustment.*", text2)
    dd=re.findall(r'due amount.*|amount due.*|total amount due.*|total due amount.*',text2)
    total_re=re.findall(r'total invoice amount.*|invoice amount',text2)
    pl=[]
    npl=[]
    filtered=[]
    for i in price:
        if ","in i or "." in i:
            filtered.append(i)
    for pr in filtered:
        s=pr.replace(",","")
        s=float(s)
        pl.append(s)
    nnp=np.unique(pl)
    npl.append(nnp)
    dis_re=re.findall(r'discount.*',text2)
    for disc in dis_re:
        for pr in pl:
            if str(pr) in disc:
    #             print(pr)
                if pr==max(pl):
                    dis+=pr
    #                 print(dis)
                    pl.remove(pr)
                
                else:
                    dis+=pr
    #             print(dis)    
    
    if dis!=0:
        DiscountAmount=dis
        print('discunt...',dis)
        for npr in npl[0]:
    #         print(npr)
            for tt in total_re:
                if str(npr) in tt:
                    print(npr,tt)
                    tot=npr
                    break
                
            for d in dd:
                if str(npr) in d:
                    print(npr,d)
                    du=npr
                    break
                

                        

                                
    else:
        DiscountAmount=dis
        try:
            tot=max(npl[0])
        except:pass                        


    for i in Tds_re:
        for npr in npl[0]:
            if str(npr) in i:
                tds=float(npr)                              

    # print('total...',to)
    # print('due...',du)
    if du==0:
        x=tot
    else:x=du
    # print(x) 
      
    # y=eval(input(print("Enter the % tax leveied:")))
    y=18
 
                
    taxable_Amt=(x/(1+(y/100))) 
    
    Value_of_goods=taxable_Amt+dis
    total_tax=x-taxable_Amt
    # total_tax=round(total_tax,4)
    # taxable_Amt=round(taxable_Amt,2)
    SubTotalexclTax=taxable_Amt+tds
    DueAmount=du

    TotalAmount=x
    #gst  amt mapping
    try:
        if seller_gstin[0:2]==billTo_gstin[0:2]:
            cgst_amt,sgst_amt=total_tax/2,total_tax/2
            igst_amt=gst_null
        else:
            igst_amt=total_tax
            cgst_amt,sgst_amt=gst_null,gst_null
    except:pass  
    #gst  % mapping
    try:
        if seller_gstin[0:2]==billTo_gstin[0:2]:
            cgst_percentage,sgst_percentage=y/2,y/2
            igst_percentage=gst_null
        else:
            igst_percentage=y
            cgst_percentage,sgst_percentage=gst_null,gst_null
    except:pass 
    # print(Value_of_goods,dis,x,y,tds,taxable_Amt,total_tax)
    cgst_amt=round(cgst_amt,2)
    igst_amt=round(igst_amt,2)
    sgst_amt=round(sgst_amt,2)
    
    SubTotalexclTax=round(SubTotalexclTax,2)
    print(cgst_amt,igst_amt,sgst_amt,SubTotalexclTax)
    # print(type(Desc))
    #title
    title=re.findall(r'tax invoice|reimbursement invoice|freight/tax invoice|export invoice|cash memo',text)
    try:
        Title=title[0]
    except:pass
    #finalcodetoappendanyforamtofpdforimageinvoice
    line_items=[]
    fields=('Title','InvNo','InvDate','DueDate','Particulars','Qty','Amount','cgst_percentage','sgst_percentage','igst_percentage','cgst_amt','sgst_amt','igst_amt','SubTotalexclTax','DiscountAmount','DueAmount','TotalAmount','Remarks','IFSC','bank_account_no','bankname','branchname','billtoaddress','billtopin','ship_to_pin','shiptoaddress','seller_gstin','billTo_gstin','shipTo_gstin','statecode','customername','selleremailid','customeremailid','customermobileno','PAN','Signature','HSNSAC')
    Inv=namedtuple('Inv',fields, defaults=(None,) * len(fields))
    line_items.append(Inv(Title,InvNo,InvDate,DueDate,Desc,Qty,Amount,cgst_percentage,sgst_percentage,igst_percentage,cgst_amt,sgst_amt,igst_amt,SubTotalexclTax,DiscountAmount,DueAmount,TotalAmount,Remarks,IFSC,bank_account_no,BankName,BranchName,billToAddress,bill_to_pin,ship_to_pin,shipToAddress,seller_gstin,billTo_gstin,shipTo_gstin,statecode,customername,selleremailid,customeremailid,customermobileno,pan,sign,hsnsac))
    return(line_items)

