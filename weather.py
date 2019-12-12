# Python program to find current  
# weather details of any city 
# using openweathermap api 
  
# import required modules 
import requests, json,os

api_key = os.environ["WEATHER_API"]
base_url = "http://api.openweathermap.org/data/2.5/weather"
  
city_name = input("Enter city name : ") 
if city_name=="":
    city_name='Taipei'
complete_url = base_url + "?q=" + city_name  +"&APPID=" + api_key

response = requests.get(complete_url) 
x = response.json() 
# print(complete_url)
# print(x)
# print(x["cod"])
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404" and x["cod"] != "401": 
  

    y = x["main"] 
    current_temperature = y["temp"]-273.15
    current_humidiy = y["humidity"] 
  
    # print following values 
    print(city_name+ "\n現在天氣："+
            "\n氣溫 = " +str(current_temperature)[:5] +"°C"+ 
          "\n濕度 = " +str(current_humidiy) +'%'+
          "\n降雨機率 = ") 
  
else: 
    print(" City Not Found ") 