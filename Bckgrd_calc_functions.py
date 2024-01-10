import pandas as pd
import numpy as np

def read_filter_convert(file_path):
    # Read the CSV file
    data = pd.read_csv(file_path)

    # Filter out rows with all zero efficiencies
    filtered_data = data.iloc[1:].replace('0.00E+00', pd.NA).dropna(subset=data.columns[1:], how='all')

    # Convert the necessary columns to numeric, handling errors
    for col in filtered_data.columns:
        filtered_data[col] = pd.to_numeric(filtered_data[col], errors='coerce')

    return filtered_data


def calculate_background_noise(activity, mass, trendline_coeffs, thickness):
    a, b = trendline_coeffs  # a is the intercept, b is the slope
    hit_efficiency = a * np.exp(b * thickness)
    return activity *mass * hit_efficiency * 3.154e7 #conversion second to year


def find_nearest_index(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx
