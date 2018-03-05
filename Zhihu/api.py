import requests

api_url = 'https://news-at.zhihu.com/api/4/news/'

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

def fetch_news_list():
    req = requests.get(api_url + 'latest', headers=HEADERS).json()
    return req

def fetch_news(id_str):
    return requests.get(api_url + id_str, headers=HEADERS).json()
