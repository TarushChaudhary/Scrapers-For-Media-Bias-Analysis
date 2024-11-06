import re

class ProcessOutlet:
    def __init__(self, text):
        self.text = text

    def common_cleaning(self):
        self.text = re.sub("Also Read.*", "", self.text, flags=re.IGNORECASE)
        self.text = re.sub(r'\n+', ' ', self.text)  # Remove empty lines
        self.text = re.sub("Disclaimer.*", "", self.text, flags=re.IGNORECASE)
        
        return self.text