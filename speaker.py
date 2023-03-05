import pyttsx3, os

path = os.getcwd()


Attrib=[ 1 , 200 , 0 , 'Female' ]   ### Values may differ

class Check:
    """From class speak """
    def __speakAttrib__():
        """From class speak || Checks speak attribute file for any changes"""
        default = [ 0 , 200 , 0 , 'Male']
        for lines in open(f"{os.getcwd()}\\Custom_Set\\speak_attrib.value" , "r"):
            if "set volume : " in lines:
                lines = lines.replace("set volume : " , "")
                if int(lines) <= 1:
                    Attrib[0] = lines
                else: 
                    Attrib[0] = default[0]
            elif "set vol_pace : " in lines:
                lines = lines.replace("set vol_pace : " , "")
                if int(lines) <= 300:
                    Attrib[1] = lines
                else: 
                    Attrib[1] = default[1]
            elif "set voice : " in lines:
                lines = lines.replace("set voice : " , "")
                if int(lines) <= 5:
                    Attrib[2] = lines
                else: 
                    Attrib[2] = default[2]
            elif "set voice_gender : " in lines:
                lines = lines.replace("set voice_gender : " , "")
                Attrib[3] = f"{lines}"

def speak(audio):
    """From class speak || Output audio - Speech"""


    if audio == "None" or audio == None or audio == "none": pass

    else:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[int(Attrib[2])].id)
        engine.setProperty('rate' , int(Attrib[1]))
        engine.setProperty('volume' , int(Attrib[0]))
        print(f"TADASHI : {audio}")
        engine.say(audio)
        engine.runAndWait()
    
Check.__speakAttrib__()
