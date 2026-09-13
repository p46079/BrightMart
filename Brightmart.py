import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load(open('linear_reg.sav', 'rb'))

# Pink background + strawberry theme
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #ffd6e7;
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(255,255,255,0.5) 0 8px, transparent 9px),
            radial-gradient(circle at 90% 80%, rgba(255,255,255,0.5) 0 8px, transparent 9px);
    }

    /* Main content box */
    .block-container {
        background-color: rgba(255, 240, 246, 0.92);
        padding: 3rem;
        border-radius: 25px;
        margin-top: 2rem;
        box-shadow: 0 8px 30px rgba(180, 60, 100, 0.15);
    }

    /* Title */
    h1 {
        color: #d6336c !important;
        text-align: center;
        font-family: "Trebuchet MS", sans-serif;
        font-weight: 800;
    }

    /* Labels */
    label {
        color: #9c2f58 !important;
        font-weight: 600 !important;
    }

    /* Input boxes */
    div[data-baseweb="input"] {
        background-color: white;
        border: 2px solid #f3a6c2;
        border-radius: 12px;
    }

    /* Predict button */
    .stButton > button {
        background-color: #e83e75;
        color: white;
        border: none;
        border-radius: 15px;
        padding: 0.6rem 2rem;
        font-size: 18px;
        font-weight: bold;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #c92f62;
        color: white;
    }

    /* Strawberry decorations */
    .strawberry {
        position: fixed;
        font-size: 45px;
        z-index: 999;
    }

    .strawberry1 {
        top: 20px;
        left: 25px;
    }

    .strawberry2 {
        top: 20px;
        right: 25px;
    }

    .strawberry3 {
        bottom: 25px;
        left: 30px;
    }

    .strawberry4 {
        bottom: 25px;
        right: 30px;
    }
</style>

<div class="strawberry strawberry1">🍓</div>
<div class="strawberry strawberry2">🍓</div>
<div class="strawberry strawberry3">🍓</div>
<div class="strawberry strawberry4">🍓</div>
""", unsafe_allow_html=True)


st.title('🍓 Sales Prediction App 🍓')

# Input features
TV = st.number_input('📺 TV Advertising Budget', min_value=0.0)
Radio = st.number_input('📻 Radio Advertising Budget', min_value=0.0)
Newspaper = st.number_input('📰 Newspaper Advertising Budget', min_value=0.0)

# Make prediction
if st.button('🍓 Predict Sales 🍓'):
    input_data = np.array([[TV, Radio, Newspaper]])
    prediction = model.predict(input_data)[0]
    st.success(f'🍓 Predicted Sales: {prediction:.2f}')
