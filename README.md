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
## 📂 Project Structure
- `data/`: Contains raw and processed CSV files and AI reports.
- `modules/`: Core logic of the application.
  - `data_loader.py`: Fetches real-time data from Yahoo Finance.
  - `processor.py`: Cleans data and calculates financial metrics.
  - `visualizer.py`: Generates technical analysis charts.
  - `agent.py`: AI-powered risk analysis using Groq Cloud.
- `.env`: Stores sensitive API keys (Environment variables).
- `requirements.txt`: List of necessary Python libraries.
- `main.py`: Full code to run

## Workflow & Execution Guide
To run the full pipeline, please execute the scripts in the following order:

# Step 1: Data Collection
    Command: python modules/data_loader.py
    
    Technical Details:
- Source: The system utilizes the yfinance library to establish a secure connection with Yahoo Finance API.
- Assets Tracked: * S&P 500 (^GSPC): Representing the benchmark for the US Equity market.
- Gold (GC=F): Representing the primary safe-haven asset in the commodities market.

    Timeframe: Automatically fetches historical daily data from January 1st, 2024, up to the current live date (Real-time synchronization).
    
    Mechanism: 
1.  The script validates the connection to the financial servers.
2.  It extracts Adjusted Closing Prices to account for corporate actions (splits/dividends).
3.  Output: Saves the raw dataset as data/raw_data.csv for the next stage of processing.

# Step 2: Data Processing
    Command: python modules/processor.py 
    
    Technical Details:
Mechanism: 
1. The script loads the data/raw_data.csv and initiates a cleaning pipeline to handle missing values via forward-fill (FFill) and removes any duplicate records. 
2. It normalizes date formats and ensures all numerical data is correctly typed for time-series analysis.

Feature Engineering:
- Performance Metrics: Calculates daily percentage returns for both assets (SP500_Return and Gold_Return).
- Trend Indicators: Computes 7-day (SP500_MA7) and 30-day (SP500_MA30) simple moving averages to identify price momentum and trends.
- Risk Assessment: Derives the rolling standard deviation for the S&P 500 (SP500_Vol) and Gold (Gold_Vol) to measure market volatility and asset risk.
- Output: Saves the enriched dataset as data/processed_data.csv.


# Step 3: Visualization
    Command: python modules/visualizer.py 
    Technical Details:
- Library Stack: Utilizes Matplotlib for core plotting, Seaborn for advanced statistical aesthetics, and the os library for robust absolute path management across different operating systems.
- System Design:  Dynamic Path Resolution: Automatically detects the project's base directory to locate data/processed_data.csv regardless of where the script is executed.
- Exception Handling: Includes a built-in validation system that alerts the user and provides instructions if the required dataset is missing.

    Dashboard Inventory (2x2 Grid):
1. Price Trend Analysis: A synchronized line chart displaying the price trajectory of the S&P 500 (Blue) and Gold (Yellow) for the 2024-2026 period.
2. Correlation Heatmap: A RdYlGn (Red-Yellow-Green) color-coded matrix measuring the statistical correlation between asset prices and daily returns.
3. Return Distribution: A combined Histogram and Kernel Density Estimation (KDE) plot comparing the risk-reward profiles of both assets.
4. Bollinger Bands Volatility Analysis: Dynamically calculates 20-day Moving Averages and Standard Deviations to visualize market expansion, contraction, and potential breakout zones for the S&P 500.

Output: Renders an interactive 16x10 inch multi-panel dashboard directly within the VS Code environment for professional financial reporting.


# Step 4: AI Insights (In Development)
    Command: python modules/agent.py

    Technical Details:
Engine: Powered by the Llama-3.3-70b model via Groq Cloud API for high-speed, professional-grade financial reasoning.
Context Integration: The agent doesn't just "chat"; it consumes a structured dictionary of statistical metrics (Mean, Standard Deviation, and Returns) calculated in the previous steps.

    Quantitative Reasoning: 
- Correlation Analysis: Automatically interprets the Correlation Coefficient to assess diversification benefits.
- Risk Evaluation: Analyzes volatility clusters to determine if the market is in a "Risk-On" or "Risk-Off" phase.

    Multilingual Output: Generates a comprehensive investment report in Vietnamese, bridging the gap between complex data and actionable insights.
    
    Output: Generates data/ai_report.txt, providing strategic asset allocation recommendations for different investor profiles (Short-term vs. Long-term).


## 📊 Key Features & Achievements
Real-time Data Integration: Uses yfinance to synchronize accurate market prices.

Professional Visualization: Interactive charts demonstrating the inverse correlation between Gold and Stocks.

Risk Identification: Technical analysis using Bollinger Bands and volatility metrics to identify market entries and exits.

AI-Powered Reasoning: An AI Agent capable of interpreting complex financial charts and providing natural language reports.