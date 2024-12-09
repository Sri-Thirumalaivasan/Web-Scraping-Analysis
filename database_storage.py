from sqlalchemy import create_engine
import pandas as pd

# Create SQLite database
data = pd.read_csv('cleaned_laptops_data.csv')
engine = create_engine('sqlite:///laptops.db')
data.to_sql('laptops', engine, index=False, if_exists='replace')
print("Data stored in SQLite database: laptops.db")
