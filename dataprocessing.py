import pandas as pd

class ProcessOutlet:
    def __init__(self, outlet_name):
        self.outlet_name = outlet_name
        self.df = pd.read_csv(f'processed_data/processed_media_data_{outlet_name}.csv')

    def _save_processed_data(self):
        self.df.to_csv(f'processed_data/processed_media_data_{self.outlet_name}.csv', index=False)
        print(f"Saved processed data for {self.outlet_name}")  # Add this line for debugging

    def ProcessEconomictimes(self):
        junk = r"\n\n\n\n\(You can now subscribe to our\n\n\(You can now subscribe to our Economic Times WhatsApp channel"
        self.df['Text'] = self.df['Text'].str.replace(junk, '', regex=True)
        self.df['Text'] = self.df['Text'].str.replace("Also Read.*", "", regex=True, case=False)
        self.df['Text'] = self.df['Text'].str.replace("Disclaimer.*", "", regex=True, case=False)
        self._save_processed_data()

        
    def ProcessHindustantimes(self):
        self.df['Text'] = self.df['Text'].str.replace("Also Read.*", "", regex=True, case=False)
        self._save_processed_data()

    def ProcessFinancialexpress(self):
        self.df['Text'] = self.df['Text'].str.replace("Disclaimer.*", "", regex=True, case=False)
        self.df['Text'] = self.df['Text'].str.replace("Also Read.*", "", regex=True, case=False)
        self._save_processed_data()

    def ProcessThehindu(self):
        self.df['Text'] = self.df['Text'].str.replace("Also Read.*", "", regex=True, case=False)
        self._save_processed_data()
    
    def ProcessNDTV(self):
        self.df['Text'] = self.df['Text'].str.replace("Also Read.*", "", regex=True, case=False)
        self._save_processed_data()

    def ProcessNews18(self):
        self.df['Text'] = self.df['Text'].str.replace("Also Read.*", "", regex=True, case=False)
        self._save_processed_data()

    def remove_duplicate_titles(self):
        self.df.drop_duplicates(subset="Title", keep="last", inplace=True)
        self._save_processed_data()



