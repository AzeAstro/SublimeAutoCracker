#Sublime Autocracker 

#Made by AzeAstro

#Imports...
import os
import subprocess
import requests
import shutil
import time
import pathlib

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


license=('''
----- BEGIN LICENSE ----- 
TwitterInc 
200 User License 
EA7E-890007 
1D77F72E 390CDD93 4DCBA022 FAF60790 
61AA12C0 A37081C5 D0316412 4584D136 
94D7F7D4 95BC8C1C 527DA828 560BB037 
D1EDDD8C AE7B379F 50C9D69D B35179EF 
2FE898C4 8E4277A8 555CE714 E1FB0E43 
D5D52613 C3D12E98 BC49967F 7652EED2 
9D2D2E61 67610860 6D338B72 5CF95C69 
E36B85CC 84991F19 7575D828 470A92AB 
------ END LICENSE ------
''')

print(logo)

class Tasks:
    def __init__(self):
        pass

    def connectionChecker(self):
        popen=subprocess.Popen(["ping","www.sublimetext.com","-c","3"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result=popen.communicate()
        if result[1]==b"":
            return True
        else:
            print("Check your connection first...")
            return False
    
    def downloader(self,result):
        if result==True:
            while True:
                architecture=input("Please,enter architecture:\nx64 or x86?\n>>>")
                if architecture.lower() in ["x64","x86"]:
                    break
            if architecture.lower()=="x64":
                url="https://download.sublimetext.com/sublime_text_3_build_3211_x64.tar.bz2"
            else:
                url="https://download.sublimetext.com/sublime_text_3_build_3211_x32.tar.bz2"
            
            print("Downloading binaries,please wait....")
            binaries=requests.get(url=url)
            print("Download ended")
            global FILENAME
            FILENAME=f"Sublime_Text_3_{architecture}.tar.bz2"
            open(FILENAME,"wb").write(binaries.content)
            popen=subprocess.Popen(["tar","xjf",FILENAME],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            result=popen.communicate()
            if result[1]==b"":
                print("Starting pathcer...")
                self.patcher(self)
            else:
                if "command not found" in result[1].decode("utf-8"):
                    os.system("sudo apt install tar")
                else:
                    print(f"[Error] {result[1].decode('utf-8')}\nIf you couldn't fix error,please,report it to us.")

    def patcher(self):
        os.rename(r"./sublime_text_3/sublime_text",r"./sublime_text_3/sublime_text_old")
        with open("./sublime_text_3/sublime_text_old","rb") as f:
            bytes_in_file=f.read()
            hex_=bytes.hex(bytes_in_file)

        with open("./sublime_text_3/sublime_text","wb") as f:
            replaced=hex_.replace("97940d","000000")
            f.write(bytes.fromhex(replaced))
        print("Pathcing done!")
        self.finalizer(self)


#sudo ln -s /opt/Sublime\ Text\ 2/sublime_text /usr/bin/sublime

    def finalizer(self):
        print("Finalizing...")

        #Copying files to /opt folder and setting perms to 777 :]
        try:
            shutil.copytree(f"{pathlib.Path(__file__).parent.resolve()}/sublime_text_3","/opt/sublime_text")
            os.system("chmod -R 777 /opt/sublime_text")
        except FileExistsError:
            try:
                shutil.move(r"/opt/sublime_text",r"/opt/sublime_text_old")
            except PermissionError:
                print("Permission denied while renaming existing sublime_text folder to sublime_text_old.")
            except FileExistsError:
                shutil.move(f"/opt/sublime_text",f"/opt/sublime_text_old_{round(time.time())}")
                shutil.copytree(f"{pathlib.Path(__file__).parent.resolve()}/sublime_text_3","/opt/sublime_text")
            except shutil.Error:
                shutil.move(f"/opt/sublime_text",f"/opt/sublime_text_old_{round(time.time())}")
                shutil.copytree(f"{pathlib.Path(__file__).parent.resolve()}/sublime_text_3","/opt/sublime_text")                    
            except Exception as e:
                print(f"Unknow error during renaming existing sublime_text folder to sublime_text_old: {e}\nPlease,report it in github.")




        #.desktop file
        try:
            shutil.copy(f"{pathlib.Path(__file__).parent.resolve()}/sublime_text_3/sublime_text.desktop","/usr/share/applications/")
        except PermissionError:
            print("Permission denied while copying sublime_text_3 folder to /opt.")
        except Exception as e:
            print(f"Unknown error during copying to /opt folder: {e}\nPlease,report it in github.")        
        except PermissionError:
            print("Permission denied while copying .desktop file to /usr/share/applications.")
        except Exception as e:
            print(f"Unknown error during copying to /usr/share/applications folder: {e}\nPlease,report it in github.")
        os.remove(FILENAME)
        shutil.rmtree("./sublime_text_3")


        symlink_popen=subprocess.Popen(["sudo","ln","-s","/opt/sublime_text/sublime_text","/usr/local/bin/subl"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        symlink_results=symlink_popen.communicate()

        if symlink_results[1]==b"":
            pass
        else:
            if "File exists" in symlink_results[1].decode("utf-8"):
                os.system("sudo rm /usr/local/bin/subl")
                os.system("sudo ln -s /opt/sublime_text/sublime_text /usr/local/bin/subl")
            else:
                print(f"Unknown error occured during creating symlink: {symlink_results[1].decode('utf-8')}\nPlease,report it in Github.")
        os.system("sudo chmod 777 /usr/local/bin/subl")

        print("Program ended.")
        print(f"When you open program,go to Help->Enter License and then paste this license text there:\n{license}")

        print("Restart your computer if you don't see Sublime in applications menu.")
if __name__=="__main__":
    result=Tasks.connectionChecker(Tasks)
    Tasks.downloader(Tasks,result)