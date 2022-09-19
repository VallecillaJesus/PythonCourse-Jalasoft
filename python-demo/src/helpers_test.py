from datetime import datetime
import helpers
    


def get_datetime_date_test():
    current_datetime = datetime.now()
    generated_datetime = helpers.get_datetime()
    
    date = str(current_datetime.date()).replace('-','') 
    time = str(current_datetime.time()).replace(':','')[:5]
    current_datetime = date + time
    assert current_datetime == generated_datetime, "Generated datetime is not correct"

def main():
    get_datetime_date_test()

main() 