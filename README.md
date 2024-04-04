# GlassesShop Bestsellers Webscraping

This repository contains a Scrapy project for scraping bestsellers eye glasses data from GlassesShop.com. GlassesShop is a brand that sells trending eye glasses, and this project aims to extract information about the bestsellers eye glasses available on their website.

## Project Overview
The goal of this project is to collect data on the bestsellers eye glasses from GlassesShop.com using web scraping techniques. The data includes the name of the glasses, price, image, and link to the glasses.

## Technologies Used
- Python
- Scrapy
- MongoDB
- CSV
- JSON

## Scraping Process
1. Scrapy Setup: Set up a Scrapy project with appropriate settings and folder structure.

2. Spider Creation: Created a spider named "glasses" to crawl the GlassesShop website.

3. Pagination Handling: Implemented pagination rules to scrape multiple pages of bestsellers eye glasses.

4. Data Extraction: Used XPath selectors to extract relevant information such as glass name, price, image URL, and product link.

5. Data Storage: Stored the extracted data in both CSV and JSON formats for easy accessibility.

6. Database Integration: Saved the scraped data into a MongoDB database for further analysis and storage.

## Usage
To run the web scraping script:

1. Clone this repository to your local machine.

2. Install the required dependencies by running pip install -r requirements.txt.

3. Navigate to the project directory and run the Scrapy spider using the command scrapy crawl glasses.

4. The scraped data will be saved in both CSV and JSON files.

5. Additionally, the data will be stored in a MongoDB database for further usage.

## Conclusion
This project successfully scraped bestsellers eye glasses data from GlassesShop.com using Scrapy. The scraped data is stored in various formats, including CSV, JSON, and MongoDB, allowing for easy access and analysis. Further enhancements could include additional data attributes extraction or improving data storage and retrieval mechanisms.

### website view

![image](https://github.com/FaeyO/webscrapping-glassesshop.com-website/assets/118575325/27d85a12-7c19-4317-9e2d-724efe27dafe)
