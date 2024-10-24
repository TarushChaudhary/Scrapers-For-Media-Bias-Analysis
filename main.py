import streamlit as st
from BS4scraper import scrape_website, extract_body_content, clean_body_content, split_into_sections
from bs4 import BeautifulSoup
from dataprocessing import get_title_by_url

st.title("Web Scraping App")

url = st.text_input("Enter the URL to scrape")

if st.button("Scrape"):
    if url:
        st.write("Scraping the website...")
        result = scrape_website(url)
        print(result)
        title = get_title_by_url(url)
        st.write(title)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content, url)
        st.session_state.cleaned_content = cleaned_content

        sections = split_into_sections(cleaned_content)

        with st.expander("Show Cleaned Content"):
            st.text_area("Cleaned Content", value=cleaned_content, height=300)
            


        # 
