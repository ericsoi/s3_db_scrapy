# **ScrapyMySQL: Web Scraping and Data Storage into MySQL Database**

ScrapyMySQL is a Python-based web scraping project that allows you to efficiently scrape data from websites and store it directly into a MySQL database. This repository provides you with a ready-to-use framework for building web scraping bots using the Scrapy library and seamlessly saving the extracted data into a MySQL database.

## Features
- **Easy Setup:** Get started quickly with a well-organized Scrapy project structure and MySQL integration.
- **Flexible Scraping:** Customize and configure your web scraping targets using Scrapy's powerful features.
- **Efficient Data Storage:** Automatically save scraped data into a MySQL database for easy storage and retrieval.
- **Robust and Reliable:** Handle website changes gracefully and maintain data integrity with error handling and retry mechanisms.

## Getting Started
Follow these steps to set up and run the ScrapyMySQL project:

1. **Clone the Repository:**
    ```
        git clone https://github.com/ericsoi/ScrapySQL.git
        cd ScrapySQL
    ```
2. **Install Dependencies**
    ```
        pip install -e requirements.txt
    ```



## Save Output to s3
1. **Install Required Packages:**
>Make sure you have the necessary packages installed:
    ```
        pip install scrapy boto3

    ```
2. **Configure AWS Credentials:**
    ```
        export AWS_ACCESS_KEY_ID=your_access_key
        export AWS_SECRET_ACCESS_KEY=your_secret_key
    ```
3. **Modify Scrapy Settings:**
    ```
    FEEDS = {
        's3://<bucket-name>/<path>/%(name)s.json': {
            'format': 'json',
            'store_empty': False,
            'encoding': 'utf8',
        },
    }

    ```