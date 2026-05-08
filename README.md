# 📈 Mid-Term Project: Financial AI Agent

## 📝 Project Overview
This project is an **Automated Financial Analysis and Market Risk Assessment System**. It focuses on analyzing the real-time relationship between the **S&P 500 Index** (Equity) and **Gold** (Safe-haven asset) for the period 2024–2026. The system leverages AI to generate strategic risk insights and investment commentary based on live market data.

## 👥 Team Members & Contributions
*   **Hân:** Data Collection (`data_loader.py`), GitHub Repository Management, and Environment Setup.
*   **Thuy Duong:** Data Processing (`processor.py`) and Financial Data Visualization (`visualizer.py`).
*   **Anh Duong:** AI Integration and Risk Analysis Agent (`agent.py`).

## 🛠 System Requirements
Ensure you have Python 3.x installed, then install the required libraries:
```bash
pip install -r requirements.txt
```

## Workflow & Execution Guide
To run the full pipeline, please execute the scripts in the following order:

Step 1: Data Collection
    Fetch the latest real-time data from Yahoo Finance:
     python modules/data_loader.py

Step 2: Data Processing
    Clean data and calculate financial indicators (Returns, Moving Averages):
        python modules/processor.py

Step 3: Visualization
    Generate 4 key financial charts (Trends, Correlation Heatmap, Return Distribution, and Bollinger Bands) directly in VS Code:
        python modules/visualizer.py

Step 4: AI Insights (In Development)
    Connect to the AI Agent for automated market commentary and risk assessment:
        python modules/agent.py

## 📊 Key Features & Achievements
Real-time Data Integration: Uses yfinance to synchronize accurate market prices.

Professional Visualization: Interactive charts demonstrating the inverse correlation between Gold and Stocks.

Risk Identification: Technical analysis using Bollinger Bands and volatility metrics to identify market entries and exits.

AI-Powered Reasoning: An AI Agent capable of interpreting complex financial charts and providing natural language reports.