# Forcaster 
import trade
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np


def main():
    now = datetime.datetime.now()
    today = ("%4s-%2s-%02d" %(now.strftime("%Y"),now.strftime("%m"),int(now.strftime("%d")) - 1))
    start_date = "2015-01-02"
    trade.check_data(today)
    symbols = ['SPY']
    stock = (raw_input("Which stock do you want to analyze? "))
    symbols.append(stock)
    dates = pd.date_range(start_date,today)
    df = trade.get_data(symbols,dates)
    sharpe_ratio,cumulative_returns,average_daily_returns,std_daily_returns = trade.sharpe_ratio(df,stock,start_date, today)
    print sharpe_ratio
    print cumulative_returns
    print average_daily_returns
    print std_daily_returns
    rm,upper_band,lower_band = trade.get_bollinger_bands(stock,df[stock],20,False)
    rm = pd.DataFrame(rm)
    rm = rm.rename(columns={stock:"rm"})
    df = df.join(rm)
    upper_band = pd.DataFrame(upper_band)
    upper_band = upper_band.rename(columns={stock:"upper_band"})
    df = df.join(upper_band)
    lower_band = pd.DataFrame(lower_band)
    lower_band = lower_band.rename(columns={stock:"lower_band"})
    df = df.join(lower_band)
    df = df.dropna(subset=["rm"])
    buy_price = 100
    sell_price = 120
    df['sell_points'] = (df[stock] >= sell_price).astype(int)
    df['buy_points'] = (df[stock] <= buy_price).astype(int)

    #trade.plot_data(df)
    graph_close(df,stock)

def graph_close(df,symbol):
    past_year = df[symbol][252:]
    df[symbol].hist(bins=20,label = symbol)
    past_year.hist(bins=20,label = "Past Year")
    plt.legend(loc="upper right")
    past_year_mean = past_year.mean()
    past_year_std = past_year.std()
    mean = df[symbol].mean()
    print "mean = " + str(mean)
    std = df[symbol].std()
    print("std = " + str(std))
    #simplify with func
    plt.axvline(mean,color='w',linestyle="dashed",linewidth=2)
    plt.axvline(std + mean,color='r',linestyle="dashed",linewidth=2)
    plt.axvline(-std + mean,color='r',linestyle="dashed",linewidth=2)
    plt.axvline(past_year_mean,color='w',linewidth=2)
    plt.axvline(past_year_std + past_year_mean,color='r',linewidth=2)
    plt.axvline(-past_year_std + past_year_mean,color='r',linewidth=2)
    plt.axvline(df[symbol][-1],color='g',linewidth=2)
    print df.kurtosis()
    plt.show()

def scatter_plot(symbol,symbols,dates):
    df= trade.get_data(symbols,dates)
    daily_returns = trade.compute_daily_returns(df)
    daily_returns.plot(kind='scatter',x='SPY',y=symbol)
    beta_symbol,alpha_symbol = np.polyfit(daily_returns['SPY'],daily_returns[symbol],1)
    plt.plot(daily_returns['SPY'], beta_symbol*daily_returns['SPY'] + alpha_symbol, '-',color='r')
    print "alpha of symbol: " , alpha_symbol
    print "beta of symbol: " , beta_symbol
    print daily_returns.corr(method='pearson')
def brian_price(symbol):
    if symbol == "AAPL":
        buy_price = 100
        sell_price = 130

    #plt.show()
if __name__ == "__main__":
    main()
