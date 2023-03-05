from Modules import *

def __ChangeSet__(hour):
    """From class GetTime || Changes 24 hour time to 12 hour time"""
    hour = int(hour)
    if hour == 13:
        return "1", "PM"
    elif hour == 14:
        return "2", "PM"
    elif hour == 15:
        return "3", "PM"
    elif hour == 16:
        return "4", "PM"
    elif hour == 17:
        return "5", "PM"
    elif hour == 18:
        return "6", "PM"
    elif hour == 19:
        return "7", "PM"
    elif hour == 20:
        return "8", "PM"
    elif hour == 21:
        return "9", "PM"
    elif hour == 22:
        return "10", "PM"
    elif hour == 23:
        return "11", "PM"
    elif hour == 24:
        return "12", "PM"
    else:
        return str(hour),"AM"

def onlytime():
    """From class GetTime || Returns hour and minute in a tuple"""
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    return hour, minute  

def MonChanger(_time_=0):
    "From class GetTime || Changes number of months to their names"
    ### For month ###
    _time_ = int(_time_)
    if _time_ == 1: 
        return "January"
    elif _time_ == 2: 
        return "February"
    elif _time_ == 3: 
        return "March"
    elif _time_ == 4: 
        return "April"
    elif _time_ == 5: 
        return "May"
    elif _time_ == 6: 
        return "June"
    elif _time_ == 7: 
        return "July"
    elif _time_ == 8: 
        return "August"
    elif _time_ == 9: 
        return "September"
    elif _time_ == 10: 
        return "October"
    elif _time_ == 11: 
        return "November"
    elif _time_ == 12: 
        return "December"
    return f"{_time_}" ### Returns Month in string format


def GiveTime():
    """From class GetTime || Returns time in String form"""
    hour = datetime.datetime.now().strftime("%H")
    minute = datetime.datetime.now().strftime("%M")
    Day = datetime.datetime.now().strftime("%d")
    month = datetime.datetime.now().strftime("%m")
    year = datetime.datetime.now().strftime("%y")
    hour = int(hour)
    _date_ = MonChanger(month)
    if hour <= 12:
        _get = "AM"
    elif hour >= 13: 
        hour,_get = __ChangeSet__(hour)
    return f"Time is {hour}:{minute} {_get} of date {Day}-{_date_}-{year}"

