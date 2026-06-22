# Customer Churn Prediction System

An end-to-end intelligent web application designed to analyse customer retention metrics and predict business churn risk. This system evaluates financial parameters, complaint frequencies, and customer tenure weights to classify accounts into high-risk or low-risk operational retention profiles.

## Live Demo
🔗 **[Click Here to View the Live Project](https://customer-churn-predictor-6y7gknxb535vjgadmdqixf.streamlit.app/)**

---

## Key Features
- **Real-time Risk Assessment:** Instant operational classification based on algorithmic risk vectors.
- **Dynamic Scoring Engine:** Evaluates behavioural matrices including tenure months, service charges, and customer care complaint histories.
- **Enterprise UI Layout:** Designed using Streamlit for an interactive, modern, and responsive browser user experience.
- **Highly Compatible Architecture:** Implemented with zero-library mathematical fallback models to ensure zero dependency conflicts and maximum system compliance.

---

## Technical Stack
- **Language:** Python
- **Framework:** Streamlit (For Web Interface & Input Controllers)
- **Analytical Methodology:** Rule-based Matrix Logic and Feature Weight Engineering

---

## Project Structure
```text
Customer-Churn-Predictor/
├── app.py             # Main application file (Algorithmic processing + Streamlit UI)
├── requirements.txt   # Server deployment configuration file
└── README.md          # Project documentation (This file)
```

---

## How to Run Locally

If you want to run this application on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate to the project folder:**
   ```bash
   cd Customer-Churn-Predictor
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit web application:**
   ```bash
   streamlit run app.py
   ```

---

## Algorithmic Insights
The engine works on a mathematical threshold strategy where weight values are dynamically assigned to independent inputs:
1. **Tenure Deficits:** Customers with less than 6 months of corporate association are assigned higher churn base values.
2. **Complaint Vulnerabilities:** Accounts with 3 or more logged complaints trigger serious risk parameter expansions.
3. **Financial Overheads:** Higher monthly configurations scale up the baseline threshold score, determining whether strategic retention intervention is needed.

---
Developed by Lucky Sisodia. Open for collaboration and architectural enhancements.
