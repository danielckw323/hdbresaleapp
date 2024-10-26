import streamlit as st
from home import home
from resale_simulator import resale_simulator
from policy_explainer import policy_explainer
from about_us import about_us
from hdb_methodology import display_methodology

# Defining the password
PASSWORD = "aibootcamp"

# Initialising session state for authentication status
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def authenticate():
    # Displaying the login if the user is not authenticated
    if not st.session_state.authenticated:
        st.sidebar.title("Login")
        password = st.sidebar.text_input("Password:", type="password")

        if password == PASSWORD:
            st.session_state.authenticated = True
            st.sidebar.success("Logged in successfully!")
        elif password:
            st.sidebar.error("Invalid password")

# Running the authentication function
authenticate()

# Displaying the content of app if authenticated
if st.session_state.authenticated:
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
else:
    st.write("Please enter the password in the sidebar to access the app.")



