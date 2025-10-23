import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(filepath):
    """Load and preprocess the dataset for GAN training."""
    data = pd.read_csv(filepath)  # <- utilise le paramètre

    # Drop unnecessary columns
    data_gan = data.drop(columns=['Date', 'App'])

    # Normalize the data
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data_gan)
    normalized_df = pd.DataFrame(normalized_data, columns=data_gan.columns)

    return normalized_df, scaler

if __name__ == "__main__":
    # Example usage
    data, scaler = preprocess_data(r"C:\Users\PC\Desktop\Synthetic-Data-Generation-with-Generative-AI-main\Synthetic-Data-Generation-with-Generative-AI-main\data\screentime_analysis.csv")
    print(data.head())
