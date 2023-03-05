from Modules import pywhatkit
from Wiki import WikiSearch

def GoogleSearch(self, query):
    query = str(query)
    query = query.replace("google search " , "")
    query = query.replace("google " , "")
    query1= query.replace(' ' , "+")
    pywhatkit.search(query1)
    WikiSearch(query, 'According to Internet')