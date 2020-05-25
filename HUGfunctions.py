from datetime import date,datetime

def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year 
  
    return age 

def create_households(x) :
    listold=['11','21','31']
    listold2=['410','411']
    if len(str(x))==6 :
        return str(x)
    elif (any(c in str(x)[:2] for c in listold) and len(str(x))==7) :
        return str(x)[:-1]
    elif len(str(x))==8 :
        return str(x)[:-1]
    elif (any(c in str(x)[:3] for c in listold2) and len(str(x))==7) :
        return str(x)[:-1]
    else :
        return str(x)

def convertDate(x) :
    #from datetime import datetime
    if x!=x :
        return x
    else :
        datasplit=str(x).split(' ')
        if len(datasplit)>1 :
            return datetime.strptime(datasplit[0], '%Y-%m-%d')
        else :
            return datetime.strptime(datasplit[0], '%d.%m.%Y')
