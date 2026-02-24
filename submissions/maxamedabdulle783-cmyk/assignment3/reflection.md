--

### 4. Technical Rationale (`reflection.md`)
# Reflection: Data Preprocessing Pipeline

This document explains the rationale behind the key decisions made during the preprocessing of the weather dataset.

## 1. Handling Missing Values (Imputation)
- **Temperature_C (Mean)**: Temperature generally follows a consistent pattern without extreme frequent spikes, making the mean a reliable representative for missing values.
- **Rainfall_mm (Zero/Mode)**: For records where the condition is 'Sunny', missing rainfall is set to 0 to maintain physical reality.

## 2. Feature Engineering
- **Heat_Index**: An interaction feature combining temperature and humidity to capture the "real feel" of the weather.
- **Day_of_Week**: Extracted from the date to help models identify cyclical weekly weather patterns.
- **Is_Rainy**: A binary classification helper to simplify the detection of precipitation events.

## 3. Scaling and Encoding
- **Standardization**: Applied to continuous features like `WindSpeed` and `Humidity` to ensure zero mean and unit variance, preventing features with larger scales from dominating the model.
- **Label Encoding**: Transformed the `WeatherCondition` text into numerical format to enable compatibility with mathematical algorithms.