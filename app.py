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
if page == "Home":
    home()
elif page == "Resale HDB Simulator":
    resale_simulator()
elif page == "HDB Policy Explainer":
    policy_explainer()
elif page == "About Us":
    about_us()
elif page == "Methodology":
    display_methodology()



