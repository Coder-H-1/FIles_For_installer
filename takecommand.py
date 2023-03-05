import speech_recognition as sr, os

def takecommand():
    """From class takecomand || Takes Command from User in string format return query"""
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        os.system("title TADASHI - Listening...")
        r.pause_threshold = 1
        try:audio = r.listen(source, 7)
        except:pass

    try: 
        os.system("title TADASHI - Initializing...")
        query = r.recognize_google(audio)
    except:
        query = "none"
    query = str(query)
    return query.lower()