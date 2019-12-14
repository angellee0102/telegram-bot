import urllib.request as req
import bs4
def news_result():
    url="https://www.cna.com.tw/list/aall.aspx"
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")

    news_list=root.find("ul",class_="sub_menu")
    first_news_title=news_list.findChild().a.text
    first_news_url=news_list.a['href']

    def first_news_paragraph(url):
        request=req.Request(url, headers={
            "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36"
        })
        with req.urlopen(request) as response:
            data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data,"html.parser")
        first_paragraph=root.find("p").text
        return (first_paragraph)

    paragraph=first_news_paragraph(first_news_url)
    result= first_news_title+'\n'+paragraph+'\n'+first_news_url
    return result

