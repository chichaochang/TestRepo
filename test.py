import yfinance as yf

aapl = yf.Ticker("AAPL")

print(aapl.splits)