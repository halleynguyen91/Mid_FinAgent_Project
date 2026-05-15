import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. THIẾT LẬP HỆ THỐNG ---
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
save_dir = os.path.join(base_dir, 'visualizations')
os.makedirs(save_dir, exist_ok=True)

# Đọc dữ liệu và thiết lập phong cách biểu đồ
df = pd.read_csv(os.path.join(base_dir, 'data', 'processed_data.csv'), parse_dates=['Date'])
sns.set_style("whitegrid")

def export_plot(name, title):
    plt.title(title, fontweight='bold', fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, f'{name}.png'))
    plt.close()

# --- 2. QUY TRÌNH XUẤT BIỂU ĐỒ (1-6) ---
def run_visualizer():
    # 1. Price Trends (S&P 500 vs Gold)
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['SP500'], label='S&P 500', color='#1f77b4')
    plt.plot(df['Date'], df['Gold'], label='Gold', color='#ffd700')
    plt.ylabel('Price (USD)')
    plt.legend()
    export_plot('1_price_trends', '1. Price Trends Comparison')

    # 2. Correlation Matrix
    plt.figure(figsize=(10, 8))
    corr_cols = ['SP500', 'Gold', 'SP500_Return', 'Gold_Return']
    sns.heatmap(df[corr_cols].corr(), annot=True, cmap='RdYlGn', center=0, fmt=".2f")
    export_plot('2_correlation', '2. Asset Correlation Matrix')

    # 3. Return Distribution
    plt.figure(figsize=(12, 6))
    sns.histplot(df['SP500_Return'], kde=True, color='#1f77b4', label='S&P 500', alpha=0.5)
    sns.histplot(df['Gold_Return'], kde=True, color='#ffd700', label='Gold', alpha=0.5)
    plt.xlabel('Daily Returns')
    plt.legend()
    export_plot('3_return_distribution', '3. Returns Distribution Analysis')

    # 4. Bollinger Bands Analysis (S&P 500)
    plt.figure(figsize=(12, 6))
    ma = df['SP500'].rolling(window=20).mean()
    std = df['SP500'].rolling(window=20).std()
    plt.plot(df['Date'], df['SP500'], color='black', label='S&P 500 Price', linewidth=1)
    plt.plot(df['Date'], ma + (std * 2), 'r--', alpha=0.6, label='Upper Band')
    plt.plot(df['Date'], ma - (std * 2), 'g--', alpha=0.6, label='Lower Band')
    plt.fill_between(df['Date'], ma - (std * 2), ma + (std * 2), color='gray', alpha=0.1)
    plt.legend()
    export_plot('4_bollinger_bands', '4. Bollinger Bands Technical Analysis')

    # 5. Volatility Comparison
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['SP500_Vol'], label='S&P 500 Vol', color='#1f77b4')
    plt.plot(df['Date'], df['Gold_Vol'], label='Gold Vol', color='#ffd700')
    plt.ylabel('Rolling Standard Deviation')
    plt.legend()
    export_plot('5_volatility_comparison', '5. Rolling Volatility (Risk Tracking)')

    # 6. Drawdown Analysis
    plt.figure(figsize=(12, 6))
    for col, color in zip(['SP500', 'Gold'], ['#1f77b4', '#ffd700']):
        peak = df[col].cummax()
        drawdown = (df[col] - peak) / peak
        plt.fill_between(df['Date'], drawdown, 0, label=f'{col} Drawdown', color=color, alpha=0.3)
    plt.ylabel('Percentage Drop from Peak')
    plt.legend()
    export_plot('6_drawdown_analysis', '6. Maximum Drawdown Analysis')

if __name__ == "__main__":
    print("Đang khởi tạo quy trình xuất biểu đồ...")
    run_visualizer()
    print(f"Hoàn thành! Tất cả biểu đồ đã được lưu tại: {save_dir}")