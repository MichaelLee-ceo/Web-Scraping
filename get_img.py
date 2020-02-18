import requests, bs4, re

def get_web_page(url):
    res = requests.get(url)
    if res.status_code != 200:
        print('Invalid Url', url)
        return None
    else:
        return res.text

def get_imgUrl(response):

    tag = input('請輸入目標標籤:')
    attr = input('請輸入標籤屬性:')

    obj = bs4.BeautifulSoup(response, 'lxml')
    imgTag = obj.select(tag)
    print('搜尋到圖片數量:', len(imgTag))

    imgUrl = obj.findAll(tag, {attr:re.compile('\.jpg$')})
    print('下載圖片數量:', len(imgUrl))

    for img in imgUrl:
        if img[attr].startswith('http'):
            print(img[attr], '...圖片下載中...')

            pic = requests.get(img[attr])
            file = open('D:/out_put/' + img[attr].split('/')[-1], 'wb')
            file.write(pic.content)
            file.close()
    print('\n')
    m = '圖片下載完成'
    print(m.center(30,'='))

resp = get_web_page('http://bobotako.pixnet.net/blog/post/47382884-%E3%80%90%E5%8F%B0%E4%B8%AD%E4%BD%8F%E5%AE%BF%E3%80%91%E5%B9%B3%E5%83%B9%E4%BD%86%E7%89%A9%E8%B6%85%E6%89%80%E5%80%BC%E7%9A%84-%E5%8F%B0%E4%B8%AD%E5%8D%9A%E5%A5%87%E5%A4%A75f3e5rf4r5f')
get_imgUrl(resp)