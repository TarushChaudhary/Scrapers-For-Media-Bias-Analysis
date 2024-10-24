from newspaper import Article
from cleaning import ProcessOutlet

outlets = ["economictimes","hindustantimes","financialexpress","thehindu","ndtv","news18"]
class Scraper:
    def __init__(self, url):
        self.url = url
        self.outlet = url.split(".")[1]
        self.article = Article(url)
        self.article.download()
        self.article.parse()

    def get_title(self):
        return self.article.title

    def get_raw_text(self):
        return self.article.text

    def get_summary(self):
        return self.article.summary
    
    def get_clean_text(self):
        processed_text = ProcessOutlet(self.outlet, self.article.text)
        if self.outlet == "economictimes":
            return processed_text.ProcessEconomictimes()
        elif self.outlet == "hindustantimes":
            return processed_text.ProcessHindustantimes()
        elif self.outlet == "financialexpress":
            return processed_text.ProcessFinancialexpress()
        elif self.outlet == "thehindu":
            return processed_text.ProcessThehindu()
        elif self.outlet == "ndtv":
            return processed_text.ProcessNDTV()
        elif self.outlet == "news18":
            return processed_text.ProcessNews18()
        else:
            return processed_text.ProcessUnknown()            
