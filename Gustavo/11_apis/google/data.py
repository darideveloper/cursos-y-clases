import os

def get_urls () -> list:
    """ Get urls for extract data from CSV file

    Returns:
        list: list of urls
    """
    
    # Read CSV and Request to API
    csv_path = os.path.join(os.path.dirname(__file__), 'urls.csv')
    csv_urls = open(csv_path, 'r')
    urls = [url.strip() for url in csv_urls]
    return urls
