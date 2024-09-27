import pandas as pd
from pathlib import Path

def load(filename, folder_path='/content/Spystat-Engine-Colab/data/clean/'):
    # Load the file directly
    file_path = Path(folder_path) / filename
    return pd.read_csv(file_path) if file_path.exists() else print(f"{filename} not found.")
