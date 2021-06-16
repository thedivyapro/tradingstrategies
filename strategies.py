import pandas as pd
import pandas_ta as ta
def resample(data,tf):
    data = data.resample(str(tf)+"T").agg({'open': 'first','high': 'max','low': 'min','close': 'last','volume': 'max'})
    return data
def sma(data,l):
    sma = pd.DataFrame()
    sma['SMA'] = ta.sma(data["close"], length=l, suffix="SMA")
    sma['SMA'] = round(sma['SMA'],2)
    return sma
def ema(data,l):
    ema = pd.DataFrame()
    ema['EMA'] = ta.ema(ta.ohlc4(data["open"], data["high"], data["low"], data["close"]), length=l)
    ema['EMA'] = round(ema['EMA'],2)
    return ema
def wma(data,l):
    wma = pd.DataFrame()
    wma['WMA'] = ta.wma(data["close"], length=l)
    wma['WMA'] = round(wma['WMA'],2)
    return wma
def vwap(data):
    vwap = pd.DataFrame()
    vwap['VWAP'] = ta.vwap(data["high"],data["low"],data["close"],data["volume"])
    vwap['VWAP'] = round(vwap['VWAP'],2)
    return vwap
def rsi(data,l):
    rsi = pd.DataFrame()
    rsi['RSI'] = ta.rsi(data["close"], length=l)
    rsi['RSI'] = round(rsi['RSI'],2)
    return rsi