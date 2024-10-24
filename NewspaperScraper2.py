from newspaper import Article
import pandas as pd
import csv
from logging import getLogger, INFO, FileHandler, Formatter

logger = getLogger(__name__)
logger.setLevel(INFO)
file_handler = FileHandler('newspaper_api.log', encoding='utf-8')
file_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

df = pd.read_csv("MediaData.csv")
filtered_df = df[df.iloc[:, 2].str.contains("indiatimes.com")]

with open("processed_media_data_economictimes.csv", "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Outlet', 'Title', 'Text', 'Prelim-Rating', 'Human-Rating','URL'])

    for index, row in filtered_df.iterrows():
        url = row.iloc[5]  # URL from the 6th column
        outlet = row.iloc[2]
        column7 = row.iloc[6]  # Value from the 7th column
        column8 = row.iloc[7]  # Value from the 8th column

        try:
            article = Article(url)
            article.download()
            article.parse()
            writer.writerow([outlet, article.title, article.text, column7, column8, url])
            print(f"Processed Article: {article.title} from {outlet}")
            logger.info(f"Processed Article: {article.title} from {outlet}")
        except Exception as e:
            print(f"Error processing {url}: {e}")
            logger.error(f"Error processing {url}: {e}")

print(filtered_df)