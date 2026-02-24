# Weather Data Preprocessing Pipeline

This repository contains the automation script for cleaning and engineering features from raw weather data.

## Features
- **Missing Data**: Mean imputation for Temperature; Constant (0) for Rainfall.
- **Engineering**: Created `Heat_Index` (Interaction) and `Is_Rainy` (Binary).
- **Transformation**: Label Encoding for weather conditions.
- **Scaling**: Standardized numerical features using StandardScaler.

## Instructions
1. Run `pip install -r requirements.txt`
2. Run `python weather_l3_preprocess.py`