import datetime
from Speak import Say
import os
def Time():
    time  = datetime.datetime.now().strftime("%H:%M")
    Say(time)
def Date():
    date = datetime.date.today()
    Say(date)

def Commandprompt():
    os.system("start cmd")

def NoninputExecution(query):
    query = str(query)
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "command prompt" in query:
        Commandprompt()
    else:
        Say("Sorry I don't understand that")

def Wikipedia(tag,query):
    name = str(query)
    import wikipedia
    result = wikipedia.summary(name).replace("who is","").replace("about","").replace("tell me about","").replace("what is","").replace("what is the","").replace("what is the definition of","").replace("what is the meaning of","").replace("what is the meaning of the word","").replace("what is the meaning of the term","").replace("wikipedia","")  
    Say(result) 

def Google(tag,query):
    import pywhatkit
    query = str(query)
    result = query.replace("google","").replace("search for","").replace("google search","")
    pywhatkit.search(result)


def InputFunction(tag,query):
    if "wikipedia" in tag:
         Wikipedia(tag,query) 
    elif "google" in tag:
        Google(tag,query)
     