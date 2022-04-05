 
from genericpath import getmtime
from sys import stdin
import time
import os
 
def files(day):
    
    os.chdir('/mnt/shareddisk/sftp/data/nokia')
    dirs_tocheck=['bc', 'folder2']
 
  
    daycount = time.time()-(float(day)*24*60*60)    

    for root, dirs, files in os.walk(os.getcwd()):  
        
        #check folders
        if os.path.basename(root) in dirs_tocheck:
            print(80*'_'+'\n')
            print(30*':'+'  NE TYPE is  '+ (os.path.basename(root).upper())+'  '+30*':'+'\n')
            # check files
            for index,file in enumerate(files):
                # get details
               
                if os.path.getctime(root+'/'+ file) > daycount :
                     
                    print(( ' -' +'Number of files: ' + file  + '     - Last Received date: '+ time.ctime(os.path.getctime(root+'/'+ file)) ))
    print(25*':'+ 'CHECKING IS DONE FOR LAST {}  DAY(S) !'.format(day) +25*':')    
 
days_input = input("Inser duration in day, hit ENTER for 7 DAYS : ")
files(7 if days_input=='' else days_input)