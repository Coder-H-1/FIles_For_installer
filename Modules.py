import os,sys
try:
    import pyttsx3, speech_recognition as sr, wikipedia,pyautogui
    from keyboard import press_and_release, write
    from pyautogui import rightClick
except:
    import os,sys
    print("Module(s) not found --->  Downloading them")
    os.system("python.exe -m pip install pyttsx3 wikipedia speechRecognition pyautogui keyboard pywhatkit")
    os.system("python.exe -m pip install pyaudio")
    speak("Please Try to Restart me")
    sys.exit()



##########################################################################################################################################################################################
# Folder and speak attrib files making and checking
path = os.getcwd()

try: os.makedirs(f"{path}//Custom_Set")
except:pass
try: os.makedirs(f"{path}//Custom_Path")
except:pass
try: open(f"{path}\\Custom_Set\\speak_attrib.value" , "r")
except:
    try:
        with open(f"{path}\\Custom_Set\\speak_attrib.value" , "w") as fileattrib:
            fileattrib.write(
                "set volume : 1\nset vol_pace : 210\nset voice : 0\nset voice_gender : Female"
                )
        print("Fixed : Error [ speak_attrib.value not found in Custom_Set ]")
    except:
        print("Try to run TADASHI with administrative powers")

###########################################################################################################

from speaker import speak
try: import pywhatkit
except: 
    speak("Please start me with Internet")
    sys.exit()

import os, sys, random, time, datetime, platform, webbrowser

