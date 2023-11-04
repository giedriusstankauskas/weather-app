from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        return render_template('weather.html', weather_data=weather_data)
    return render_template('weather.html', weather_data=None)


def get_weather(city):
    # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    data = response.json()
    return data


if __name__ == '__main__':
    app.run(debug=True)
