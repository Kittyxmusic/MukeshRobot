class Config(object):
    LOGGER = True
    API_ID = 25614292 
    API_HASH = "59ee8005ce6b056fa639d956f028eeeb"
    TOKEN = "6909402640:AAEUXjuibT9DlAl72lSi3JtVFnwUWwG931Q"
    OWNER_ID= 7006715434
    
    SUPPORT_CHAT = "kittybothub"
    START_IMG = "https://telegra.ph/file/5618197d321f4f555bb9c.jpg"
    EVENT_LOGS = (-1002024032988)
    MONGO_DB_URI= "mongodb+srv://chalcogen:dumb980@cluster0.u25jq25.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
   
    DATABASE_URL = " postgresql://xrlkskby:gobwyeqocauwmdrggqom@alpha.mkdb.sh:5432/rjfvbvc"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "4Z5UHYEW3LJ7U99J"
    )
    TIME_API_KEY = "V33SSMCSDT6L"

    
    BL_CHATS = [] 
    DRAGONS = [7006715434]
    DEV_USERS = [7006715434]  
    DEMONS = [7006715434] 
    TIGERS = [7006715434]  
    WOLVES = [7006715434] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
