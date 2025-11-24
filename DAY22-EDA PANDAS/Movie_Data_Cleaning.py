import pandas as pd

# 1. Sample movie dataset
data = {
    'Title': ['Inception', 'Avatar', 'Inception', 'Titanic', 'Avatar'],
    'Genre': ['Sci-Fi', 'sci fi', 'Sci-Fi', 'Romance', 'SCI-FI'],
    'Year': [2010, 2009, 2010, 1997, 2009]
}

df = pd.DataFrame(data)
print("--- Original Dataset ---")
print(df)

# 2. Remove duplicate rows
df = df.drop_duplicates()
print("\n--- After Dropping Duplicates ---")
print(df)

# 3. Standardize the Genre column
df['Genre'] = df['Genre'].str.lower()            # convert to lowercase
df['Genre'] = df['Genre'].str.replace('-', ' ')  # replace hyphens with spaces
df['Genre'] = df['Genre'].str.replace('_', ' ')  # replace underscores with spaces
df['Genre'] = df['Genre'].str.strip()           # remove leading/trailing spaces

print("\n--- After Cleaning Genre Column ---")
print(df)
