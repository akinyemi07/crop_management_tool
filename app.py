from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

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

# Get the current weather (mocked for now, you can add real weather API integration)
def get_current_weather():
    return random.choice(list(weather_mapping.keys()))  # Random weather for demo

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_crop', methods=['POST'])
def predict_crop():
    current_weather = get_current_weather()
    print(f"Current weather: {current_weather}")
    
    soil_type = request.form['soil_type']

    # Ensure valid weather and soil types
    if current_weather not in weather_mapping or soil_type not in soil_mapping:
        return "Invalid weather or soil type", 400

    # Predict crop based on weather and soil
    input_data = (weather_mapping[current_weather], soil_mapping[soil_type])
    recommended_crop = crop_recommendations.get(input_data, "No recommendation available")

    return render_template('result.html', recommended_crop=recommended_crop, weather=current_weather, soil=soil_type)

if __name__ == '__main__':
    app.run(debug=True)

