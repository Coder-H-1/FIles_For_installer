from speaker import speak
from Modules import wikipedia

def WikiSearch(query=None, condition=None):
    """From class Wiki || Speaks results of query given if available"""
    if condition == None: 
        condition = "According To Wikipedia"
    if query != None:
        query = str(query)
        try: 
            results = wikipedia.summary(query, sentences=2)
            speak(condition)
            speak(results)
        except:
            try: 
                results = wikipedia.summary("who is " + query, sentences=2)
                speak(condition)
                speak(results)
            except:
                try: 
                    results = wikipedia.summary("defination of " + query, sentences=2)
                    speak(condition)
                    speak(results)
                except:
                    try: 
                        results = wikipedia.summary("what is " + query, sentences=2)
                        speak(condition)
                        speak(results)
                    except:
                        try: 
                            results = wikipedia.summary("where is " + query, sentences=2)
                            speak(condition)
                            speak(results)
                        except:
                            try: 
                                results = wikipedia.summary("define " + query, sentences=2)
                                speak(condition)
                                speak(results)
                            except:
                                if condition != "According to Internet":
                                    speak("Sir, Couldn't find anything about it.")
