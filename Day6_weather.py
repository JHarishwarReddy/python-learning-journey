import requests

API_KEY = "a3584f72c4373d73bbcae3a17a9fd78c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            Max_temperature = data["main"]["temp_max"]
            Min_temperature = data["main"]["temp_min"]
            feels_like = data["main"]["feels_like"]
            weather_description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print(f"Weather in {name}, {country}:")
            print(f"Temperature: {temperature}°C")
            print(f"Max and Min Temperature: {Max_temperature}°C / {Min_temperature}°C")
            print(f"Feels like: {feels_like}°C")
            print(f"Description: {weather_description}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
            
        else:
            print(f"Error City Not Found: {data['message']}")
            print("Please check the city name and try again.")
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the weather service. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

#Main function to run the weather application
while True:
    city = input("Enter city name (or 'exit' to quit): ")
    if city.lower() == 'exit':
        break
    get_weather(city)