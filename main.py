from strategies import *
import pandas as pd
sma_length = int(input("Enter the length of SMA (Recommended: 21): "))
ema_length = int(input("Enter the length of EMA (Recommended: 21): "))
wma_length = int(input("Enter the length of WMA (Recommended: 21): "))
rsi_length = int(input("Enter the length of RSI (Recommended: 21): "))
macd_vals = eval(input("Enter the [fast,slow] of MACD (Recommended: [8,21]): "))
data = pd.read_csv("NIFTY.csv", parse_dates =["dateTime"], index_col ="dateTime")
r = resample(data,3)        # Resample OHLCV DataFrame
rsi = rsi(r,rsi_length)     # RSI - Relative Strength Index
r['RSI{}'.format(rsi_length)] = rsi['RSI']
vwap = vwap(r)              # VWAP - Volume Weighted Average Price
r['VWAP'] = vwap['VWAP']
sma = sma(r,sma_length)     # SMA - Simple Moving Average
r['SMA{}'.format(sma_length)] = sma['SMA']
ema = ema(r,ema_length)     # EMA - Exponential Moving Average
r['EMA{}'.format(ema_length)] = ema['EMA']
wma = wma(r,wma_length)     # WMA - Weighted Moving Average
r['WMA{}'.format(wma_length)] = wma['WMA']
f =  int(macd_vals[0])    # MACD - Moving Average Convergence Divergence
s =  int(macd_vals[-1])
macd = macd(r,f,s)
r['MACD{}_{}'.format(macd_vals[0],macd_vals[-1])] = macd['MACD_{}_{}_9'.format(macd_vals[0],macd_vals[-1])]
r.reset_index(drop=False, inplace=True) # Resetting Index
print(r)
r.to_csv("ta-thp.csv", index=False) # Printing DataFrame to CSV
print("TA is successfully shipped to CSV file.")