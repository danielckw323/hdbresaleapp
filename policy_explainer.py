import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def policy_explainer():
    st.title("HDB Policy Explainer & Simulator")

    st.write("Explore the relevant HDB policies based on your situation and simulate different housing options.")

    # The following is the section for Simulator
    st.subheader("HDB Housing Simulator")

    # Step 1: Finding out if the user is a first-time or second-time resale flat buyer
    buyer_type = st.selectbox(
        "Are you a first-time or second-time HDB buyer?",
        ("First-Time Buyer", "Second-Time Buyer")
    )

    # Step 2: Enquiring the type of housing loan that the resale flat buyer is looking at.
    loan_type = st.selectbox(
        "Select the type of housing loan you are considering:",
        ("HDB Loan", "Bank Loan")
    )

    # Step 3: Enquiring the preferred housing type based on the options listed
    housing_type = st.selectbox(
        "Select your preferred housing type:",
        ("1-room", "2-room", "3-room", "4-room", "5-room",
         "Executive Apartment", "Executive Maisonette", "3 Gen Multi-Generation")
    )

    # Showing the selections made by the user
    st.write(f"### Summary of Your Selections:")
    st.write(f"**Buyer Type**: {buyer_type}")
    st.write(f"**Housing Loan**: {loan_type}")
    st.write(f"**Preferred Housing Type**: {housing_type}")

    # Recommendation Feature
    st.subheader("Recommendation")
    if buyer_type == "First-Time Buyer":
        st.write(
            "As a **First-Time Buyer**, you may want to refer to the "
            "[HDB First-Time Home Buyers' Guide](https://www.hdb.gov.sg/cs/infoweb/about-us/news-and-publications/publications/hdbspeaks/Helping-First-time-Homebuyers-Afford-a-Resale-Flat) "
            "for more information about available schemes and grants."
        )
    elif buyer_type == "Second-Time Buyer":
        st.write(
            "As a **Second-Time Buyer**, you may want to refer to the "
            "[HDB Fresh Start Housing Scheme](https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-new-flats/application/fresh-start-housing-scheme) "
            "to explore options available for you."
        )

# Calling the function to run the explainer
policy_explainer()