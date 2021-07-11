#Sublime Autocracker 

#Made by AzeAstro

#Imports...
import os
import subprocess
import requests
import shutil
import time
import ctypes

logo='''
 ____        _     _ _                
/ ___| _   _| |__ | (_)_ __ ___   ___ 
\___ \| | | | '_ \| | | '_ ` _ \ / _ \\
 ___) | |_| | |_) | | | | | | | |  __/
|____/ \__,_|_.__/|_|_|_| |_| |_|\___|
                                      
    _         _         ____                _             
   / \  _   _| |_ ___  / ___|_ __ __ _  ___| | _____ _ __ 
  / _ \| | | | __/ _ \| |   | '__/ _` |/ __| |/ / _ \ '__|
 / ___ \ |_| | || (_) | |___| | | (_| | (__|   <  __/ |   
/_/   \_\__,_|\__\___/ \____|_|  \__,_|\___|_|\_\___|_|   

'''

print(logo)

class Tasks:
    def __init__(self):
        pass

    def connectionChecker(self):
        popen=subprocess.Popen(["ping","/n","3","www.sublimetext.com"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result=popen.communicate()
        if result[1]==b"":
            return True
        else:
            print("Check your connection first...")
            return False

    def downloader(self,result):
        if result==True:
            while True:
                global ARCHITECTURE
                ARCHITECTURE=input("Please,enter architecture:\nx64 or x86?\nNote: You will install this software so,select your own architecture\n>>>")
                if ARCHITECTURE.lower() in ["x64","x86"]:
                    break
            if ARCHITECTURE.lower()=="x64":
                url="https://download.sublimetext.com/Sublime Text Build 3211 x64 Setup.exe"
            else:
                url="https://download.sublimetext.com/Sublime Text Build 3211 Setup.exe"

            print("Downloading files.....")
            setup_bin=requests.get(url=url)
            print("Download ended.")
            global FILENAME
            FILENAME="Sublime_setup.exe"
            open(FILENAME,"wb").write(setup_bin.content)
            print("Installing...")
            os.system(f"{FILENAME} /VERYSILENT /NORESTART")
            #25 seconds sleep for letting installer to end installation.
            time.sleep(25)
            print("Installation ended.")


    def pathcer(self):
        print("Starting to patch...")
        if ARCHITECTURE.lower()=="x64":
            f=open("C:\Program Files\Sublime Text 3\sublime_text.exe","rb")
            bytes_=f.read()
            f.close()
            

            #archiving old exe
            shutil.move("C:\Program Files\Sublime Text 3\sublime_text.exe","C:\Program Files\Sublime Text 3\sublime_text_old.exe")


            #Epic thanks to one guy from Python Discord due this code.
            #If he sees it,I am the guy who spent 17 hours due one letter. :D
            def bytes_replace(bstr, offset, b):
                return bstr[:offset] + b + bstr[offset+1:]

            #Replacements
            bytes_ = bytes_replace(bytes_, 0x8545, b"\x85")
            bytes_ = bytes_replace(bytes_, 0x08FF19, b'\xeb')
            bytes_ = bytes_replace(bytes_, 0x1932C7, b't')

            f=open("C:\Program Files\Sublime Text 3\sublime_text.exe","wb")
            f.write(bytes_)
            f.close()
            print("Patch ended.\nHappy coding! :D")
        else:
            f=open("C:\Program Files (x86)\Sublime Text 3\sublime_text.exe","rb")
            bytes_=f.read()
            f.close()
            

            #archiving old exe
            shutil.move("C:\Program Files (x86)\Sublime Text 3\sublime_text.exe","C:\Program Files (x86)\Sublime Text 3\sublime_text_old.exe")


            #Epic thanks to one guy from Python Discord due this code.
            #If he sees it,I am the guy who spent 17 hours due one letter. :D
            def bytes_replace(bstr, offset, b):
                return bstr[:offset] + b + bstr[offset+1:]

            #Replacements
            bytes_ = bytes_replace(bytes_, 0x8545, b"\x85")
            bytes_ = bytes_replace(bytes_, 0x08FF19, b'\xeb')
            bytes_ = bytes_replace(bytes_, 0x1932C7, b't')

            f=open("C:\Program Files (x86)\Sublime Text 3\sublime_text.exe","wb")
            f.write(bytes_)
            f.close()
            print("Patch ended.\nHappy coding! :D")            


if __name__=="__main__":
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin == True:
        result=Tasks.connectionChecker(Tasks)
        Tasks.downloader(Tasks,result)
    else:
        print("Script requires to run as administration due installation process. Such as installing sublime text 3 and editing files and etc.")