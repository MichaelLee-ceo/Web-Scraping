import requests, bs4, traceback, time

start = time.time()

url = 'https://www.dcard.tw/search/general?query=UX430'
res = requests.get(url)
#print(res.text)


obj = bs4.BeautifulSoup(res.text, 'lxml')

titles = obj.find_all('h3', {'class': 'PostEntry_title_H5o4d PostEntry_unread_2U217'})  #find_all回傳一組list
posts = obj.find_all('div', {'class': 'PostEntry_excerpt_2eHlN'})
links = obj.find_all('a', {'class': 'PostEntry_root_V6g0r'})
print('搜尋到標題數量:', len(titles))
print('搜尋到內文數量:', len(posts))
print('搜尋到文章數量:', len(links))

count = 0
#error = 0

file = open('D:/ux430.txt', 'w+', encoding = 'utf8')         #encoding = 'utf-8' --> UnicodeEncodeError-cp950
for c in titles:
    #try:
        t = '  ' + '>>>' + ' ' + c.text
        file.write(t)
        file.write('\n')

        l = '  ' + 'Link: ' + 'https://www.dcard.tw' + links[count]['href']
        file.write(l)
        file.write('\n')

        p = '內文:' + '\n' + posts[count].text + '\n'
        file.write(p)
        file.write('\n')
    #except:

        # error += 1
        #
        # print('---異常發生---')
        # errorFile = open('D:/pythonError.txt', 'a')
        # errorFile.write(traceback.format_exc())
        # print('===異常回報完畢===', '\n')
        # errorFile.close()

        count += 1

#print('發現異常資料:', error, '筆')

file.close()

print('=====Finished=====')

end = time.time()

print('花費時間:', end - start)


# for c in posts:
#     print(c.text)
#
# print('===========')
#
# print(posts[0].text)