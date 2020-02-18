import requests, bs4, re

def get_imgUrl(res):
    obj = bs4.BeautifulSoup(res, 'lxml')
    imgTag = obj.select('img')
    print('搜尋到圖片:', len(imgTag))

    imgUrl = obj.findAll('img', {'src':re.compile('\.jpg$')})
    print('下載圖片數量:', len(imgUrl))

    for img in imgUrl:
        if img['src'].startswith('http'):
            print(img['src'].split('%')[-1], '...圖片下載中...')
            pic = requests.get(img['src'])
            pic.raise_for_status()
            print('圖片下載成功!')
            file = open('D:/imgoutput/' + img['src'].split('%')[-1], 'wb')
            file.write(pic.content)
            file.close()
    m = '圖片下載完成'
    print(m.center(30, '='))

get_imgUrl()

