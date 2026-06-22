"""
Customer Churn Prediction Web Dashboard
Author: Lucky Sisodia
Description: Clean Streamlit interface using programmatic risk scoring matrices.
"""

import streamlit as st

# Page layout configuration
st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

def evaluate_churn_risk_score(tenure, charges, complaints):
    """
    Algorithmic calculation engine evaluating risk weight factors.
    Returns 1 for high churn risk, 0 for loyal customer metrics.
    """
    # Baseline logic tracking customer dropouts
    risk_factor = 0.0
    
    # Tenure tracking logic weight
    if tenure < 6:
        risk_factor += 0.4
    elif tenure < 12:
        risk_factor += 0.2
        
    # Complaint analysis metrics weight
    if complaints >= 3:
        risk_factor += 0.5
    elif complaints >= 1:
        risk_factor += 0.2
        
    # Financial metrics distribution weight
    if charges > 80.0:
        risk_factor += 0.3
    elif charges > 40.0:
        risk_factor += 0.1
        
    # Dynamic matrix threshold split decision
    if risk_factor >= 0.6:
        return 1
    else:
        return 0

# User Interface Layout
st.title("Customer Churn Prediction System")
st.write("Enter customer engagement metrics below to calculate retention risk assessment analysis.")

st.write("---")

# Input numeric controllers
tenure_input = st.number_input("Customer Tenure (In Months):", min_value=0, max_value=120, value=12, step=1)
charges_input = st.number_input("Monthly Bill Charges (In USD/INR):", min_value=0.0, max_value=500.0, value=50.0, step=5.0)
complaints_input = st.number_input("Total Customer Care Complaints Lodged:", min_value=0, max_value=20, value=1, step=1)

st.write("---")

# Predictive calculation engine trigger
if st.button("Evaluate Churn Risk Profile", type="primary"):
    
    # Core mathematical risk validation matrix execution
    prediction = evaluate_churn_risk_score(tenure_input, charges_input, complaints_input)
    
    st.subheader("Risk Analytics Assessment Result:")
    
    if prediction == 1:
        st.error("CHURN ALERT: This account shows clear behavioral markers indicating a high risk of canceling services. Strategic retention offers recommended immediately.")
    else:
        st.success("LOYAL ASSESSMENT: This account displays safe behavioral patterns. High baseline probability of long-term operational retention.")

st.write("---")
# Credits attribution block
st.caption("Made by Lucky Sisodia for all")
