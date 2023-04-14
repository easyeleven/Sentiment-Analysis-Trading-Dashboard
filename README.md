# Sentiment-Analysis-Trading-Dashboard
This project is a sentiment analysis financial trading dashboard that allows users to select a stock or cryptocurrency and view its price data and news sentiment data. The dashboard uses Python, Streamlit, Pandas, yfinance, textblob, seaborn, matplotlib, and pycoingecko to gather and display the data. Users can select an asset type (stocks or crypto) and an asset from the sidebar, and view the price data and news sentiment data.

## Requirements
* Python 3.6 or later* Streamlit
* Pandas
* yfinance
* textblob
* seaborn
* matplotlib
* pycoingecko

## Setup
1. Clone the repository: `git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Replace `YOUR_API_KEY` in `sentiment_analysis_trading_dashboard.py` with your own News API key.

## Usage
1. Run the dashboard: `streamlit run sentiment_analysis_trading_dashboard.py`
2. Select an asset type (stocks or crypto) and an asset from the sidebar.
3. View the price data and news sentiment data.

## Deployment
1. Create an account on Streamlit Sharing.
2. Fork the repository on GitHub.
3. Create a new app on Streamlit Sharing.
4. Connect your forked repository to the app.
5. Set the build command to `streamlit run sentiment`
