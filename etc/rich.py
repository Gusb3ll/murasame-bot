import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

def Google():
    start = datetime.datetime(2021, 2, 1)
    end = datetime.datetime(2021, 3, 1)

    google = web.DataReader("GOOGL", 'yahoo', start, end)

    google['Open'].plot(label='GOOGL Open Price', figsize=(15, 7))
    google['Close'].plot(label='GOOGL Close Price')
    google['High'].plot(label='GOOGL High Price')
    google['Low'].plot(label='GOOGL Low Price')
    plt.legend()
    plt.title('Google Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.savefig('rich.png')
