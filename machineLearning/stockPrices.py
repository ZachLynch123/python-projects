import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')

# prints all the features. Can have as many features as you want, but
# make sure to have meaningful ones that actually have something to do with the data 

# df = dataFrame
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

# Take
forecast_col_close = 'Adj. Close'

df.fillna(-9999, inplace=True)
