import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('data/processed_data.csv')

# --- 1. BIỂU ĐỒ 1: Xu hướng giá (Price Trend) ---
fig1 = px.line(df, x='Date', y=['SP500', 'Gold'], 
               title='Biểu đồ 1: Xu hướng biến động giá S&P 500 và Vàng')
fig1.show()

# --- 2. BIỂU ĐỒ 2: Bản đồ nhiệt tương quan (Correlation Heatmap) ---
plt.figure(figsize=(10, 6))
correlation_matrix = df[['SP500', 'Gold', 'SP500_Return', 'Gold_Return']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlGn', center=0)
plt.title('Biểu đồ 2: Bản đồ nhiệt tương quan tài sản (Correlation Heatmap)')
plt.show() 

# --- 3. BIỂU ĐỒ 3: Phân phối tỷ suất sinh lời (Histogram) ---
fig3 = px.histogram(df, x=['SP500_Return', 'Gold_Return'], 
                   marginal="box", barmode="overlay",
                   title='Biểu đồ 3: Phân phối tỷ suất sinh lời (Nhận diện rủi ro)')
fig3.show()

# --- 4. BIỂU ĐỒ 4: Dải Bollinger Bands (Bollinger Bands Analysis) ---
df['MA20'] = df['SP500'].rolling(window=20).mean()
df['STD20'] = df['SP500'].rolling(window=20).std()
df['Upper_Band'] = df['MA20'] + (df['STD20'] * 2)
df['Lower_Band'] = df['MA20'] - (df['STD20'] * 2)

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=df['Date'], y=df['SP500'], name='Giá S&P 500', line=dict(color='blue')))
fig4.add_trace(go.Scatter(x=df['Date'], y=df['Upper_Band'], name='Dải trên (Rủi ro)', line=dict(dash='dash', color='red')))
fig4.add_trace(go.Scatter(x=df['Date'], y=df['Lower_Band'], name='Dải dưới (Cơ hội)', line=dict(dash='dash', color='green')))
fig4.update_layout(title='Biểu đồ 4: Phân tích biến động Bollinger Bands (S&P 500)')
fig4.show()

print("Hoàn thành xuất 4 biểu đồ")