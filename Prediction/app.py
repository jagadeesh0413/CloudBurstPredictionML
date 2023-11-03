import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Load your dataset (assuming you have a CSV file)
data = pd.read_csv('cloudburst_data.csv')

# Data preprocessing
# ...
data['date'] = pd.to_datetime(data['date'])
data['time'] = pd.to_datetime(data['time']).dt.time
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['day'] = data['date'].dt.day
data.drop(['date', 'time'], axis=1, inplace=True)
# Split the data into features and target
X = data.drop('cloudburst', axis=1)
y = data['cloudburst']
# Map 'Yes' and 'No' to binary labels
data['cloudburst'] = data['cloudburst'].map({'Yes': 1, 'No': 0})

# Split the data into features and target
X = data.drop('cloudburst', axis=1)
y = data['cloudburst']

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train a Random Forest Classifier (you can try other models as well)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)
# Define the prediction function
def predict_cloudburst(date, temperature, humidity, windSpeed, precipitation, pressure):
    # Preprocess the input data similarly to the training data
    input_data = pd.DataFrame({'date': [date], 'temperature': [temperature], 'humidity': [humidity], 'windSpeed': [windSpeed], 'precipitation': [precipitation], 'pressure': [pressure]})
    input_data['date'] = pd.to_datetime(input_data['date'])
    input_data['year'] = input_data['date'].dt.year
    input_data['month'] = input_data['date'].dt.month
    input_data['day'] = input_data['date'].dt.day
    input_data.drop('date', axis=1, inplace=True)
    input_data = scaler.transform(input_data)  # Scale the input data

    # Make the prediction
    prediction = clf.predict(input_data)

    return 'Yes' if prediction[0] == 1 else 'No'  # Assuming prediction is binary (0 or 1)
@app.route('/')
def home():
    return 'Welcome to our project!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    date = data['date']
    temperature = float(data['temperature'])
    humidity = int(data['humidity'])
    windSpeed = float(data['windSpeed'])
    precipitation = float(data['precipitation'])
    pressure = float(data['pressure'])

    # Call the prediction function
    input_data = pd.DataFrame({'date': [date], 'temperature': [temperature], 'humidity': [humidity], 'windSpeed': [windSpeed], 'precipitation': [precipitation], 'pressure': [pressure]})
    input_data['date'] = pd.to_datetime(input_data['date'])
    input_data['year'] = input_data['date'].dt.year
    input_data['month'] = input_data['date'].dt.month
    input_data['day'] = input_data['date'].dt.day
    input_data.drop('date', axis=1, inplace=True)
    input_data = scaler.transform(input_data)  # Scale the input data
    prediction = predict_cloudburst(date, temperature, humidity, windSpeed, precipitation, pressure)

    # Return the prediction as JSON
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)