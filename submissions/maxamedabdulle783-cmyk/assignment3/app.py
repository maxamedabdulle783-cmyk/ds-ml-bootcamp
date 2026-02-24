import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the dataset
df = pd.read_csv('weather_dataset.csv')

# 1. Handling Missing Values
df['Temperature_C'] = df['Temperature_C'].fillna(df['Temperature_C'].mean())
df['Rainfall_mm'] = df['Rainfall_mm'].fillna(0)

# 2. Feature Engineering
df['Date'] = pd.to_datetime(df['Date'])
df['Day_of_Week'] = df['Date'].dt.dayofweek
df['Heat_Index'] = df['Temperature_C'] + (df['Humidity_Prc'] * 0.1)
df['Is_Rainy'] = (df['Rainfall_mm'] > 0).astype(int)

# 3. Encoding Categorical Variables
le = LabelEncoder()
df['WeatherCondition_Encoded'] = le.fit_transform(df['WeatherCondition'])

# 4. Feature Scaling (Standardization)
scaler = StandardScaler()
features_to_scale = ['Temperature_C', 'Humidity_Prc', 'WindSpeed_kmh', 'Heat_Index']
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# Save the processed data
df.to_csv('weather_clean_ready.csv', index=False)