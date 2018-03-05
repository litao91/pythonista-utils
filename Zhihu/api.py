import requests
from string import Template

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
    return requests.get(api_url + str(id_str), headers=HEADERS).json()


def gen_page(news):
    image = Template(
        '''
<div class="img-wrap">
<h1 class="headline-title">$title</h1>


<span class="img-source">$image_source</span>


<img src="$image" alt="">
<div class="img-mask"></div>
</div>
        ''').safe_substitute(
            title=news['title'],
            image_source=news['image_source'],
            image=news['image']
        )
    template = Template(
        '''
        <html>
        <head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
        <!--
        <link rel="stylesheet" type="text/css" href="$cssurl">
        -->
        <link rel="stylesheet" type="text/css" href="http://news-at.zhihu.com/css/share.css?v5956a">
        </head>
        <body>
        <!--
        <img src="$image" alt="$image_source">
        -->
        $body
        </body>
        </html>
        ''')
    body = news['body']
    cssurl = news['css'][0]
    return template.safe_substitute(
        cssurl=cssurl,
        body=body,
        image=news['image'],
        image_source=news['image_source']).replace('<div class="img-place-holder"></div>', image)
