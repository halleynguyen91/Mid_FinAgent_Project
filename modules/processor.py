import pandas as pd
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)
raw_path = os.path.join(base_dir, 'data', 'raw_data.csv')
processed_path = os.path.join(base_dir, 'data', 'processed_data.csv')

def process_financial_data():
    try:
        # 1. Đọc và Chuẩn hóa định dạng (Normalization)
        df = pd.read_csv(raw_path)
        df['Date'] = pd.to_datetime(df['Date'])
        df.drop_duplicates(inplace=True)
        df.sort_values('Date', inplace=True)
        
        # 2. Xử lý dữ liệu thiếu (Forward-fill) & Xử lý giá trị ngoại lai (Outliers)
        for col in ['Gold', 'SP500']:
            q_low = df[col].quantile(0.01)
            q_hi  = df[col].quantile(0.99)
            df[col] = df[col].clip(lower=q_low, upper=q_hi)
        df.fillna(method='ffill', inplace=True)

        # 3. Kỹ thuật đặc trưng (Feature Engineering)
        df['Gold_Return'] = df['Gold'].pct_change()
        df['SP500_Return'] = df['SP500'].pct_change()

        # 4. Tính trung bình trượt (7 ngày và 30 ngày) & Độ biến động (Volatility)
        df['SP500_MA7'] = df['SP500'].rolling(window=7, min_periods=1).mean()
        df['SP500_MA30'] = df['SP500'].rolling(window=30, min_periods=1).mean()
        df['SP500_Vol'] = df['SP500_Return'].rolling(window=30, min_periods=1).std()
        df['Gold_Vol'] = df['Gold_Return'].rolling(window=30, min_periods=1).std()

        # 5. Lưu dữ liệu đã xử lý
        df.dropna(subset=['Gold_Return', 'SP500_Return'], inplace=True)
        df.to_csv(processed_path, index=False)
        
        print(f"Success: Updated to {df['Date'].max().date()}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    process_financial_data()