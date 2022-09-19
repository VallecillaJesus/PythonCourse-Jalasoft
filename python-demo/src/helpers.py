from datetime import datetime

def get_datetime():
    current_datetime = datetime.now()
    date = str(current_datetime.date()).replace('-','') 
    time = str(current_datetime.time()).replace(':','')[:5]
    return date + time