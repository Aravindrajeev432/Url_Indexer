import requests
from decouple import config
import time
api_key = config("APIKEY")
site_url = config("SITEURL")
url_list = config("URLLIST", cast=lambda v: [s.strip() for s in v.split(',')])


def record_timestamp(result):
    with open('timestamp.txt', 'a') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S") + str(result) + '\n')


def main() -> bool:
    
    url: str = "ssl.bing.com/webmaster/api.svc/json/SubmitUrIbatch"
    headers: dict = {
        "Content-Type": "application/json",
        "charset": "utf-8",
    }
    params: dict = {
        "apikey": api_key,
    }
    data: dict = {"siteUrl": site_url, "urlList": url_list}
    response = requests.get(url, headers=headers, params=params, json=data)
    if response.status_code == 200:
        return True
    return False


record_timestamp(result=main())