import streamlit as st
from home import home
from resale_simulator import resale_simulator
from policy_explainer import policy_explainer
from about_us import about_us
from hdb_methodology import display_methodology

# Displaying the content
st.title("Welcome to the HDB Resale App")
st.write("Here’s your app content.")

# Sidebar for navigation
st.sidebar.title("HDB Resale App")
page = st.sidebar.radio(
    "Navigation",
    ("Home", "Resale HDB Simulator", "HDB Policy Explainer", "About Us", "Methodology")
)

# Page routing
try:
    if page == "Home":
        st.write("Loading Home page...")  # Debug statement
        home()
    elif page == "Resale HDB Simulator":
        st.write("Loading Resale HDB Simulator...")  # Debug statement
        resale_simulator()
    elif page == "HDB Policy Explainer":
        st.write("Loading HDB Policy Explainer...")  # Debug statement
        policy_explainer()
    elif page == "About Us":
        st.write("Loading About Us...")  # Debug statement
        about_us()
    elif page == "Methodology":
        st.write("Loading Methodology...")  # Debug statement
        display_methodology()
except Exception as e:
    st.error(f"An error occurred: {e}")



