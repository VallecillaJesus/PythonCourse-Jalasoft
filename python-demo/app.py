import os
import requests
from datetime import date, datetime

URL = 'https://demo-api.free.beeceptor.com/'

def get_datetime():
    current_datetime = datetime.now()
    date = str(current_datetime.date()).replace('-','') 
    time = str(current_datetime.time()).replace(':','')[:6]
    return date + time

def get_request_data():
    response = requests.get(URL)
    return str(response.content)


def generate_file(path, filename, content):
    foldername = filename.replace('log_','')[:8]
    target = path + foldername + '\\' + filename

    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w") as file:
        file.write(content)


def main():
    current_folder = os.getcwd() + "\\"

    datetime  = get_datetime()
    generate_file(current_folder,f"log_{datetime}.txt",get_request_data())
    # filename = "log_{}{}{}".format(time.hour,time.minute,time.second)
    # print(filename, type(filename))

    # os.makedirs(current_folder + foldername, exist_ok=True)

    # with open(filename, "w") as file:
    #     file.write(response.content)
        

main()