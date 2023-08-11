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

3. **Run the spider
```
    scrapy crawl sqlspider -O out.csv
```
## Saving data to a MySQL database
To save data to mysql database make sure mysql python module is installed and create a table with coresponding fields(name,price,url)
```
    pip install mysql-connector-python
```

Configure the following in settings.py under the SQLPipeline class 
```
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'user',
            password = 'password',
            database = 'database'
        )
```


## Saving data to a PostgreSQL database

To save data to a PostgreSQL database ensure psycopg2 is installed and create a table with coresponding fields(name,price,url)
```
    pip install psycopg2
```
Configure the following in pipelines.py under the PostgresPipeline class 
```
    def create_connection(self):
        self.conn = psycopg2.connect(
            host = 'localhost',
            user = 'user',
            password = 'password',
            database = 'database'
        )
```

## Saving data to a MongoDb database

To save data to a MongoDb ensure pymongo is installed
```
    pip install pymongo
```
Configure the following in settings.py with youw mongodb endpoint and database name
```
    MONGODB_URI = "mongodb://localhost:27017/"
    MONGODB_DATABASE = "test"  # Replace with your database name
```


## Saving data to s3
1. **Install Required Packages:**
    Make sure you have the necessary packages installed:
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

For s3 and the database options, you dont need to specify the output flag and file. 

```
    scrapy crawl sqlspider
```