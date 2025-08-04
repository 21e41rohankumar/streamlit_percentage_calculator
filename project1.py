import streamlit as st

st.set_page_config(layout="centered")

st.title("🎓 Percentage Calculator")

# Headings
st.markdown('<div class="main-title">A Small Percentage Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Input marks for 6 subjects to calculate percentage and result.</div>', unsafe_allow_html=True)

# ✅ Styling with background image and glassmorphism
st.markdown("""
    <style>
    /* Background image */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images4.alphacoders.com/659/659449.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Overlay for readability */
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0;
        bottom: 0;
        right: 0;
        left: 0;
        background: rgba(0, 0, 0, 0.3);
        z-index: 0;
    }

    /* Headings */
    .main-title {
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 36px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 10px;
        position: relative;
        z-index: 1;
    }

    .subtitle {
        font-size: 18px;
        color: #eeeeee;
        text-align: center;
        margin-bottom: 30px;
        position: relative;
        z-index: 1;
    }

    /* Input fields */
    .stNumberInput > div > input {
        background-color: white;
        color: black;
        position: relative;
        z-index: 1;
    }

    /* Result box styling */
    .glass-box {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 30px;
        margin-top: 30px;
        color: #ffffff;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        text-align: center;
        font-size: 20px;
        font-family: 'Segoe UI', sans-serif;
        position: relative;
        z-index: 1;
    }

    .glass-box .box-title {
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 15px;
    }

    .box-row {
        margin: 10px 0;
    }

    .pass {
        color: #00ff88;
        font-weight: bold;
    }

    .fail {
        color: #ff4d4d;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Input fields
sum1 = st.number_input("Enter the 1st subject marks", min_value=0, max_value=100)
sum2 = st.number_input("Enter the 2nd subject marks", min_value=0, max_value=100)
sum3 = st.number_input("Enter the 3rd subject marks", min_value=0, max_value=100)
sum4 = st.number_input("Enter the 4th subject marks", min_value=0, max_value=100)
sum5 = st.number_input("Enter the 5th subject marks", min_value=0, max_value=100)
sum6 = st.number_input("Enter the 6th subject marks", min_value=0, max_value=100)

# Calculate and display result
if st.button("🎯 Calculate Total Marks"):
    total_marks = sum1 + sum2 + sum3 + sum4 + sum5 + sum6
    max_marks = 600
    percentage = (total_marks / max_marks) * 100

    # Pass/fail condition
    if percentage >= 40:
        result_text = "✅ Pass"
        result_class = "pass"
    else:
        result_text = "❌ Fail"
        result_class = "fail"

    # Display result
    st.markdown(f'''
        <div class="glass-box">
            <div class="box-title">🎓 Exam Result</div>
            <div class="box-row"><strong>Total Marks:</strong> {total_marks} / {max_marks}</div>
            <div class="box-row"><strong>Percentage:</strong> {percentage:.2f}%</div>
            <div class="box-row"><strong>Result:</strong> <span class="{result_class}">{result_text}</span></div>
        </div>
    ''', unsafe_allow_html=True)
