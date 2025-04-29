from flask import Flask, request
import requests
import json

app = Flask(__name__)

API_KEY = '78ad180b81784d95934ec0a270e1524d'  

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            temp = data['main']['temp']
            return f"Aktualna temperatura w {city}: {temp}°C"
        else:
            return "Błąd: Nie udało się pobrać danych pogodowych."
    except Exception as e:
        return f"Błąd: {str(e)}"

@app.route('/', methods=['GET'])
def index():
    city = request.args.get('city', 'Warsaw')  
    weather_info = get_weather(city)
    return weather_info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
