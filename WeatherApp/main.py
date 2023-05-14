import requests
import json

city = input("Enter the name of the city:\n").capitalize()
url = f"""http://api.weatherapi.com/v1/current.json?key=1dccb8c2f03c4cbdb48142719230805&q={city}"""

r = requests.get(url)

weatherDict = json.loads(r.text)
# print(type(weatherDict))
data = weatherDict["current"]["temp_c"]
print(f"The current weather in {city} is {data} Degrees Celsius")
