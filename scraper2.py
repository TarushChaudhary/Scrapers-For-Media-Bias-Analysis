from newspaper import Article
from cleaning import ProcessOutlet
from BS4scraper import scrape_website, extract_body_content, clean_body_content, extract_title
outlets = ["economictimes","hindustantimes","financialexpress","thehindu","ndtv","news18"]
class Scraper:
    def __init__(self, url):
        self.url = url
        try:
            self.article = Article(url)
            self.article.download()
            self.article.parse()
            self.method = "newspaper"
        except Exception as e:
            print(f"Error downloading using Newspaper, Attempting to Scrape Using BeautifulSoup")
            self.method = "scraping"
            self.html = scrape_website(self.url)

    def get_title(self):
        if self.method == "newspaper":
            return self.article.title
        else:
            return extract_title(self.html)
            

    def get_raw_text(self):
        if self.method == "newspaper":
            return self.article.text
        else:
            return extract_body_content(self.html)

    def get_summary(self):
        return self.article.summary
    
    def get_clean_text(self):
        if self.method == "newspaper":
            processed_text = ProcessOutlet(self.article.text)
            return processed_text.common_cleaning()
        else:
            return clean_body_content(extract_body_content(self.html), self.url)
