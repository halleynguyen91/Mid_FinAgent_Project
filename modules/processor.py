import pandas as pd
import numpy as np

# 1. Đọc và Chuẩn hóa định dạng (Normalization)
df = pd.read_csv('data/raw_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.drop_duplicates(inplace=True)
df.sort_values('Date', inplace=True)

# 2. Xử lý dữ liệu thiếu (Forward-fill) & Xử lý giá trị ngoại lai (Outliers)
df.fillna(method='ffill', inplace=True)
for col in ['Gold', 'SP500']:
    q_low = df[col].quantile(0.01)
    q_hi  = df[col].quantile(0.99)
    df = df[(df[col] < q_hi) & (df[col] > q_low)]

# 3. Kỹ thuật đặc trưng (Feature Engineering)
# Tính tỷ suất sinh lời hàng ngày
df['Gold_Return'] = df['Gold'].pct_change()
df['SP500_Return'] = df['SP500'].pct_change()

# Tính trung bình trượt (7 ngày và 30 ngày)
df['SP500_MA7'] = df['SP500'].rolling(window=7).mean()
df['SP500_MA30'] = df['SP500'].rolling(window=30).mean()

# Tính độ biến động (Volatility - Rolling 30 days)
df['SP500_Vol'] = df['SP500_Return'].rolling(window=30).std()

# 4. Lưu dữ liệu đã xử lý
df.dropna(inplace=True)
df.to_csv('data/processed_data.csv', index=False)
print("Đã hoàn thành làm sạch và xử lý dữ liệu!")