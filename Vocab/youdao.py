import requests

__version__ = "0.1.0"

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
# 有道申请的 key
KEY= "1945325576"
KEY_FROM = "Youdao-dict-v21"

def query_words(words):
    """使用有道 API 查询词典并在终端打印，输出的 result 格式
    （空格，>>，换行之类的）不要在意因为我有强迫症- -!
    :param words:
        要查询的单词或句子
    """
    url = "http://fanyi.youdao.com/openapi.do?keyfrom={}&key={}" \
          "&type=data&doctype=json&version=1.1&q={}"

    try:
        req = requests.get(
            url.format(KEY_FROM, KEY, words), headers=HEADERS).json()
        # errorCode 为 0 是正常状态
        r_str = ''
        if req['errorCode'] == 0:
            r_str = r_str + ">>  {}: {} \n".format(words, "".join(req['translation']))
            # 类似短语和缩写词如 API,JDK 之类的无音标属性
            try:
                us_phonetic = req['basic']['us-phonetic']
                uk_phonetic = req['basic']['uk-phonetic']
                r_str = r_str + "    美:[{}]  英:[{}]\n".format(us_phonetic, uk_phonetic)
            except:
                pass
            # 查询不到内容时没有 'basic' 属性
            if "basic" in req:
                # 词典释义内容
                for _, value in enumerate(req['basic']['explains']):
                    r_str = r_str + "    {}\n".format(value)
                
                # 网络释义内容
                for _, value in enumerate(req['web']):
                    r_str = r_str + "    {}{}\n".format(value['key'], value['value'])
            return r_str
        else:
            # 输入查询的内容有误，检查拼写
            print(">>  Exception: The words can't be found,"
                  "please check your spelling")
    except Exception:
        # 网络错误，API 无法访问或者输入了奇怪的东西，如 fuck$#$#
        print(">>  Please check your spelling or network connection")
        

# for testing
if __name__ == '__main__':
	print(query_words('test'))
