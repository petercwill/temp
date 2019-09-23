import pandas as pd
import re

prices = pd.read_csv('temp_rnn.csv')
info = pd.Series(prices.columns).iloc[1:].to_frame('M4id')
info['category'] = 'A'
info['category'].iloc[:50] = 'B'
info['Frequency'] = 4
info['Horizon'] = 8
info['SP'] = 'Quarterly'
info['StartingDate'] = '04-01-2001'
info.to_csv('./info.csv')

prices.drop('period',axis=1,inplace=True)
prices.columns = [re.sub(',',"",c) for c in prices.columns]
print(prices)
train = prices.T.iloc[:,:-8]
train.to_csv('./Train/Quarterly-train.csv')
test = prices.T.iloc[:,-8:]
test.to_csv('./Test/Quarterly-test.csv')
