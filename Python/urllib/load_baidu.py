import urllib.request
import urllib.parse
import string
import random

def load_data():
    base_url = "https://www.baidu.com/s?wd="
    input = {
        "wd":"哈哈",
        "key":"abc",
        "value":"efg"
    }
    prefx = urllib.parse.urlencode(input)
    url = base_url + prefx
    #定义请求头

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"
    ]
    #创建请求对象
    req = urllib.request.Request(url)
    #添加请求头
    req.add_header("User-Agent",random.choice(user_agent_list))
    response = urllib.request.urlopen(req)
    data = response.read()
    print(req.headers)
    print(req.get_full_url())
    print(data)


load_data()