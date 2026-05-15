import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. THIẾT LẬP ĐƯỜNG DẪN & DỮ LIỆU ---
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)
file_path = os.path.join(base_dir, 'data', 'processed_data.csv')
save_dir = os.path.join(base_dir, 'visualizations')

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

try:
    # Sử dụng parse_dates để chuẩn hóa định dạng ngày ngay từ đầu
    df = pd.read_csv(file_path, parse_dates=['Date'])
    print(f"Success: Visualizer loaded data to {df['Date'].max().date()}")
except Exception as e:
    print(f"Error: {e}")
    exit()

sns.set_style("whitegrid")

# --- 2. CÁC HÀM VẼ BIỂU ĐỒ RIÊNG BIỆT ---

def plot_price_trends(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['SP500'], label='S&P 500', color='#1f77b4')
    plt.plot(df['Date'], df['Gold'], label='Gold', color='#ffd700')
    plt.title('1. Price Trends (S&P 500 vs Gold)', fontweight='bold')
    plt.legend()
    plt.savefig(os.path.join(save_dir, '1_price_trends.png'))
    plt.close()

def plot_correlation(df):
    plt.figure(figsize=(10, 8))
    corr_cols = ['SP500', 'Gold', 'SP500_Return', 'Gold_Return']
    # center=0 giúp hiện màu đỏ khi tương quan âm, rất quan trọng cho nhận định rủi ro
    sns.heatmap(df[corr_cols].corr(), annot=True, cmap='RdYlGn', center=0, fmt=".2f")
    plt.title('2. Correlation Matrix', fontweight='bold')
    plt.savefig(os.path.join(save_dir, '2_correlation.png'))
    plt.close()

def plot_return_dist(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(df['SP500_Return'], kde=True, color='#1f77b4', label='S&P 500', alpha=0.5)
    sns.histplot(df['Gold_Return'], kde=True, color='#ffd700', label='Gold', alpha=0.5)
    plt.title('3. Return Distribution', fontweight='bold')
    plt.legend()
    plt.savefig(os.path.join(save_dir, '3_return_distribution.png'))
    plt.close()

def plot_bollinger(df):
    plt.figure(figsize=(12, 6))
    window = 20
    ma = df['SP500'].rolling(window=window, min_periods=1).mean()
    std = df['SP500'].rolling(window=window, min_periods=1).std()
    upper = ma + (std * 2)
    lower = ma - (std * 2)
    plt.plot(df['Date'], df['SP500'], color='black', label='S&P 500 Price', linewidth=1)
    plt.plot(df['Date'], upper, 'r--', alpha=0.5, label='Upper Band')
    plt.plot(df['Date'], lower, 'g--', alpha=0.5, label='Lower Band')
    plt.fill_between(df['Date'], lower, upper, color='gray', alpha=0.1)
    plt.title('4. Bollinger Bands Analysis (S&P 500)', fontweight='bold')
    plt.legend()
    plt.savefig(os.path.join(save_dir, '4_bollinger_bands.png'))
    plt.close()

def plot_volatility_comparison(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['SP500_Vol'], label='S&P 500 Volatility', color='#1f77b4')
    plt.plot(df['Date'], df['Gold_Vol'], label='Gold Volatility', color='#ffd700')
    plt.title('5. Rolling Volatility Comparison (Risk Tracking)', fontweight='bold')
    plt.ylabel('Standard Deviation of Returns')
    plt.legend()
    plt.savefig(os.path.join(save_dir, '5_volatility_comparison.png'))
    plt.close()

def plot_drawdown(df):
    plt.figure(figsize=(12, 6))
    for col, color in zip(['SP500', 'Gold'], ['#1f77b4', '#ffd700']):
        rolling_max = df[col].cummax()
        drawdown = (df[col] - rolling_max) / rolling_max
        plt.fill_between(df['Date'], drawdown, 0, label=f'{col} Drawdown', color=color, alpha=0.3)
    plt.title('6. Drawdown Analysis (Market Risk)', fontweight='bold')
    plt.ylabel('Percentage Drop from Peak')
    plt.legend()
    plt.savefig(os.path.join(save_dir, '6_drawdown_analysis.png'))
    plt.close()

# --- 3. THỰC THI ---
if __name__ == "__main__":
    print("Đang khởi tạo và lưu 6 biểu đồ...")
    plot_price_trends(df)
    plot_correlation(df)
    plot_return_dist(df)
    plot_bollinger(df)
    plot_volatility_comparison(df)
    plot_drawdown(df)
    print(f"Hoàn thành! 6 biểu đồ đã được lưu vào: {save_dir}")