# import dependencies
import requests # make HTTP GET request


# construct API request URL and fetch data in JSON format
def get_weather_data(API_KEY, city_name):
     API_URL = 'https://api.openweathermap.org/data/2.5/weather'
     payload = {
          'q': city_name,
          'appid': API_KEY,
          'units': 'metric'
     }

     try:
          response = requests.get(API_URL, params=payload)
          weather_data = response.json()

          # check if response is successful
          if response.status_code == 200:
               return weather_data
          else:
               print(f"[!] Error: {weather_data['message']}")
               return None
          
     except Exception as e:
          print(f"Error: {e}")
          return None


# print relevant weather information 
def display_data(weather_data):
     if weather_data:
          print(f"\nCurrent weather in {weather_data['name']}, {weather_data['sys']['country']}:")
          print(f"Coordinates >> Latitude: {weather_data['coord']['lat']}, Longitude: {weather_data['coord']['lon']}")
          print(f">> Weather: {weather_data['weather'][0]['description']}")
          print(f">> Temperature: {weather_data['main']['temp']}°C")
          print(f">> Clouds: {weather_data['clouds']['all']}%")
          print(f">> Humidity: {weather_data['main']['humidity']}%")
          print(f">> Pressure: {weather_data['main']['pressure']} hPa")
          print(f">> Wind direction: {weather_data['wind']['deg']}°")
          print(f">> Wind Speed: {weather_data['wind']['speed']} m/s") 
     else:
          print("[!] Unable to fetch weather information.")


# get user input, call functions to fetch and display weather information
def main():
     API_KEY = "YOUR_API_KEY_GOES_HERE" # OpenWeatherMap API Key here 

     # capture user input >> direct geocoding
     city_name = input(f"Enter city name: ")

     # fetch data
     weather_data = get_weather_data(API_KEY, city_name)

     # display weather information
     display_data(weather_data)


if __name__ == "__main__":
     main()
