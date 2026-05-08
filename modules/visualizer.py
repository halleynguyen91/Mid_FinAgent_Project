import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- XỬ LÝ ĐƯỜNG DẪN HỆ THỐNG ---
# Lấy đường dẫn tuyệt đối đến thư mục chứa file visualizer.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Định vị thư mục gốc của dự án (thư mục cha của modules)
base_dir = os.path.dirname(current_dir)
# Kết nối đến file dữ liệu trong thư mục data
file_path = os.path.join(base_dir, 'data', 'processed_data.csv')

# --- ĐỌC DỮ LIỆU VỚI XỬ LÝ NGOẠI LỆ ---
try:
    df = pd.read_csv(file_path)
    print(f"Thành công: Đã tìm thấy dữ liệu tại {file_path}")
except FileNotFoundError:
    print("-" * 50)
    print(f"LỖI: Không tìm thấy file dữ liệu tại: {file_path}")
    print("HƯỚNG DẪN: Vui lòng chạy file 'modules/processor.py' trước để khởi tạo dữ liệu.")
    print("-" * 50)
    # Dừng chương trình nếu không có dữ liệu
    exit()

# --- CẤU HÌNH HIỂN THỊ BIỂU ĐỒ ---
plt.rcParams['figure.figsize'] = (16, 10)
sns.set_style("whitegrid") # Thêm lưới cho biểu đồ trông chuyên nghiệp hơn
fig, axes = plt.subplots(2, 2)
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# 1. BIỂU ĐỒ XU HƯỚNG GIÁ (Price Trends)
axes[0, 0].plot(df['Date'], df['SP500'], label='S&P 500', color='#1f77b4', linewidth=1.5)
axes[0, 0].plot(df['Date'], df['Gold'], label='Gold', color='#ffd700', linewidth=1.5)
axes[0, 0].set_title('1. Diễn biến giá S&P 500 và Vàng (2024-2026)', fontsize=12, fontweight='bold')
axes[0, 0].legend()
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. BẢN ĐỒ NHIỆT TƯƠNG QUAN (Correlation Heatmap)
corr_cols = ['SP500', 'Gold', 'SP500_Return', 'Gold_Return']
corr_matrix = df[corr_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', center=0, ax=axes[0, 1], fmt=".2f")
axes[0, 1].set_title('2. Ma trận tương quan tài sản', fontsize=12, fontweight='bold')

# 3. PHÂN PHỐI TỶ SUẤT SINH LỜI (Return Distribution)
sns.histplot(df['SP500_Return'], kde=True, color='#1f77b4', label='S&P 500', ax=axes[1, 0], alpha=0.5)
sns.histplot(df['Gold_Return'], kde=True, color='#ffd700', label='Gold', ax=axes[1, 0], alpha=0.5)
axes[1, 0].set_title('3. Phân phối tỷ suất sinh lời hàng ngày', fontsize=12, fontweight='bold')
axes[1, 0].legend()

# 4. DẢI BOLLINGER BANDS CHO S&P 500 (Volatility Analysis)
df['MA20'] = df['SP500'].rolling(window=20).mean()
df['STD20'] = df['SP500'].rolling(window=20).std()
df['Upper'] = df['MA20'] + (df['STD20'] * 2)
df['Lower'] = df['MA20'] - (df['STD20'] * 2)

axes[1, 1].plot(df['Date'], df['SP500'], color='black', label='Giá S&P 500', linewidth=1)
axes[1, 1].plot(df['Date'], df['Upper'], 'r--', alpha=0.5, label='Upper Band')
axes[1, 1].plot(df['Date'], df['Lower'], 'g--', alpha=0.5, label='Lower Band')
axes[1, 1].fill_between(df.index, df['Lower'], df['Upper'], color='gray', alpha=0.1)
axes[1, 1].set_title('4. Phân tích biến động Bollinger Bands', fontsize=12, fontweight='bold')
axes[1, 1].legend(loc='best', fontsize='small')
axes[1, 1].tick_params(axis='x', rotation=45)

# HIỂN THỊ KẾT QUẢ
print("Đang khởi tạo cửa sổ hiển thị biểu đồ...")
plt.show()