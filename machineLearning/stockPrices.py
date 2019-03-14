import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')

# prints all the features. Can have as many features as you want, but
# make sure to have meaningful ones that actually have something to do with the data 
print(df.head())