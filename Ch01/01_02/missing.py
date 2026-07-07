# %%
import pandas as pd

# %%
# NaN - Not a Number
# NaT - Not a Time
df = pd.read_csv('cart.csv', parse_dates=['date'])
df
# %%
print("DataType\n",df.dtypes)

# %%
df['amount'].astype('Int32')

# %%
df.isnull()

# %%
# Linhas que possuem valores faltantes
df.isnull().any(axis=1)
# %%
