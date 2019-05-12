import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def graph_data(stock):

    stock_price_url =  'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data =[]
    split_src = source_code.split('\n')

    for line in split_src:
            split_line = line.split(',')
            if len(split_line) == 6:
                if 'values' not in line:
                    stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
    delimiter=','
    unpack=True,
    # %Y = full year (2019)
    # %y = partial year (19)
    # %m = number month (03)
    # %d = number day (12)
    # %H = hours
    # %M = minutes
    # %S = seconds
    # 12-12-2012
    # %m-%d-%Y
    converters={0: bytespdate2num('%Y%m%d')})

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Tesla graph')
    plt.legend()
    plt.show()




graph_data('TSLA')













