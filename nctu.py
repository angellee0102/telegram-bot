import urllib.request as req
import bs4

url="https://www.nctu.edu.tw/"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
root=bs4.BeautifulSoup(data,"html.parser")
textTitle=root.find('h4').text
date=textTitle[1:11]
title_withoutspace=" ".join(textTitle.split())
# print(date)
# print(title_withoutspace)
def nctu_introtext():
    introtext=root.find("div",class_="introtext").text
    introtext_return=introtext.replace('\n','')
    return ('交大首頁最新內容:\n「' +title_withoutspace[11:]+"」\n"+introtext_return)

def nctu_readmore():
    readmore_link=root.find("div",class_="readmore").a['href']
    return ('https://www.nctu.edu.tw'+readmore_link)

# nctu_request()