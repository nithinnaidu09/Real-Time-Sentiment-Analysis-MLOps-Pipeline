import pandas as pd
import os

def load_and_clean_data(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    df.dropna(inplace=True)
    df['text'] = df['text'].str.replace(r'[^a-zA-Z\s]', '', regex=True)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print("Data saved to:", output_path)

if __name__ == "__main__":
    input_file = "data/raw/sentiment.csv"
    output_file = "data/processed/cleaned.csv"
    load_and_clean_data(input_file, output_file)