from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Configure Selenium WebDriver
service = Service("C:\\Users\\stvas\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")  # Replace with the path to your ChromeDriver
driver = webdriver.Chrome(service=service)

# Open the target website
url = "https://www.flipkart.com/search?q=laptops"
driver.get(url)
time.sleep(2)  # Wait for page to load

# Scrape data
products = []
prices = []
ratings = []

# Extract product details
try:
    product_names = driver.find_elements(By.CLASS_NAME, '_4rR01T')  # Replace with actual class
    product_prices = driver.find_elements(By.CLASS_NAME, '_30jeq3')  # Replace with actual class
    product_ratings = driver.find_elements(By.CLASS_NAME, '_3LWZlK')  # Replace with actual class

    for name, price, rating in zip(product_names, product_prices, product_ratings):
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)
except Exception as e:
    print(f"Error during scraping: {e}")

# Close the browser
driver.quit()

# Save data to a CSV
data = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
data.to_csv('laptops_data.csv', index=False)
print("Data saved to laptops_data.csv")
