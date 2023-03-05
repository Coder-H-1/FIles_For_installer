from Modules import *

def YTSearch(query):
    """From class YouTube || Opens query on YouTube""" 
    query = str(query)
    query = query.replace("youtube " , "")
    query = query.replace("search " , "")
    query1 = query.replace(" " , "+")
    if 'play+playlist' in query1: 
        webbrowser.open("https://www.youtube.com/watch?v=Ct5kU0w1Vgk&list=PLTnfJXRz5-KMLKqe93Pa0ddscbzZSWdoM")
    elif 'play+' in query1: 
        query1 = query1.replace("play+" , "")
        pywhatkit.playonyt(query1)
        query1 = query1.replace("+" , " ")
        speak(f"Played {query1} on YouTube")
    else: 
        webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={query1}") 
