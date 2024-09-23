import pandas as pd
from newspaper import Article
import csv

# Read the CSV file
df = pd.read_csv('MediaData.csv')

# Filter rows where the 3rd column matches "thehindu.com", "financialexpress.com", "ndtv.com", "opindia.com"
filtered_df = df[df.iloc[:, 2].str.contains("thehindu.com|financialexpress.com|ndtv.com|opindia.com")] 

# Create a new CSV file and write the header
with open('processed_media_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Outlet', 'Title', 'Text', 'Prelim-Rating', 'Human-Rating','URL'])

    # Process each row in the filtered dataframe
    for index, row in filtered_df.iterrows():
        url = row.iloc[5]  # URL from the 6th column
        outlet = row.iloc[2]
        column7 = row.iloc[6]  # Value from the 7th column
        column8 = row.iloc[7]  # Value from the 8th column

        try:
            # Scrape the article
            article = Article(url)
            article.download()
            article.parse()

            # Write the data to the new CSV file
            writer.writerow([outlet, article.title, article.text, column7, column8, url])
        except Exception as e:
            print(f"Error processing URL {url}: {str(e)}")

print("Processing complete. Results saved in 'processed_media_data.csv'")