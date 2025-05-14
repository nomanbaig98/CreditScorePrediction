import os
current_path = os.getcwd()
df_path = os.path.join(current_path, 'cleaned.csv')
model_path = os.path.join(current_path, 'final_pipeline.pkl.gz')
print("CSV exists:", os.path.exists(df_path))
print("Model exists:", os.path.exists(model_path))