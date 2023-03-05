from Modules import *
def query_reset():
    for files in os.listdir(f"{path}\\Custom_Set"):
        if files == "speak_attrib.value":pass
        else:
            try: 
                os.remove(f"{path}\\Custom_Set\\{files}")
            except Exception as e: 
                print(f"Error : [ {e} ]")

def query_Set(query):
    query = str(query)
    query = query.replace("set chat " , "")
    query = query.replace("if i say " , "")
    isay, ysay = query.split(" you say ")
    filesnumb = 0
    for files in os.listdir(f"{os.getcwd()}//Custom_Set"):
        filesnumb+=1
    with open(f"{os.getcwd()}//Custom_Set//Custom{filesnumb}.set_value", "w") as file1: 
        file1.write(f"{isay} : {ysay}\n")
    file1.close()

def query_Request(query):
    query = str(query)
    toReturn = False
    for files in os.listdir(f"{os.getcwd()}//Custom_Set"):
        if files == "speak_attrib.value":pass
        else:
            for lines in open(f"{os.getcwd()}//Custom_Set//{files}", "r"):
                lines = str(lines)
                isay, ysay = lines.split(" : ")
                if query == isay: 
                    speak(ysay)
                    toReturn = True
    return toReturn