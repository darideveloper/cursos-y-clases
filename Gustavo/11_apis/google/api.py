import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

def connect() -> build:
    """ Connect to Google Search Console API

    Returns:
        build: element to connect to API
    """
    
    key_file = os.path.join(os.path.dirname(__file__), 'key.json')
    scope = ['https://www.googleapis.com/auth/webmasters']
    credentials = service_account.Credentials.from_service_account_file(key_file, scopes=scope)
    service = build('searchconsole', 'v1', credentials=credentials)
    return service

def get_data_url (url:str, service:build) -> dict:
    """ Get data from specific URL

    Args:
        url (str): url to extract data
        service (build): element to connect to API

    Returns:
        dict: data from specific URL
    """
    
    request = {
        "startDate": '2023-01-01',
        "endDate": '2023-03-01',
        "dimensions": ["page"],
        "dimensionFilterGroups": [{
            'filters': [{
                'dimension': 'page',
                'operator': 'equals',
                'expression': url
            }]
        }]
    }
    
    response = service.searchanalytics().query(siteUrl='sc-domain:mixkit.co', body=request).execute()
    
    return response