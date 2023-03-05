from Modules import speak, random
from GetTime import *
from SetNote import *

def chat(_chat=None):
    if _chat != None or _chat != "None":
        hellohi = [
                'hi',
                'hello',
                'hello jarvis',
                'oh hello',
                'oh hello jarvis',
                'hola',             
                'hola amigo',
                'bonjour'
            ]
        
        hellohi_reply = [
                    'Oh hello Sir',
                    'Hello Sir',
                    'Oh hello sir, How are you Doing',
                    'Hello Sir, How are you?'
                    ]
        
        how_send = [
                'how are you',
                'how are you doing',
                'how about you',
                'how are you jarvis'
                ]
        
        how_return = [
                "I'm fine",
                "I'm fine Sir",
                "Fine Sir",
                "I'm good",
                "I'm good Sir",
                "I'm very well Sir", 
                "well Sir"
                    ]
        
        work_send = [
        'what are you doing',
        'what you doing'
        ]
        
        work_reply = [
        'Sir, I am listening and answering to you.', 
        'I am speaking to you'
        ]
        
        iam_send =  [
        "i am fine",
        "i am good",
        "mai theek hun",
        "not good"
        ]
        
        iam_reply = [
                "That's good",
                "That's Fine",
                "Oh, Great!",
                "Good To Hear That",
                "Great!",
                "Good."
                    ]
        
        iam2_send = [
                "i am not fine",
                "i am not good"
                    ]      
        
        iam2_reply = [
                "Oh?, What happened?",
                "That's not good",
                "OH!",
                "Sorry to hear but what happened?",
                "What happened?"
                    ]
        
        Nothing = [
                'nothing',
                "what can you do",
                'nothing at all'
                ]
        
        Nothing_reply = [
                'Nothing',
                'nothing at all',
                'Absolutely Nothing'
                ]       

        query = str(_chat)
        if query_Request(query) == True: pass
        else:
            speak(random.choice(hellohi_reply)  if query in hellohi else "None")
            speak(random.choice(Nothing_reply)  if query in Nothing else "None")
            speak(random.choice(iam2_reply)     if query in iam2_send else "None")
            speak(random.choice(how_return)     if query in how_send else "None")
            speak(random.choice(work_reply)     if query in work_send else "None")
            speak(random.choice(iam_reply)      if query in iam_send else "None")
            
            speak("Please don't try to abuse"   if '*' in query else "None")
            speak("Sir, 'jarvis' Here"          if 'tadashi' in query or 'friday' in query else "None")
            chat('introduce yourself' if 'who are you' in query or 'well by the way who are you' in query or 'who the heck are you' in query else "None")

            speak(GiveTime() if 'what time is it' in query or "what is the time" in query or 'tell me time' in query or 'tell time' in query else "None")
            
            if 'introduce yourself' in query: 
                speak("Hello, I am jarvis")
                speak("A 'not' very intelligent system, coded to do many stuff.")
                speak("That's it.")
