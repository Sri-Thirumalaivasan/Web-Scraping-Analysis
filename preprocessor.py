import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the scraped data
data = pd.read_csv('laptops_data.csv')

# Clean data
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)

print(data.head())
print(data.info())
print(data.columns)
print(data[['Price', 'Rating']].head())

# Normalize price and rating
data['Price'] = data['Price'].str.replace('₹', '').str.replace(',', '').astype(float)
scaler = MinMaxScaler()
data[['Price', 'Rating']] = scaler.fit_transform(data[['Price', 'Rating']])

# Save cleaned data
data.to_csv('cleaned_laptops_data.csv', index=False)
print("Cleaned data saved to cleaned_laptops_data.csv")
