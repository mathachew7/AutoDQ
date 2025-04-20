import os 
import pandas as pd

# Define the datasets folder path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, 'datasets')

def load_datasets():
    print("🔍 Scanning dataset folder...")
    files = [f for f in os.listdir(DATASET_DIR) if f.endswith(('.csv', '.xlsx'))]

    if not files:
        print("⚠️ No dataset files found.")
        return

    for file in files:
        file_path = os.path.join(DATASET_DIR, file)
        print(f"📄 Loading file: {file}")
        try:
            if file.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file.endswith('.xlsx'):
                df = pd.read_excel(file_path)
            else:
                print(f"❌ Unsupported format: {file}")
                continue

            print(f"✅ Loaded {file} with {df.shape[0]} rows and {df.shape[1]} columns.")
            print(df.head(2))  # preview the first 2 rows
        except Exception as e:
            print(f"❌ Error loading {file}: {e}")

if __name__ == "__main__":
    load_datasets()

