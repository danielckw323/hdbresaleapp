import streamlit as st
import pandas as pd

def home():
    st.title("Resale HDB Statistics")

    st.write("""
    [IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters. 
    
    Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

    Always consult with qualified professionals for accurate and personalized advice.]
        
    The statistics provide the median prices for resale transactions of a particular flat type in a given town.
    This is based on resale cases registered in the quarter. The median price (at fiftieth percentile) tells you 
    that half of the flats transacted during the quarter were sold above the median price and half were sold below the median price.

    The median resale prices are inclusive of Cash-Over-Valuation (COV) for transactions where resale prices are above market valuations.

    For more information about HDB resale data, you can visit the [Resale Statistics](https://www.hdb.gov.sg/cs/infoweb/residential/buying-a-flat/resale/resale-statistics) page.
    """)

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




