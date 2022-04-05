 
from genericpath import getmtime
from sys import stdin
import time
import os
 

def files(day):
     
    dirs_tocheck=['folder1', 'folder2']  
    daycount = time.time()-(float(day)*24*60*60)   

    for root, dirs, files in os.walk(os.getcwd()): 
        
        #check folders
        if os.path.basename(root) in dirs_tocheck:
            print(90*'_')
            print('Folder :'+ os.path.basename(root)+'\n')
            # check files
            for index,file in enumerate(files):
                # get details
                if os.path.getctime(root+'/'+ file) > daycount :
                    print(( str(index) + '-'+ '   '+time.ctime(os.path.getctime(root+'/'+ file)) +'     File Name :' +file +'\n'))
   

days_input = input("Inser duration in day : ")
files(days_input)



 