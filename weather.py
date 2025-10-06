import requests

API_KEY = "af893453c5c3680552e6ef46c9ede7ab"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"



city_name = input("City: ")

request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city_name}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    lon = data['coord']['lon']
    lat = data['coord']['lat']
    print("")
else:
    print(response)


request_url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=fi"
response = requests.get(request_url)

print(response)
if response.status_code == 200:
    data = response.json()
    print(f"Aika on: {data['list'][0]['dt_txt']}.")
    print(f"Sää on: {data['list'][0]['weather'][0]['description']}.")
    print(f"Lämpötila on: {data['list'][0]['main']['temp']}°C" )
    print(f"Tuulennopeus on: {data['list'][0]['wind']['speed']} m/s")
    print("")
    print(f"Aika on: {data['list'][1]['dt_txt']}.")
    print(f"Sää on: {data['list'][1]['weather'][0]['description']}.")
    print(f"Lämpötila on: {data['list'][1]['main']['temp']}°C" )
    print(f"Tuulennopeus on: {data['list'][1]['wind']['speed']} m/s")
    print("")
    print(f"Aika on: {data['list'][2]['dt_txt']}.")
    print(f"Sää on: {data['list'][2]['weather'][0]['description']}.")
    print(f"Lämpötila on: {data['list'][2]['main']['temp']}°C" )
    print(f"Tuulennopeus on: {data['list'][2]['wind']['speed']} m/s")
    print("")
    print(f"Aika on: {data['list'][3]['dt_txt']}.")
    print(f"Sää on: {data['list'][3]['weather'][0]['description']}.")
    print(f"Lämpötila on: {data['list'][3]['main']['temp']}°C" )
    print(f"Tuulennopeus on: {data['list'][3]['wind']['speed']} m/s")
    print("")
    print(f"Aika on: {data['list'][4]['dt_txt']}.")
    print(f"Sää on: {data['list'][4]['weather'][0]['description']}.")
    print(f"Lämpötila on: {data['list'][4]['main']['temp']}°C" )
    print(f"Tuulennopeus on: {data['list'][4]['wind']['speed']} m/s")
    print("")
    print(f"Aika on: {data['list'][5]['dt_txt']}.")
    print(f"Sää on: {data['list'][5]['weather'][0]['description']}.")
    print(f"Lämpötila on: {data['list'][5]['main']['temp']}°C" )
    print(f"Tuulennopeus on: {data['list'][5]['wind']['speed']} m/s")
    print("")
    print(f"Aika on: {data['list'][6]['dt_txt']}.")
    print(f"Sää on: {data['list'][6]['weather'][0]['description']}.")
    print(f"Lämpötila on: {data['list'][6]['main']['temp']}°C" )
    print(f"Tuulennopeus on: {data['list'][6]['wind']['speed']} m/s")
    print("")
    print(f"Aika on: {data['list'][7]['dt_txt']}.")
    print(f"Sää on: {data['list'][7]['weather'][0]['description']}.")
    print(f"Lämpötila on: {data['list'][7]['main']['temp']}°C" )
    print(f"Tuulennopeus on: {data['list'][7]['wind']['speed']} m/s")

elif response.status_code == 401:
    data = response.json()
    print(data)



