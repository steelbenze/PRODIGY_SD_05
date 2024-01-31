import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape product information from the website
def scrape_products(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all product elements on the page
        products = soup.find_all('div', class_='product')

        # Create a list to store product information
        product_data = []

        # Iterate through each product element
        for product in products:
            # Extract product details such as name, price, and rating
            name = product.find('h2', class_='product-name').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            rating = product.find('span', class_='product-rating').text.strip()

            # Append the product information to the list
            product_data.append([name, price, rating])

        return product_data
    else:
        print("Failed to retrieve data from the website")
        return None

# Function to save product information to a CSV file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Rating']) # Header row
        writer.writerows(data)

if __name__ == "__main__":
    # URL of the e-commerce website to scrape
    url = 'https://example.com/products'

    # Scrape product information from the website
    product_data = scrape_products(url)

    if product_data:
        # Save product information to a CSV file
        save_to_csv(product_data, 'products.csv')
        print("Product information saved to products.csv")
