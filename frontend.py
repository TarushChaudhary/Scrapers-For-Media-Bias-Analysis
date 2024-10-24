import streamlit as st
from scraper import Scraper
from llm import chat_with_llm   # Assuming this is the class name in llm.py

def main():
    st.title("Article Analysis Chatbot")
    
    # Initialize session state variables if they don't exist
    if 'cleaned_text' not in st.session_state:
        st.session_state.cleaned_text = None

    # Create two columns for input fields
    col1, col2 = st.columns(2)
    
    # URL input field
    with col1:
        url = st.text_input("Enter article URL:")
        if st.button("Scrape"):
            try:
                scraper = Scraper(url)
                st.session_state.cleaned_text = scraper.get_clean_text()
                st.success("Article scraped successfully!")
                st.write("### Article Title:")
                st.write(scraper.get_title())
            except Exception as e:
                st.error(f"Error scraping article: {str(e)}")
    
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

