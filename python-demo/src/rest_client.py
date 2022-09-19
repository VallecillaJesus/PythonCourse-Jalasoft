import requests
import logging

URL = 'https://demo-api.free.beeceptor.com//my/api/path'

def get_demo_api_data():
    """
    GET data from Rest API Endpoint
    """
    
    response = requests.get(URL)
    
   
    if response.status_code != 200:
        logging.warning(f'Request returned non OK value {response.status_code}')
        return
        
    logging.info(f'Successful request at: {URL}')
    return response.text