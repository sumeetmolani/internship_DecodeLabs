import pandas as pd # pyright: ignore[reportMissingModuleSource]

file_path = r"E:\decodelabs Data Science intership\Dataset for Data Analytics.xlsx"

try:
    df = pd.read_excel(file_path)
    print("--- Starting Data Cleaning ---\n")
    initial_rows = df.shape[0]
    df.drop_duplicates(inplace=True)
    print(f"Removed {initial_rows - df.shape[0]} duplicate rows.")
    numeric_cols = df.select_dtypes(include=['number']).columns
    non_numeric_cols = df.select_dtypes(exclude=['number']).columns
    for col in numeric_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].mean())
            print(f"Filled missing values in numeric column: {col}")
    for col in non_numeric_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna("Unknown")
            print(f"Filled missing values in text column: {col}")
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        print("Formatted 'Date' column to datetime.")
    print("\n--- Data Cleaning Complete ---")
    print(f"Final Dataset Shape: {df.shape}")
    output_path = r"E:\decodelabs Data Science intership\Cleaned_Dataset.xlsx"
    df.to_excel(output_path, index=False)
    print(f"Cleaned file saved as: {output_path}")
except Exception as e:
    print(f"An error occurred: {e}")