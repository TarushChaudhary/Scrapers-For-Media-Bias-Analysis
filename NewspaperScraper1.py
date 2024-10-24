import pandas as pd
from newspaper import Article
import csv
import time
from requests.exceptions import Timeout
from logging import getLogger, INFO, FileHandler, Formatter

# Set up logging
logger = getLogger(__name__)
logger.setLevel(INFO)
file_handler = FileHandler('newspaper_api.log', encoding='utf-8')
file_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Read the CSV file
df = pd.read_csv('MediaData.csv')

#outlets = ["thehindu.com", "financialexpress.com", "ndtv.com", "opindia.com","hindustantimes.com","economictimes.indiatimes.com"]
outlets = ["news18.com"]

processed_outlets = set()

for i in outlets:
    filtered_df = df[df.iloc[:, 2].str.contains(i)]

    # Create a new CSV file and write the header
    with open(f'processed_media_data_{i.split(".")[0]}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Outlet', 'Title', 'Text', 'Prelim-Rating', 'Human-Rating','URL'])

        # Process each row in the filtered dataframe
        for index, row in filtered_df.iterrows():
            url = row.iloc[5]  # URL from the 6th column
            outlet = row.iloc[2]
            column7 = row.iloc[6]  # Value from the 7th column
            column8 = row.iloc[7]  # Value from the 8th column
            print(url)
            try:
                # Scrape the article
                article = Article(url)
                article.download()
                article.parse()

                # Write the data to the new CSV file
                writer.writerow([outlet, article.title, article.text, column7, column8, url])
                logger.info(f"Processed Article: {article.title} from {outlet}")
                print(f"Processed Article: {article.title} from {outlet}")
            except Timeout:
                if "financialexpress.com" in i:
                    if len(processed_outlets) == len(outlets) - 1:
                        logger.warning(f"Timeout occurred for {url}. Waiting for 5 seconds before retrying...")
                        time.sleep(5)
                        try:
                            article = Article(url)
                            article.download()
                            article.parse()
                            writer.writerow([outlet, article.title, article.text, column7, column8, url])
                        except Exception as e:
                            logger.error(f"Error processing URL {url} after waiting: {str(e)}")
                    else:
                        logger.warning(f"Timeout occurred for {url}. Switching to next outlet.")
                        break
                else:
                    logger.warning(f"Timeout occurred for {url}. Skipping...")
            except Exception as e:
                logger.error(f"Error processing URL {url}: {str(e)}")

    processed_outlets.add(i)
    logger.info(f"Processing complete. Results saved in 'processed_media_data_{i.split('.')[0]}.csv'")