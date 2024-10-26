import streamlit as st
from PIL import Image
import os

def display_methodology():
    st.title("Methodology")
    st.write("""
        The HDB Resale App uses interactive features and preprocessed datasets to give users personalized suggestions, policy explanations, and resale price simulations. The primary goal of the app is to make decision-making easier for first-time and second-time resale flat buyers by providing them with simple information and a simulation experience.

        ### Data Collection and Preprocessing

        The data is mainly gathered from public sources, such as the Housing and Development Board (HDB) website and other government websites that provide information on resale transactions, housing grants, and pertinent legislation. The data used comprises HDB selling prices, home types, grant eligibility criteria, and various housing loan schemes. The resale HDB data is processed to produce useful insights such as median resale prices, CPF Housing Grant comparisons, and loan scheme comparisons.

        ### Data Flow

       The app uses a structured data flow. When a user visits the "Resale HDB Simulator" or "HDB Policy Explainer" pages, the app reads the corresponding datasets with pandas, converts them to readily interpretable tables or charts, and dynamically refreshes the user interface with Streamlit.

        1. **Input Data**: When activating the app, it reads CSV files such as 'hdb_resale_data.csv' and 'housing_grants_data.csv'. These files provide data inputs for various functions and are presented or used in visualizations.

        2. **Processing**: The data is subsequently processed according to user inputs. In the "Resale HDB Simulator," for example, users can choose their buyer status, loan type, and chosen housing type. These inputs are used to filter the dataset, allowing the app to provide tailored information like pricing estimates or grant eligibility.


        3. **Outputs and Visualizations**: Based on the user's choices and the filtered data, the app creates outputs in the form of tables, charts (using Matplotlib), or text recommendations. For example, grant comparison charts are created by processing data from 'housing_grants_data.csv', giving customers a visual representation of how various CPF Housing Grants compare.

        ### Implementation Details

        The app is created with Python and Streamlit, a robust framework for developing online apps. The codebase is divided into sections matching to various functionalities. The app's pages, including "About Us," "Policy Explainer," and "Resale HDB Simulator," are coded as distinct functions. Streamlit's sidebar allows users to move between various areas. The app includes Matplotlib for data visualization, enabling dynamic production of bar charts, comparisons, and tables. The app also has error handling techniques, which ensure that missing files (such as CSV files) are recognized and sensible error messages are presented.
    """)

# Defining the file paths for the flowcharts
simulator_flowchart_path = r"C:\Users\danie\Desktop\HDB_Resale_App\resale_hdb_simulator_flowchart.png"
policy_explainer_flowchart_path = r"C:\Users\danie\Desktop\HDB_Resale_App\resale_hdb_policy_explainer_flowchart.png"

# Showing the "Resale HDB Simulator" flowchart
st.subheader("Flowchart for Resale HDB Simulator")
if os.path.exists(simulator_flowchart_path):
    img_simulator = Image.open(simulator_flowchart_path)
    st.image(img_simulator, caption="Flowchart for Resale HDB Simulator", use_column_width=True)
else:
    st.error(f"The file '{simulator_flowchart_path}' was not found. Please ensure the file is in the correct location.")

# Showing the "Resale HDB Policy Explainer" flowchart
st.subheader("Flowchart for Resale HDB Policy Explainer")
if os.path.exists(policy_explainer_flowchart_path):
    img_policy_explainer = Image.open(policy_explainer_flowchart_path)
    st.image(img_policy_explainer, caption="Flowchart for Resale HDB Policy Explainer", use_column_width=True)
else:
    st.error(f"The file '{policy_explainer_flowchart_path}' was not found. Please ensure the file is in the correct location.")

# Calling the function to run the methodology section
display_methodology()
