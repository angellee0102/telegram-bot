# https://medium.com/@aakankshaws/using-beautifulsoup-requests-to-scrape-weather-data-9c6e9d317800
import requests
page = requests.get("https://weather.com/zh-TW/weather/tenday/l/TWXX0021:1:TW")
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,"html.parser")
all=soup.find("div",{"class":"locations-title ten-day-page-title"}).find("h1").text
table=soup.find_all("table",{"class":"twc-table"})
l=[]
for items in table:
    # for i in range(len(items.find_all("tr"))-1):
    for i in range(4):
        d = {}  
        # d["day"]=items.find_all("span",{"class":"date-time"})[i].text
        d["date"]=items.find_all("span",{"class":"day-detail"})[i].text
        d["description"]=items.find_all("td",{"class":"description"})[i].text 
        d["high/low temp"]=items.find_all("td",{"class":"temp"})[i].text 
        d["precip"]=items.find_all("td",{"class":"precip"})[i].text
        # d["wind"]=items.find_all("td",{"class":"wind"})[i].text  
        d["humidity"]=items.find_all("td",{"class":"humidity"})[i].text 
        l.append(d)

import pandas
df = pandas.DataFrame(l)
def get_weather_string(i):
    result="\n日期: "+df.iloc[i]['date']+\
        '\n天氣: '+df.iloc[i]['description']+\
        '\n高低溫: '+df.iloc[i]['high/low temp']+\
        '\n降雨機率: '+df.iloc[i]['precip']+\
        '\n濕度: '+df.iloc[i]['humidity']
    return result

def today_weather():
    today_weather_str='\n「今天」天氣：'+get_weather_string(0)
    return today_weather_str
def tomorrow_weather():
    tomorrow_weather_str='\n「明天」天氣: '+get_weather_string(1)
    return tomorrow_weather_str
def afterTomorrow_weather():
    afterTomorrow_weather_str='\n「後天」天氣:'+get_weather_string(2)
    return afterTomorrow_weather_str