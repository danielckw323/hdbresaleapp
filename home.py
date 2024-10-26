import streamlit as st
import pandas as pd

def home():
    st.title("Resale HDB Statistics")

    # Loading the CSV data
    try:
        # Ensuring the path to the CSV file is right
        data = pd.read_csv("hdb_resale_data.csv")

        st.write("Here is the resale HDB data:")

        # Showing the table
        st.dataframe(data)

    except FileNotFoundError:
        st.error("The file 'hdb_resale_data.csv' was not found. Please ensure the file is in the correct location.")
    except Exception as e:
        st.error(f"An error occurred: {e}")


# Calling the function to render the home page in the app
home()




