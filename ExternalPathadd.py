from Modules import os
def EXECUTE(query):
    query = str(query)
    query = query.replace("open " , "")
    for files in os.listdir(f"{os.getcwd()}//Custom_Path"):
        for lines in open(f"{os.getcwd()}//Custom_Path//{files}", "r"):
            lines = str(lines)
            thing, execution = lines.split(" : ")
            if query == thing: 
                os.startfile(execution)