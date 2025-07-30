# Time-Series-Stock-Visualizer

This is a simple Python project that loads stock price data from a CSV file,  
plots the daily closing price over time, and overlays a 7-day rolling average to smooth out fluctuations.

---

## Features

- Loads stock data CSV exported from Yahoo Finance or similar sources  
- Converts dates for accurate time-series plotting  
- Calculates 7-day rolling average of closing prices  
- Plots both raw closing prices and rolling averages using Matplotlib

---

## Requirements

- Python 3.x  
- pandas  
- matplotlib

Install dependencies with:  
```bash
pip install pandas matplotlib
python stock_visualizer.py
