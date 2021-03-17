import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

def Google():
    start = datetime.datetime(2021, 2, 1)
    end = datetime.datetime(2021, 3, 1)

    google = web.DataReader("GOOGL", 'yahoo', start, end)

    google['Open'].plot(label='Google Open Price', figsize=(15, 7))
    google['Close'].plot(label='Google Close Price')
    google['High'].plot(label='Google High Price')
    google['Low'].plot(label='Google Low Price')
    plt.legend()
    plt.title('Google Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.savefig('rich1.png')

def Tesla():
    start = datetime.datetime(2021, 2, 1)
    end = datetime.datetime(2021, 3, 1)

    yahoo = web.DataReader("TSLA", 'yahoo', start, end)

    yahoo['Open'].plot(label='Tesla Open Price', figsize=(15, 7))
    yahoo['Close'].plot(label='Tesla Close Price')
    yahoo['High'].plot(label='Tesla High Price')
    yahoo['Low'].plot(label='Tesla Low Price')
    plt.legend()
    plt.title('Tesla Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.savefig('rich2.png')
