import streamlit as st
from scraper2 import Scraper
from llm import chat_with_llm   # Assuming this is the class name in llm.py
import re
def main():
    st.title("Article Analysis Chatbot")
    
    # Initialize session state variables if they don't exist
    if 'cleaned_text' not in st.session_state:
        st.session_state.cleaned_text = None

    # Create two columns for input fields
    col1, col2 = st.columns(2)
    website_pattern = r"https?://(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    # URL input field
    with col1:
        url = st.text_input("Enter article URL or text:")
        if st.button("Scrape"):
            try:
                if re.search(website_pattern, url):
                    scraper = Scraper(url)
                    st.session_state.cleaned_text = scraper.get_clean_text()
                    st.success("Article scraped successfully!")
                    st.write("### Article Title:")
                    st.write(scraper.get_title())
                else:
                    st.session_state.cleaned_text = url
                    st.success("Text scraped successfully!")
            except Exception as e:
                st.error(f"Error scraping article: {str(e)}, please enter text manually.")
    # LLM prompt input field
    with col2:
        prompt = st.text_input("Enter your prompt:")
        if st.button("Send to LLM"):
            if st.session_state.cleaned_text is None:
                st.warning("Please scrape an article first!")
            elif not prompt:
                st.warning("Please enter a prompt!")
            else:
                try:
                    response = chat_with_llm(prompt, st.session_state.cleaned_text)
                    st.write("### LLM Response:")
                    st.write(response)
                except Exception as e:
                    st.error(f"Error processing LLM request: {str(e)}")

    # Display cleaned text if available
    if st.session_state.cleaned_text:
        with st.expander("View Cleaned Article Text"):
            st.write(st.session_state.cleaned_text)

if __name__ == "__main__":
    main()

