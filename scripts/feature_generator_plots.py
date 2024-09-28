# plots.py
import matplotlib.pyplot as plt

def plot_spy_moving_averages(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['SPY_Close'], label='SPY Close', color='blue')
    plt.plot(data['Date'], data['SPY_5_MA_Close'], label='5-Day MA', color='orange', linestyle='--')
    plt.plot(data['Date'], data['SPY_20_MA_Close'], label='20-Day MA', color='green', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('SPY Close Prices with 5-Day and 20-Day Moving Averages')
    plt.legend()
    plt.show()

def plot_spy_oscillators_and_volume_z_scores(data):
    plt.figure(figsize=(12, 8))
    plt.plot(data['Date'], data['SPY_Oscillator_5'], label='SPY 5-Day Oscillator', color='blue', linestyle='--')
    plt.plot(data['Date'], data['SPY_Oscillator_20'], label='SPY 20-Day Oscillator', color='green', linestyle='--')
    plt.plot(data['Date'], data['SPY_Volume_Z_5'], label='5-Period Z-Score of SPY Volume', color='red', alpha=0.6)
    plt.plot(data['Date'], data['SPY_Volume_Z_20'], label='20-Period Z-Score of SPY Volume', color='orange', alpha=0.6)
    plt.xlabel('Date')
    plt.ylabel('Oscillator (%) / Volume Z-Score')
    plt.title('SPY Oscillators and Volume Z-Scores')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_spy_percent_close_change(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['SPY_Percent_Close_Change'], label="Percent Change in SPY Close", color='red')
    plt.title('Percent Change in SPY Close Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Percent Change (%)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_spy_percent_high_to_previous_close(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['SPY_Percent_Change:High_To_Previous_Close'], label="SPY Percent High Change", color='red')
    plt.title('Percent Change of High to Previous Close Over Time')
    plt.xlabel('Date')
    plt.ylabel('Percent Change (%)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_spy_percent_low_to_previous_close(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['SPY_Percent_Change:Low_To_Previous_Close'], label="SPY Percent Low Change", color='red')
    plt.title('Percent Change of Low to Previous Close Over Time')
    plt.xlabel('Date')
    plt.ylabel('Percent Change (%)')
    plt.legend()
    plt.grid(True)
    plt.show()
