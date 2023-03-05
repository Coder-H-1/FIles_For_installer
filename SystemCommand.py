from Modules import *
from CodedPaths import *

def System(command=None):
    """From class SystemCommand || Runs command that could affect windows"""
    command= str(command)
    if 'open settings' in command: 
        press_and_release("win + i")
        speak("Opened System Settings")
    
    elif 'lock computer' in command or 'lock the computer' in command or 'lock my pc' in command or 'lock the pc' in command: 
        press_and_release("win + l")
    
    elif 'open run prompt' in command: 
        press_and_release("win + r")

    elif 'open search' in command: 
        press_and_release("win + s")

    elif 'refresh the computer' in command or 'refresh computer' in command or'refresh pc' in command or 'refresh the pc' in command: 
        press_and_release("f5")
    
    elif 'open display settings' in command:
        if int(platform.release()) <= 10: 
            speak("Sir, You are on windows version lower than windows 10 so its ease of access at that time, ?Operation aborted?")
        elif int(platform.release()) >= 10:
            press_and_release("win + u")

    elif 'restart the pc' in command or 'restart pc' in command or 'restart computer' in command or 'restart the computer' in command: 
        speak("Restarting the Computer")
        press_and_release("win + d")
        time.sleep(0.3)
        press_and_release("alt + f4")
        time.sleep(0.3)
        press_and_release("down")
        time.sleep(0.2)
        press_and_release("enter")
        
    elif 'shutdown computer' in command or 'shutdown pc' in command or 'shutdown my pc' in command or 'shutdown the computer' in command: 
        speak("Shutting down the computer")
        press_and_release("win+d")
        time.sleep(0.3)
        press_and_release("alt+f4")
        time.sleep(0.3)
        press_and_release("enter")
    
    elif 'computer to sleep' in command or 'pc to sleep' in command or 'put the computer to sleep' in command: 
        speak("Putting Computer to sleep")
        press_and_release("win + d")
        time.sleep(0.3)
        press_and_release("alt + f4")
        time.sleep(0.3)
        press_and_release("up")
        time.sleep(0.2)
        press_and_release("enter")

    else: 
        pass

def Sys(command):
    """From class SystemCommand || Opens|Close programs | if not found passes query to System Command"""
    
    command = str(command)
    command = command.lower()
    if 'open task manager' in command: 
        os.startfile(taskmanager)
        speak("Opened Task manager")

    elif 'close task manager' in command: 
        os.system("taskkill /f /im taskmgr.exe")
        speak("Closed Task Manager")

    elif 'open disk management' in command: 
        os.startfile(DiskManagement)
        speak("Opened Disk Management")

    elif 'close disk management' in command: 
        os.system("taskkill /f /im diskmgmt.msc")
        speak("Closed Disk Management")

    elif 'open cmd' in command or 'open terminal' in command: 
        os.startfile(CMD)
        speak("Opened Command Prompt")

    elif 'close cmd' in command or 'close terminal' in command: 
        os.system("taskkill /f /im cmd.exe")

    elif 'open notepad' in command: 
        os.startfile(Notepad)
        speak("Opened Notepad")

    elif 'close notepad' in command: 
        os.system("taskkill /f /im notepad.exe")
        speak("Closed Notepad")

    elif 'open file manager' in command or 'open file explorer' in command: 
        os.startfile(fileMGMT)
        speak("Opened File Explorer")

    elif 'close file explorer' in command or 'close file manager' in command: 
        speak("Sorry, It cannot be done.")

    elif 'open registry editor' in command: 
        os.startfile(regEditor)
        speak("Opened Registry Editor")

    elif 'close registry editor' in command: 
        os.system("taskkill /f /im regedit.exe")
        speak("Closed Registry Editor")

    elif 'open device manager' in command: 
        os.startfile(DeviceMGMT)
        speak("Opened Device Manager")

    elif 'close device manager' in command: 
        os.system("taskkill /f /im devmgmt.msc")
        speak("Closed Device Manager")

    elif 'open device info' in command: 
        os.startfile(DeviceInfo)
        speak("Opened System Information")

    elif 'close device info' in command: 
        os.system("taskkill /f /im msinfo32.exe")
        speak("Closed System Information")

    elif 'hostname' in command: 
        os.system("hostname")
        speak("Printed Hostname")

    elif 'ip address' in command: 
        os.system("ipconfig")
        speak("Printed IP Address")

    elif 'open system config' in command: 
        os.startfile(MSConfig)
        speak("Opened Microsoft Configurations")

    elif 'close system config' in command: 
        os.system("taskkill /f /im msconfig.exe")

    elif 'open system info' in command: 
        os.startfile(MSINFO)
        speak("Opened Microsoft Information")

    elif 'close system info' in command: 
        os.system("taskkill /f /im msinfo32.exe")
        speak("Closed Microsoft Information")

    elif 'take screenshot' in command or 'take a screenshot' in command: 
        press_and_release("win + PrtScn")
        speak("ScreenShot Taken")
        os.startfile("C:\\Users\\H\\Pictures\\Screenshots")

    elif 'clear screen' in command or 'cls' in command or 'clear the screen'in command:
        os.system("cls")         

    elif 'go to desktop' in command: 
        press_and_release("win + d")
        speak("Done!, You're on Desktop now") 

    elif 'open chrome' in command:  
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        speak("Opened Chrome")

    elif 'close chrome' in command or 'shutdown chrome' in command: 
        os.system("Taskkill /f /im chrome.exe")
        speak("Closed Chrome")
        os.system("cls")

    elif 'open google' in command: 
        webbrowser.open("https://www.google.com/")
        speak("Opened Google")

    elif 'open youtube' in command: 
        webbrowser.open("https://www.youtube.com/")
        speak("Opened Youtube")

    elif 'open reddit' in command: 
        webbrowser.open("https://www.reddit.com/")
        speak("Opened Reddit")

    elif 'open instagram' in command: 
        webbrowser.open("https://www.instagram.com/")
        speak("Opened Instagram")

    elif 'open camera' in command: 
        os.startfile(f"C:\\Windows\\Camera\\Camera.exe")
        speak("Opened Camera")

    elif 'close camera' in command: 
        os.system("taskkill /f /im Camera.exe")

    elif 'open control panel' in command: 
        os.system("control.exe")

    elif 'close control panel' in command: 
        speak("[Operation Aborted!], You have to close it manually.")

    else:
        System(command)
