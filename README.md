# WebScrapper
The Web Scraping App is a Python application that allows users to scrape data from a website and save it in different formats, including CSV, Excel, and JSON. This app is designed to simplify the process of web scraping and data extraction for users who want to collect structured data from web pages.
Certainly! Here's a description and documentation for the web scraping app:

## Web Scraping App Documentation

### Features

1. **Web Scraping**: The app sends an HTTP GET request to the specified URL and uses the BeautifulSoup library to parse the HTML content of the web page.

2. **Data Extraction**: It extracts data from the web page based on specified HTML tags and class attributes. In the provided example, it extracts book titles, prices, and links from the "https://books.toscrape.com/" website.

3. **Data Export**: The app provides options to export the scraped data in three different formats:
   - CSV: Data is saved in a comma-separated values (CSV) file.
   - Excel: Data is saved in an Excel (.xlsx) file.
   - JSON: Data is saved in a JSON file.

4. **Encoding**: Data is saved with UTF-8 encoding to handle non-ASCII characters.

### Prerequisites

Before using the Web Scraping App, ensure that you have the following installed:

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`, `pandas`, `json`, `csv`, `openpyxl`

You can install these packages using `pip` if they are not already installed:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

### Usage

1. **Clone the Repository**: Clone the repository containing the Web Scraping App code to your local machine.

2. **Run the App**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the app code is located.
   - Run the Python script by executing the following command:

     ```bash
     python app.py
     ```

3. **Input the URL**: The app will prompt you to input the URL of the website you want to scrape. Provide the URL and press Enter.

4. **Data Extraction**: The app will scrape the data from the specified website based on the code provided in the script. In the example provided, it extracts book titles, prices, and links.

5. **Data Export**: The scraped data will be saved in three different formats (CSV, Excel, and JSON) in the same directory as the app script. The files will be named 'books.csv', 'books.xlsx', and 'books.json'.

6. **Completion**: Once the data is saved, the app will display messages indicating that the data has been successfully saved in the respective files.

### Customization

You can customize the app to scrape different data from different websites by modifying the code in the Python script. Specifically, you can change the website URL and adjust the data extraction code to meet your specific requirements.

### Notes

- Always ensure that you have the necessary permissions to scrape data from a website. Be respectful of website terms of service and robots.txt rules.
- Web scraping can put a load on the website's server. Please be considerate and avoid scraping large amounts of data rapidly.

### Disclaimer

This app is provided as an educational tool and for personal use. Users are responsible for complying with all legal and ethical guidelines related to web scraping and data collection. The developers of this app are not responsible for any misuse of the tool.

### Feedback and Support

If you encounter issues or have questions about the Web Scraping App, feel free to reach out to us for support or provide feedback for future improvements.
