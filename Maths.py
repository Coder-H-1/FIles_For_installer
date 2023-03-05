from speaker import speak

def __maths__(query):
    query = str(query)
    reply = False
    if 'sum of' in query or '+' in query:
        if 'sum of ' in query: 
            query = query.replace("sum of " , "")
            d1,d2 = query.split(" and ")
            sum = int(d1) + int(d2)
        elif '+' in query: 
            d1,d2 = query.split(" + ")
            sum = int(d1) + int(d2)
        speak(sum)
        reply = True

    elif 'subtract' in query or '-' in query:
        query = query.replace("subtract " , "")
        query = query.replace("sub " , "")
        if 'from' in query: 
            d1,d2 = query.split(" from ")
            sub = int(d2) - int(d1)
        elif 'minus' in query or '-' in query: 
            d1,d2 = query.split(" - ")
            sub = int(d1) - int(d2)
        speak(sub)
        reply = True

    elif 'multiply' in query or 'x' in query:
        if 'multiply' in query: 
            query = query.replace("multiply" , "")
            d1,d2 = query.split(" by ")
            mut = int(d1) * int(d2)
        elif 'x' in query: 
            d1,d2 = query.split(" x ")
            mut = int(d1) * int(d2)
        speak(mut)
        reply = True

    elif 'divide' in query or '/' in query or 'divided by' in query:
        if 'divide' in query: 
            query = query.replace("divide " , "")
            d1,d2 = query.split(" by ")
            div = int(d1) / int(d2)
        elif '/' in query: 
            d1,d2 = query.split("/")
            div = int(d1) / int(d2)
        elif 'divided by' in query: 
            d1,d2 = query.split("divided by")
            div = int(d1) / int(d2)
        speak(div)
        reply = True
        
    return reply