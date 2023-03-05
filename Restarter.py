from Modules import os,sys,path,speak
class Restarter: ### To restart this file
    def res():
        try: 
            os.startfile(f"{path}\\Main.py")
            sys.exit()
        except Exception as e:
            speak(f"Error - [{e}]")