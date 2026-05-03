import yfinance as yf
import pandas as pd
import os

def fetch_financial_data(tickers=["^GSPC", "GC=F"], start_date="2024-01-01"):
    print(f"Đang tải dữ liệu cho các mã: {tickers}...")
    
    # Tải dữ liệu giá đóng cửa
    data = yf.download(tickers, start=start_date)['Close']
    
    # Đổi tên cột cho dễ xử lý và trực quan
    data.columns = ['Gold', 'SP500']
    
    # Tạo thư mục data nếu chưa có
    if not os.path.exists('data'):
        os.makedirs('data')
        
    # Lưu ra file CSV thô
    data.to_csv("data/raw_data.csv")
    print("Đã tải xong và lưu dữ liệu vào data/raw_data.csv!")
    return data

if __name__ == "__main__":
    fetch_financial_data()