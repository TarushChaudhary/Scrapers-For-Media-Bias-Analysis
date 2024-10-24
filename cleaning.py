import re

class ProcessOutlet:
    def __init__(self, outlet_name, text):
        self.outlet_name = outlet_name
        self.text = text

    def _save_processed_data(self):
        # This method might need to be updated or removed if we're not using pandas
        pass

    def ProcessEconomictimes(self):
        junk = r"\n\n\n\n\(You can now subscribe to our\n\n\(You can now subscribe to our Economic Times WhatsApp channel"
        self.text = re.sub(junk, '', self.text)
        self.text = re.sub("Also Read.*", "", self.text, flags=re.IGNORECASE)
        self.text = re.sub("Disclaimer.*", "", self.text, flags=re.IGNORECASE)
        self.text = re.sub(r'\n+', ' ', self.text)  # Remove empty lines
        return self.text

    def ProcessHindustantimes(self):
        self.text = re.sub("Also Read.*", "", self.text, flags=re.IGNORECASE)
        self.text = re.sub(r'\n+', ' ', self.text)  # Remove empty lines
        return self.text

    def ProcessFinancialexpress(self):
        self.text = re.sub("Disclaimer.*", "", self.text, flags=re.IGNORECASE)
        self.text = re.sub("Also Read.*", "", self.text, flags=re.IGNORECASE)
        self.text = re.sub(r'\n+', ' ', self.text)  # Remove empty lines
        return self.text

    def ProcessThehindu(self):
        self.text = re.sub("Also Read.*", "", self.text, flags=re.IGNORECASE)
        self.text = re.sub(r'\n+', ' ', self.text)  # Remove empty lines
        return self.text
    
    def ProcessNDTV(self):
        self.text = re.sub("Also Read.*", "", self.text, flags=re.IGNORECASE)
        self.text = re.sub(r'\n+', ' ', self.text)  # Remove empty lines
        return self.text

    def ProcessNews18(self):
        self.text = re.sub("Also Read.*", "", self.text, flags=re.IGNORECASE)
        self.text = re.sub(r'\n+', ' ', self.text)  # Remove empty lines
        return self.text
    
    def ProcessUnknown(self):
        self.text = re.sub(r'\n+', ' ', self.text)  # Remove empty lines
        self.text = re.sub("Also Read.*", "", self.text, flags=re.IGNORECASE)
        return self.text
