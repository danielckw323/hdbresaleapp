# This is the resale_simulator.py file for the HDB Resale App project

import streamlit as st

def resale_simulator():
    st.title("Resale HDB Buying Simulator")
    # Adding interactive components such as sliders and inputs to simulate buying a resale HDB
    st.write("Simulation will be implemented here.")

    # User providing inputs for CPF and loan information
    cpf_savings = st.number_input("Enter your CPF savings:", min_value=0, value=50000)
    monthly_repayment = st.number_input("Expected monthly housing loan repayment:", min_value=0, value=1000)
    loan_duration = st.number_input("Loan duration (years):", min_value=1, max_value=30, value=25)

    # Computation to estimate loan eligibility
    total_loan = monthly_repayment * loan_duration * 12
    st.write(f"Based on your inputs, you can afford a loan amount of approximately ${total_loan}.")

    # Adding a logic to provide recommendation based on three key elements: CPF, loan amount, and housing market
    if cpf_savings < 20000:
        st.warning("Your CPF savings are low. Consider increasing CPF contributions or adjusting your budget.")
    else:
        st.success("You have sufficient CPF savings to proceed with a resale HDB purchase.")

