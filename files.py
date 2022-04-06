 
from genericpath import getmtime
import time
import os
 

class colors: # You may need to change color settings
 
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

    # Underline
    UBlack="\033[4;30m"       # Black
    URed="\033[4;31m"         # Red
    UGreen="\033[4;32m"       # Green
    UYellow="\033[4;33m"      # Yellow
    UBlue="\033[4;34m"        # Blue
    UPurple="\033[4;35m"      # Purple
    UCyan="\033[4;36m"        # Cyan
    UWhite="\033[4;37m"       # White

    # Background
    On_Black="\033[40m"       # Black
    On_Red="\033[41m"         # Red
    On_Green="\033[42m"       # Green
    On_Yellow="\033[43m"      # Yellow
    On_Blue="\033[44m"        # Blue
    On_Purple="\[\033[45m"      # Purple
    On_Cyan="\033[46m"        # Cyan
    On_White="\033[47m"       # White

    # High Intensty
    IBlack="\033[0;90m"       # Black
    IRed="\033[0;91m"         # Red
    IGreen="\033[0;92m"       # Green
    IYellow="\033[0;93m"      # Yellow
    IBlue="\033[0;94m"        # Blue
    IPurple="\033[0;95m"      # Purple
    ICyan="\033[0;96m"        # Cyan
    IWhite="\033[0;97m"       # White

    # Bold High Intensty
    BIBlack="\033[1;90m"      # Black
    BIRed="\033[1;91m"        # Red
    BIGreen="\033[1;92m"      # Green
    BIYellow="\033[1;93m"     # Yellow
    BIBlue="\033[1;94m"       # Blue
    BIPurple="\033[1;95m"     # Purple
    BICyan="\033[1;96m"       # Cyan
    BIWhite="\033[1;97m"      # White

    # High Intensty backgrounds
    On_IBlack="\033[0;100m"   # Black
    On_IRed="\033[0;101m"     # Red
    On_IGreen="\033[0;102m"   # Green
    On_IYellow="\033[0;103m"  # Yellow
    On_IBlue="\033[0;104m"    # Blue
    On_IPurple="\033[10;95m"  # Purple
    On_ICyan="\033[0;106m"    # Cyan
    On_IWhite="\033[0;107m"   # White

 

def files(day):
    
#     os.chdir('/home/usr')
    dirs_tocheck=['folder3', 'folder1', 'folder2']
     
 
    daycount = time.time()-(int(day)*24*60*60)
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
                    status_backup_pre = status_backup if file_count !=0 else status_backup_pre

                    brief_report_dic['ne-type']   = os.path.basename(root).upper()
                    brief_report_dic['file-count']=  str(file_count)
                    brief_report_dic['status']    =  status_backup_pre

            print('\n')
            print( colors.Red +'  NE Type     :  '+ colors.off+ colors.BIRed + os.path.basename(root).upper()+ colors.off)
            print( colors.Red +'  File Counts :  '+ colors.off+ colors.BIRed + str(file_count) + colors.off )
            print( colors.Red +'  Status      :  '+ colors.off+ colors.BIRed +  str( status_backup_pre ) + colors.off +' '+ colors.On_Blue + str('LAST UPDATE ' if file_count==0 else '') + colors.off +'\n')    

            # add to list
            brief_report_list.append(brief_report_dic) 
        

 

    

    print(60*':')
    print('\n')

    print(' '+colors.On_Blue + str(20*' ') + colors.off +  colors.BBlue + ' Brif Report '+ colors.off + colors.On_Blue+ 20*' '+colors.off )
    print('\n')    
    for bReport in  brief_report_list:
        if len(bReport) !=0 :
            print( colors.Red +  '    NE Type       :  ' + bReport['ne-type'] +colors.off )         
            print( colors.Green +'    File Counts   :  ' + bReport['file-count'] + colors.off)         
            print( colors.Blue + '    Status        :  ' + bReport['status'] + colors.off )
            print('    '  +colors.Blue+ 45*'_' + colors.off+'\n')
    

 
    print('\n'+15*':'+ colors.Yellow + 'DONE FOR LAST' +colors.off +colors.BYellow +' '+str(day)+' '+ colors.off + colors.Yellow+ 'DAYS !' + colors.off  + 15*':'+'\n')


days_input = input("Insert Day   : ")
files(7 if days_input=='' else days_input)
