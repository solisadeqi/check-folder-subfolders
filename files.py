  
from genericpath import getmtime
import time
import os
 

class colors: 
 
    # Reset
    off="\033[0m"       # Text Reset

    # Regular Colors
    Black="\033[0;30m"        # Black
    Red="\033[0;31m"          # Red
    Green="\033[0;32m"        # Green
    Yellow="\033[0;33m"       # Yellow
    Blue="\033[0;34m"         # Blue
    Purple="\033[0;35m"       # Purple
    Cyan="\033[0;36m"         # Cyan
    White="\033[0;37m"        # White

    # Bold
    BBlack="\033[1;30m"       # Black
    BRed="\033[1;31m"         # Red
    BGreen="\033[1;32m"       # Green
    BYellow="\033[1;33m"      # Yellow
    BBlue="\033[1;34m"        # Blue
    BPurple="\033[1;35m"      # Purple
    BCyan="\033[1;36m"        # Cyan
    BWhite="\033[1;37m"       # White

 
    # Background
    On_Black="\033[40m"       # Black
    On_Red="\033[41m"         # Red
    On_Green="\033[42m"       # Green
    On_Yellow="\033[43m"      # Yellow
    On_Blue="\033[44m"        # Blue
    On_Purple="\[\033[45m"      # Purple
    On_Cyan="\033[46m"        # Cyan

    # High Intensty
    IBlack="\033[0;90m"       # Black
    IRed="\033[0;91m"         # Red
    IGreen="\033[0;92m"       # Green
    IYellow="\033[0;93m"      # Yellow
    IBlue="\033[0;94m"        # Blue
    IPurple="\033[0;95m"      # Purple
    ICyan="\033[0;96m"        # Cyan

    # Bold High Intensty
    BIBlack="\033[1;90m"      # Black
    BIRed="\033[1;91m"        # Red
    BIGreen="\033[1;92m"      # Green
    BIYellow="\033[1;93m"     # Yellow
    BIBlue="\033[1;94m"       # Blue
    BIPurple="\033[1;95m"     # Purple
    BICyan="\033[1;96m"       # Cyan

    # High Intensty backgrounds
    On_IBlack="\033[0;100m"   # Black
    On_IRed="\033[0;101m"     # Red
    On_IGreen="\033[0;102m"   # Green
    On_IYellow="\033[0;103m"  # Yellow
    On_IBlue="\033[0;104m"    # Blue
    On_IPurple="\033[10;95m"  # Purple
    On_ICyan="\033[0;106m"    # Cyan


dirs_tocheck={
    
    'folder1'  :'Folder1 Name',
    'folder2'  :'Folder2 Name',
    'folder3'  :'Folder3 Name',
}


def files(day):
    print(day)
    try:
        # os.chdir('/mnt/shareddisk/sftp/data/nokia')
         
        daycount = time.time()-(float(day)*24*60*60)
        #start checking
        brief_report_list =[]
        for root, dirs, files in os.walk(os.getcwd()):
            #check folders
            if os.path.basename(root) in dirs_tocheck:
                print(60*':'+'\n')
                brief_report_dic={}
            
                # check files
                file_count =0
                for index,file in enumerate(files):
                    status_backup_pre = time.ctime(os.path.getctime(root+'/'+ file))  
                    # get file details
                    if (os.path.getctime(root+'/'+ file)) > daycount :
                        file_count=file_count+1
                        status_backup= time.ctime(os.path.getctime(root+'/'+ file))
                        
                        print(( colors.Blue +' File Name: ' + colors.off + colors.BGreen +file  + colors.off+ '      '+ colors.Purple +'Last Received date: '+ colors.off+ colors.BCyan+ time.ctime(os.path.getctime(root+'/'+ file)) +colors.off ))
                        # status of backup
                          
                    brief_report_dic['ne-type']   = os.path.basename(root)
                    brief_report_dic['file-count']=  str(file_count)
                    brief_report_dic['status']    =  status_backup if file_count !=0 else status_backup_pre
                brief_report_list.append(brief_report_dic)

                print('\n')
                print( colors.Red +'  NE Type-     :  '+ colors.off+ colors.BIRed + dirs_tocheck[os.path.basename(root)] + colors.off)
                print( colors.Red +'  File Counts- :  '+ colors.off+ colors.BIRed + str(file_count) + colors.off )
                print( colors.Red +'  Status-      :  '+ colors.off+ colors.BIRed +  str( status_backup_pre ) + colors.off +' '+ colors.On_Blue + str('LAST UPDATE ' if file_count==0 else '') + colors.off +'\n')    
                
                # print( brief_report_dic )
                # print( brief_report_list )
                # add to list
                 
            

        # brief report
        print(60*':')
        print('\n')

        print(' '+colors.On_Blue + str(20*' ') + colors.off +  colors.BBlue + ' Brief Report '+ colors.off + colors.On_Blue+ 20*' '+ colors.off )
        print('\n')    
        for bReport in  brief_report_list:
            # print(brief_report_list)
            # print(brief_report_dic)
            if len(bReport) !=0 :
                # print( colors.Red +  '    NE Type       :  ' + bReport['ne-type'] +colors.off )         
                print( colors.IRed +  '    NE Type       :  ' + dirs_tocheck[bReport['ne-type']] +colors.off )         
                print( colors.IGreen +'    File Counts   :  ' + bReport['file-count'] + colors.off)         
                print( colors.IBlue + '    Status        :  ' + bReport['status'] + colors.off )
                print('    '  +colors.Blue+ 45*'_' + colors.off+'\n')
        
        print('\n'+15*':'+ colors.Yellow + 'DONE FOR LAST' +colors.off +colors.BYellow +' '+str(day)+' '+ colors.off + colors.Yellow+ 'DAYS !' + colors.off  + 15*':'+'\n')
    except KeyboardInterrupt:
        print(  '\n    '+ colors.On_IGreen+ "   hmmm! It seems something's wrong, You may try agin! " + colors.off)



run_files=True
while True:
    try:
        days_input=input("Insert Day or Hit ENTER for 7 Days  : ")
        day=7 if days_input=='' else days_input
        if float( day ) > 0:
            break #ok
        else:
            print('    '+colors.BRed+ "    Day must be positive, more than ZERO. " + colors.off)
    except ValueError:
        print( '    '+ colors.BRed+ "    Insert Day in NUMERIC NUMBER, Please. like: 2, 0.2 " + colors.off)
    except KeyboardInterrupt:
        print(  '\n    '+ colors.On_IGreen+ "    See you later ! " + colors.off)
        run_files =False
        break
     

# if ctl+c in while loop happen, function will not run
if (run_files) : files(day)
    
 
