import pandas as pd


def get_title_by_url(url):
    mediadata = pd.read_csv('mediadata.csv')  # Load the CSV file
    matching_row = mediadata[mediadata.iloc[:, 5] == url]  # Check for matching URL in the 6th column
    if not matching_row.empty:
        return matching_row.iloc[0, 4]  # Return the title from the 5th column
    return None  # Return None if no match is found


