import numpy as np
import pandas as pd

df = pd.read_csv('bookdb/books.csv')

# Convert entries containing comma to integer format
df.voters = df.voters.apply(lambda x: x.replace(',', '') if ',' in str(x) else x)

# Remove entries having invalid ISBN number
df.isbn = df.isbn.apply(lambda x: np.NaN if not str(x).isnumeric() else x)

# Drop specific columns used in the application
df = df.dropna(subset=df.columns[[11,1,2,13,3,4,9,7]], how='any')

# Export df to csv file
df.to_csv('bookdb/books.csv', index=False)