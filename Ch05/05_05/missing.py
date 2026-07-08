# %%
import pandas as pd


df = pd.read_csv('cart.csv', parse_dates=['date'])
df

# %% 
# df['amount'].fillna(1, inplace=True)
df.fillna({'amount': 1}, inplace=True)
df

# %%
most_common = df['name'].mode()[0]
# df['name'].fillna(most_common, inplace=True)
df['name'] = df['name'].fillna(most_common)

df

# %%
# df['date'].fillna(method='ffill', inplace=True)
df['date'] = df['date'].ffill()
df

# %%
import numpy as np
prices = df.groupby('name')['price'].transform(np.mean)
prices

# %%
# df['price'].fillna(prices, inplace=True)
df['price'] = df['price'].fillna(prices)
df
# %%
