from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Dummy prediction function
def predict_cloudburst(date, temperature, humidity, wind_speed, precipitation, pressure):
    # Replace this with your actual prediction logic
    # For now, return 'Yes' if temperature is above 25°C, 'No' otherwise
    if temperature > 25:
        return 'Yes'
    else:
        return 'No'
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    date = data.get('date')
    temperature = float(data.get('temperature'))
    humidity = int(data.get('humidity'))
    wind_speed = float(data.get('wind-speed'))
    precipitation = float(data.get('precipitation'))
    pressure = float(data.get('pressure'))

    # Call the dummy prediction function
    prediction = predict_cloudburst(date, temperature, humidity, wind_speed, precipitation, pressure)

    # Return the prediction as JSON
    return jsonify({'prediction': prediction})
if __name__ == '__main__':
    app.run(debug=True)
