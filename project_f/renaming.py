
''' 
Change the filename of the input files
to an uniform format
'''
#%% packages

import os
import numpy
import datetime
import shutil
import hashlib
from  validation import *


directory1="mixed_files" 

#%% apply `change_filename()`
#   on all files in a directory
class renamed_files:

    def convert_filename(directory,file):
        

        
    
        
        # STEP 1: Check if `directory` exists
        if not os.path.exists(directory):
            print("STATUS: [ERROR] Specified directory does not exist")
        else:
            print("STATUS: [SUCCESS] (STEP 1) Speciifed directory exists...continuing...")
        # STEP 2: Check if `renamed directory` exists
        if not os.path.exists(directory1):
            print("STATUS: [ERROR] Specified directory does not exist...making it...")
            os.mkdir(directory1)
        else:
            print("STATUS: [SUCCESS] (STEP 2) Speciifed directory exists....continuing...")
        text = str(datetime.datetime.now())
        uid = hashlib.md5(text.encode()).hexdigest()
        # step 3: making a new directory to save the renamed files
        dir3=f'{directory}_{uid}'
        directory2=f'{directory1}/{dir3}'
        print(directory2)
        os.mkdir(directory2) 
        
        
            
        # STEP 4: Obtain file list
        file_list = []
        # for filename in os.listdir(directory):
        file_list.append(file)
        print(f"STATUS: [SUCCESS] (STEP 3) File List = {len(file_list)} items")

    
        
        # STEP 5: Iterate over file_list
        for file in file_list:
            
            # STEP 6: Generate Unique ID
            # UID = TimeStamp + Random component
            text = str(datetime.datetime.now())                 # timestamp
            text += str(numpy.random.standard_cauchy(size = 1)) # Random part
            uid = hashlib.md5(text.encode()).hexdigest()
            
            # STEP 7: Change filename
            
            old_file_name = f"{directory}/{os.path.basename(file)}"
            # new_file_name = f"{directory1}/{uid + os.path.splitext(file)[1]}"
            new_file_name=f"{directory2}/{uid[:20]}_{os.path.basename(file)}"
            # {uid[:20]}_
            shutil.copy(src = old_file_name, dst = new_file_name)

            print(f"STATUS: [RENAME] {old_file_name} --> {new_file_name}")
            
        

        valid=validation.classifier(dir3)


        return valid




# convert_filename('t1')

