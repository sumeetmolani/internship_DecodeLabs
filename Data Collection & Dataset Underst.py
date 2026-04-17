import pandas as pd # pyright: ignore[reportMissingModuleSource]

file_path = r"E:\decodelabs Data Science intership\Dataset for Data Analytics.xlsx"

try:
    df = pd.read_excel(file_path)
    print("--- Dataset Loaded Successfully ---\n")
    print(f"Dataset Shape: {df.shape}") 
    print(f"Columns: {df.columns.tolist()}\n") 
    print("--- Data Structure Information ---")
    print(df.info())
    print("\n")
    print("--- Statistical Summary ---")
    print(df.describe())
    print("\n--- Missing Values Count ---")
    print(df.isnull().sum())
except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}. Please check the folder[cite: 39].")
except Exception as e:
    print(f"An error occurred: {e}")