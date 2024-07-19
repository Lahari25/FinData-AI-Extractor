import streamlit as st
import pandas as pd

# Dummy function to simulate the openai_helper.extract_financial_data function
def extract_financial_data(news_article):
    data = {
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Value": ["Apple", "AAPL", "$94.84 billion", "$24.16 billion", "$1.52"]
    }
    return pd.DataFrame(data)

# Set up layout
col1, col2 = st.columns([3, 2])

# Initialize the DataFrame
financial_data_df = pd.DataFrame({
    "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
    "Value": ["", "", "", "", ""]
})

# Left column: text area and button
with col1:
    st.title("Financial Data Extraction Tool")
    news_article = st.text_area("Paste your financial news article here", height=300)
    if st.button("Extract"):
        financial_data_df = extract_financial_data(news_article)

# Right column: display the DataFrame
with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.table(financial_data_df)
