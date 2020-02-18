import requests

def get_web_page(url):
    res = requests.get(url)
    if res.status_code != 200:
        print('Invalid Url', url)
        return None
    else:
        return res.text

get_web_page()