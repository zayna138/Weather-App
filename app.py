```python
import streamlit as st
import requests

st.title("🌤 Weather App")

city = st.text_input("Enter city name")

api_key = "3094d1136be22a5207ef07834e83756c"

if city:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        st.subheader("Weather Details")

        st.write(f"📍 City: {city}")
        st.write(f"🌡 Temperature: {temperature} °C")
        st.write(f"💧 Humidity: {humidity}%")
        st.write(f"☁ Weather: {weather}")
        st.write(f"🌬 Wind Speed: {wind_speed} m/s")

    else:
        st.error(data["message"])
```
