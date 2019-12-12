import urllib.request as req
import bs4

url="https://www.cna.com.tw/list/aall.aspx"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
root=bs4.BeautifulSoup(data,"html.parser")
print(root)