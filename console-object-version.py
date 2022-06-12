# this will return result in object: [{},{},.. ]
 
from genericpath import getmtime
import time
import os
 
dirs_tocheck={
     'folder1'  :'Folder1 Name',
     'folder2'  :'Folder2 Name',
     'env'  :'env',
}

def files(day=7):

    try:
        os.chdir('/home/folder/subfolder')
         
        daycount = time.time()-(float(day)*24*60*60)
        #start checking
        result=[]
        for root, dirs, files in os.walk(os.getcwd()):
            #check folders
            if os.path.basename(root) in dirs_tocheck:
                backupsInFolders={}
                filesInDirs=[]
                for index,file in enumerate(files):
                    status_backup_pre = time.ctime(os.path.getctime(root+'/'+ file))  
                    # get file details
                    file_count=0
                    if (os.path.getctime(root+'/'+ file)) > daycount :
                        file_count=file_count+1
                        status_backup= time.ctime(os.path.getctime(root+'/'+ file))
                        filesInDirs.append({file:status_backup})

                    backupsInFolders['ne-type']   = os.path.basename(root)
                    backupsInFolders['status']    =  status_backup if file_count !=0 else status_backup_pre
                    backupsInFolders['files']     =  filesInDirs
                
                result.append(backupsInFolders)  
                
        print(result)
    except Exception as err:
        print(err)

files()
