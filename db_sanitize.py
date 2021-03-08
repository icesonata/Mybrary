import numpy as np
import pandas as pd

df = pd.read_csv('bookdb/books.csv')

# Convert entries containing comma to integer format
df.voters = df.voters.apply(lambda x: x.replace(',', '') if ',' in str(x) else x)

# Remove entries having invalid ISBN number
df.ISBN = df.ISBN.apply(lambda x: np.NaN if not str(x).isnumeric() else x)

# Drop specific fields used in the application as database
# df = df.dropna(subset=df.columns[[11,1,2,13,3,4,9,7]], how='any')
subset = ['ISBN', 'title', 'author', 'published_date', 'rating', 'voters', 'page_count', 'description']
df = df.dropna(subset=subset, how='any')

# Remove duplicates
df = df.drop_duplicates(subset=['ISBN'])

# Export df to csv file
df.to_csv('bookdb/books.csv', index=False)