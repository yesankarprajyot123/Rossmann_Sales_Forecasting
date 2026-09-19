import streamlit as st
import numpy as np
import joblib

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Rossmann Sales Forecasting",
    page_icon="📈",
    layout="wide"
)

# ---------------------------
# LOAD MODEL
# ---------------------------

model = joblib.load("model/sales_model.pkl")

# ---------------------------
# CUSTOM CSS
# ---------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: #00E5FF;
}

.stButton > button {
    background-color: #00E5FF;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    height: 50px;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR
# ---------------------------

st.sidebar.title("👨‍💻 Developer")

st.sidebar.write("""
**Prajyot Yesankar**

Aspiring Data Analyst & Data Science Enthusiast

### Skills
- Python
- SQL
- Power BI
- Machine Learning
- Data Analytics
""")

# ---------------------------
# HEADER
# ---------------------------

st.title("📈 Rossmann Store Sales Forecasting")

st.markdown("""
Predict store sales using Machine Learning and Linear Regression.
""")

st.markdown("---")

# ---------------------------
# ABOUT PROJECT
# ---------------------------

st.header("📌 About Project")

st.write("""
Rossmann Sales Forecasting predicts future store sales based on
customer traffic, promotions, store status, weekdays, and seasonal trends.

### Machine Learning Algorithm
- Linear Regression

### Dataset
- Rossmann Store Sales Dataset

### Project Features
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Linear Regression
- Model Evaluation
- Streamlit Web Application
- Sales Forecasting
""")

st.markdown("---")

# ---------------------------
# DATASET INSIGHTS
# ---------------------------

st.header("📊 Dataset Insights")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Records", "1M+")

with col2:
    st.metric("Features", "5")

with col3:
    st.metric("R² Score", "0.8555")

with col4:
    st.metric("RMSE", "1484")

st.markdown("---")

# ---------------------------
# INPUT FORM
# ---------------------------

st.header("📝 Enter Store Information")

col1, col2 = st.columns(2)

with col1:

    customers = st.number_input(
        "Customers",
        min_value=0,
        value=500
    )

    promo = st.selectbox(
        "Promo Running?",
        [0, 1],
        help="0 = No, 1 = Yes"
    )

    open_store = st.selectbox(
        "Store Open?",
        [0, 1],
        help="0 = Closed, 1 = Open"
    )

with col2:

    day_of_week = st.selectbox(
        "Day Of Week",
        [1, 2, 3, 4, 5, 6, 7]
    )

    month = st.selectbox(
        "Month",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    )

# ---------------------------
# PREDICTION
# ---------------------------

if st.button("📈 Predict Sales"):

    input_data = np.array([[
        customers,
        promo,
        open_store,
        day_of_week,
        month
    ]])

    prediction = model.predict(input_data)

    predicted_sales = max(0, prediction[0])

    st.markdown("---")

    st.header("📊 Prediction Result")

    st.success(
        f"Estimated Sales: ₹ {predicted_sales:,.2f}"
    )

    st.info("""
    This prediction is generated using a Linear Regression model trained
    on Rossmann Store Sales data.
    """)

st.markdown("---")

# ---------------------------
# PROJECT WORKFLOW
# ---------------------------

st.header("⚙️ Project Workflow")

st.write("""
1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Train-Test Split
6. Linear Regression
7. Model Evaluation
8. Sales Forecasting
9. Streamlit Deployment
""")

st.markdown("---")

# ---------------------------
# ABOUT LINEAR REGRESSION
# ---------------------------

st.header("📚 About Linear Regression")

st.write("""
Linear Regression is a Machine Learning algorithm used to predict
continuous numerical values.

In this project it predicts:

### Store Sales

Based on:

- Customers
- Promotions
- Store Open Status
- Day Of Week
- Month

The model learns the relationship between these variables
and forecasts expected sales.
""")

st.markdown("---")

# ---------------------------
# ABOUT DEVELOPER
# ---------------------------

st.header("🙋 About Developer")

st.write("""
Hi, I'm **Prajyot Yesankar**

B.Tech Computer Science & Design Graduate.

Interested in:

- Data Analytics
- Data Science
- SQL
- Power BI
- Python
- Machine Learning

I enjoy building real-world business analytics and machine learning projects.
""")

st.markdown("---")

# ---------------------------
# CONTACT
# ---------------------------

st.markdown("""
<div style="text-align:center; font-size:20px;">
<a href="https://www.linkedin.com/in/prajyot-yesankar-79215b258/" target="_blank">💼 LinkedIn</a>
&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="https://github.com/yesankarprajyot123" target="_blank">💻 GitHub</a>
&nbsp;&nbsp;|&nbsp;&nbsp;
<a href="mailto:yesankarprajyot@gmail.com">📧 Email</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; font-size:18px;'>
❤️ Developed by <b>Prajyot Yesankar</b>
<br><br>
Python | SQL | Power BI | Machine Learning | Data Analytics
</div>
""", unsafe_allow_html=True)