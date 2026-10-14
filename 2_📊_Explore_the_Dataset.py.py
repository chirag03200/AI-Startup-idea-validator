import streamlit as st
import pandas as pd

st.set_page_config(page_title="Explore Dataset", page_icon="📊")

st.markdown("# 📊 Explore the Startup Dataset")
st.write("This is the dataset of over 40,000 startups used for the uniqueness analysis. Use the search box below to filter by name.")
st.divider()

@st.cache_data
def load_data():
    """Loads the startup CSV data."""
    try:
        df = pd.read_csv('startups.csv')
        # Ensure description column exists and is a string
        if 'description' not in df.columns:
            df['description'] = ''
        df['description'] = df['description'].fillna('').astype(str)
        return df
    except FileNotFoundError:
        return None

df_startups = load_data()

if df_startups is not None:
    search_query = st.text_input("Search for a startup by name:", "")
    
    if search_query:
        # Filter the DataFrame based on the search query (case-insensitive)
        filtered_df = df_startups[df_startups['name'].str.contains(search_query, case=False, na=False)]
        st.write(f"Found {len(filtered_df)} startups matching your search.")
        st.dataframe(filtered_df)
    else:
        # Show the first 1000 rows by default if no search query
        st.write("Showing the first 1,000 startups. Use the search box to find specific ones.")
        st.dataframe(df_startups.head(1000))
else:
    st.error("Error: The 'startups.csv' file was not found. Please make sure it's in the main directory.")
