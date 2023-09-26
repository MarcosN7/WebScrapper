import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import csv

# Define the URL of the website you want to scrape
url = "https://books.toscrape.com/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data from the page
    # Find all book containers
    book_containers = soup.find_all('article', class_='product_pod')
    
    # Create a list to store the data
    data = []
    
    # Loop through each book container and extract the data
    for book in book_containers:
        # Extract the book title
        title = book.h3.a['title']
        
        # Extract the book price
        price = book.select('div p.price_color')[0].text
        
        # Extract the book link
        book_link = url + 'catalogue' + book.h3.a['href'][8:]
        
        # Append the data to the list
        data.append([title, price, book_link])
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=["Title", "Price", "Link"])
    
    # Save the data to CSV
    df.to_csv('books.csv', index=False, encoding='utf-8')
    print("Scraped data has been saved to 'books.csv'.")

    # Save the data to Excel with UTF-8 encoding using openpyxl
    df.to_excel('books.xlsx', index=False, engine='openpyxl')
    print("Scraped data has been saved to 'books.xlsx'.")

    # Save the data to JSON
    json_data = df.to_json(orient='records', force_ascii=False)
    with open('books.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)
    print("Scraped data has been saved to 'books.json'.")
    
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
