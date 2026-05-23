import requests

city = input("Enter city name: ")

api_key = "3094d1136be22a5207ef07834e83756c"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

print(data)

if response.status_code == 200:

    temperature = data["main"]["temp"]

    humidity = data["main"]["humidity"]

    weather = data["weather"][0]["description"]

    wind_speed = data["wind"]["speed"]

    print("\nWeather Details\n")

    print("City:", city)

    print("Temperature:", temperature, "°C")

    print("Humidity:", humidity, "%")

    print("Weather:", weather)

    print("Wind Speed:", wind_speed, "m/s")

else:

    print("Error:", data["message"])