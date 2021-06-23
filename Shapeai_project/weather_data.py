import requests
from datetime import datetime

#vars
api_key = '8a0d2778bdf4795fae846be737b618ed'
location = input("Enter the city name: ")
file_name = "weather_info.txt"

#Connect to website using API and fetching data
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#wirte function
def write_function(file_name):
    with open(file_name,'w') as f:
        f.write("-------------------------------------------------------------\n")
        f.write("Weather Stats for - {}  || {} \n".format(location.upper(), date_time))
        f.write("-------------------------------------------------------------\n")

        f.write("Current temperature is: {:.2f} deg C \n".format(temp_city))
        f.write("Current weather desc  : {} \n".format(weather_desc))
        f.write("Current Humidity      : {} {} \n".format(hmdt,'%'))
        f.write("Current wind speed    : {} {} \n".format(wind_spd ,'kmph'))
    print("successfully file written")



write_function(file_name)