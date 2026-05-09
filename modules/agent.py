import os
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_data(filepath="data/processed_data.csv"):
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    return df

def summarize_data(df):
    summary = {}
    for col in df.columns:
        summary[col] = {
            "Giá cuối": round(df[col].iloc[-1], 2),
            "Trung bình 30 ngày": round(df[col].tail(30).mean(), 2),
            "Độ lệch chuẩn": round(df[col].tail(30).std(), 2),
            "Tỷ suất sinh lời (%)": round(
                (df[col].iloc[-1] / df[col].iloc[0] - 1) * 100, 2
            ),
        }
    return summary

def run_agent(summary: dict) -> str:
    prompt = f"""Bạn là chuyên gia phân tích tài chính.
Dữ liệu thống kê S&P 500 và Vàng: {summary}
Hãy viết báo cáo tiếng Việt gồm:
1. Nhận xét xu hướng giá từng tài sản.
2. Đánh giá mức độ biến động.
3. Phân tích tương quan S&P 500 và Vàng.
4. Khuyến nghị phân bổ danh mục đầu tư.
Trích dẫn số liệu cụ thể trong phân tích."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response.choices[0].message.content

def save_report(report: str, output_path="data/ai_report.txt"):
    print("\n" + "="*60)
    print("BÁO CÁO PHÂN TÍCH TỪ AI")
    print("="*60)
    print(report)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nBáo cáo đã lưu tại: {output_path}")

if __name__ == "__main__":
    df = load_data()
    summary = summarize_data(df)
    report = run_agent(summary)
    save_report(report)