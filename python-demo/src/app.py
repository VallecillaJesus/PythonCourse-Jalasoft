import os
from rest_client import get_demo_api_data
from files_helper import generate_file
from helpers import get_datetime


def main():
    current_folder = os.getcwd() + "\\"

    datetime  = get_datetime()
    generate_file(current_folder,f"log_{datetime}.txt", get_demo_api_data())
        

main()