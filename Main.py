
### Imports of Files class and function 
from Modules import *
from Chatbot import chat as CHAT
from CodedPaths import *
from ExternalPathadd import EXECUTE
from GetTime import *
from Google import GoogleSearch
from Maths import __maths__ as MATHS
from Restarter import Restarter
from SetNote import *
from speaker import speak
from SystemCommand import Sys as SYS
import SystemVerify
from takecommand import takecommand
from Wiki import WikiSearch
from YouTube import YTSearch
###


class Main:
    """The Home for all Classes containing all functioning of jarvis\n
    After an update that converted every class to file changed this title"""

    class Responder:
        def res():
            query = takecommand().lower()
            if query != "none":
                print("User Said : " + query)
                if 'google search' in query: 
                    GoogleSearch(query)

                elif 'wikipedia ' in query or 'define ' in query: 
                    query = query.replace("wikipedia search " , "")
                    query=query.replace("wikipedia " , "")
                    WikiSearch(query) 

                elif 'youtube ' in query: 
                    YTSearch(query)

                elif 'system showdown' in query or 'exit system' in query or 'quit' in query: 
                    speak("Have a good day Sir")
                    sys.exit()

                elif 'restart yourself' in query or 'recharge yourself' in query:
                    speak("Restarting Myself")
                    Restarter.res()

                elif 'start ' in query: 
                    EXECUTE(query)

                elif 'et chat ' in query: 
                    query_Set(query)

                elif 'reset chat' in query: 
                    query_reset()

                else:
                    SYS(query)
                    CHAT(query)
                    MATHS(query)

                   
if __name__=="__main__":
    os.system("title JARVIS - At your service")
    os.system("cls")
    hour, minute = onlytime()
    speak("Good Morning, Sir" if int(hour) > 0 and int(hour) <= 11 and int(minute) < 60 else "None")
    speak("Good Afternoon, Sir" if int(hour) > 11 and int(hour) <= 15 and int(minute) < 60 else "None")
    speak("Good Evening, Sir" if int(hour) > 15 and int(hour) <= 18 and int(minute) < 60 else "None")
    speak("Good Night, Sir" if int(hour) > 18 and int(minute) < 60 else "None")

    speak(GiveTime()) 
    while True:
        try: Main.Responder.res()
        except Exception as e: 
            print(f"Error : [ {e} ]")
