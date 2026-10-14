import streamlit as st

st.set_page_config(page_title="About the Tech", page_icon="💡")

st.markdown("# 💡 About the Technology")
st.write(
    """
    Vali-AI uses a combination of powerful AI and data analysis models to provide insights into your startup idea. 
    Here's a breakdown of the core components:
    """
)
st.divider()

st.header("1. Uniqueness Analysis")
st.markdown(
    """
    - **Model:** `Sentence-BERT (all-MiniLM-L6-v2)`
    - **How it works:** This is a deep learning model that understands the meaning and context of sentences. 
      It converts your idea description and the descriptions of over 40,000 existing startups into numerical representations (vectors).
    - **The Magic:** By calculating the "distance" between your idea's vector and all other vectors, we can find the most similar existing companies. 
      A large distance means your idea is more unique!
    """
)

st.header("2. Market Trend Analysis")
st.markdown(
    """
    - **Tool:** `pytrends` (Google Trends API)
    - **How it works:** This tool programmatically fetches historical search interest data from Google for your specified keyword.
    - **The Insight:** We analyze the data from the last 5 years to determine if public interest in your concept is growing, stable, or declining. This is a strong indicator of market demand.
    """
)

st.header("3. Public Sentiment Analysis")
st.markdown(
    """
    - **Model:** `Hugging Face Transformers (distilbert-base-uncased-finetuned-sst-2-english)`
    - **How it works:** This is a pre-trained model specifically fine-tuned to classify text as having a POSITIVE or NEGATIVE sentiment.
    - **The Insight:** By analyzing a sample customer comment, we can gauge the emotional tone surrounding the problem you're trying to solve. A strong negative sentiment often indicates a significant "pain point" that customers are eager to solve.
    """
)
