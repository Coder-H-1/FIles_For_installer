from Modules import platform, os,sys
from speaker import speak
def __System__():
    """From class SystemVerify || Checks if a.i is capable with os"""
    "Informations about user's pc"
    name = platform.system()
    print("Verifing the Operating System (OS)")
    if name != "Windows": 
        print("Verification --> Error OS: Not Windows")
        speak("Sorry, not developed for other System, Only for Windows thankyou")
        sys.exit()

    elif 'Windows' in name: 
        print("Verification : Done")
        processor = platform.architecture()[0]
        other = platform.platform()
        print("OS : " + other, processor)
        print("")
        os.system("cls")

__System__()