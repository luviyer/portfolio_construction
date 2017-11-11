import pandas as pd


def clean_data(filename):
    df = pd.read_csv(filename, index_col=['LPERMNO', 'datadate'], parse_dates=True)
    df = df.unstack(level=0)
    df.fillna(method='ffill', inplace=True)

    return df

fundamentals = clean_data('fundamentals.csv')
# print(fundamentals)
# Let's calculate our value measure - the Book to Market Ratio
B2M = (fundamentals['atq'] - fundamentals['ltq']) / fundamentals['mkvaltq']
# print(B2M)

# Let's calculate our momentum scores
returns = clean_data('returns.csv')

# Sum the returns over the last year, and then subtract the return from the month before
MOM = returns['trt1m'].rolling(window=12).sum().shift(1) - returns['trt1m'].shift(1)

# print(MOM)

df = pd.concat({'B2M': B2M, 'MOM': MOM})

# Now, say we were just doing a value strategy, then we would now rank the assets based on Book to Market,
# with the highest B2M ratios signifying our value stocks
print(df.rank(axis=1))
# print(df.loc[:][df.rank(axis=1) >= 25])








# # print(df.index[0][:])
# mom_portfolio = {t: df.columns[df.loc[('MOM', t)].isnull()] for t in df.index[1]}
# mom_portfolio = pd.DataFrame(mom_portfolio)
# print(mom_portfolio)


