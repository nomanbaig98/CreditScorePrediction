import os
import gzip
import pickle
import pandas as pd

# Get the directory where the current script lives
script_dir = os.path.dirname(os.path.abspath(__file__))

# Relative paths to CSV and model from the script location
df_path = os.path.join(script_dir, 'cleaned.csv')
model_path = os.path.join(script_dir, 'final_pipeline.pkl.gz')

# Print paths being checked
print("Looking for CSV at:", df_path)
print("Looking for model at:", model_path)

# Load data
try:
    data = pd.read_csv(df_path)
    print("✅ CSV loaded successfully.")
except FileNotFoundError:
    print("❌ CSV file not found. Ensure it's in the same folder as this script.")

# Load model
try:
    with gzip.open(model_path, 'rb') as file:
        model = pickle.load(file)
    print("✅ Model loaded successfully.")
except FileNotFoundError:
    print("❌ Model file not found. Ensure it's in the same folder as this script.")
