from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)

# OpenWeather API Integration 
OPENWEATHER_API_KEY = 'c3429ac0b0a5645df06acc29acc66fdd'

# Weather and soil type mappings
weather_mapping = {'Sunny': 0, 'Rain': 1, 'Cloudy': 2, 'Stormy': 3}
soil_mapping = {'Loam': 0, 'Clay': 1, 'Sand': 2}

# Crop recommendations based on weather and soil type
crop_recommendations = {
    (0, 0): "Wheat",
    (0, 1): "Barley",
    (0, 2): "Carrots",
    (1, 0): "Rice",
    (1, 1): "Sugarcane",
    (1, 2): "Corn",
    (2, 0): "Peas",
    (2, 1): "Cabbage",
    (2, 2): "Potatoes",
    (3, 0): "Ginger",
    (3, 1): "Turmeric",
    (3, 2): "Bananas"
}

# Get current weather using OpenWeather API
def get_current_weather(city="London"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"{weather_description.capitalize()}, {temperature}°C"
    else:
        return "Weather data unavailable"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_crop', methods=['POST'])
def predict_crop():
    # Get real-time weather
    city = request.form['city']
    current_weather = get_current_weather(city)
    print(f"Current weather: {current_weather}")

    soil_type = request.form['soil_type']

    # Predict crop based on weather and soil
    recommended_crop = "Wheat"  # Default prediction (change based on actual logic)

    return render_template('result.html', recommended_crop=recommended_crop, weather=current_weather, soil=soil_type)

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_text = request.form['feedback']
    # Here, we would typically save feedback in a database (but we'll just print for now)
    print(f"User feedback: {feedback_text}")
    return jsonify({"message": "Thank you for your feedback!"})

if __name__ == '__main__':
    app.run(debug=True)

