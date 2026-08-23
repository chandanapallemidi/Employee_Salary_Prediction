import streamlit as st
import pandas as pd
import pickle

# Page configuration
st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💼",
    layout="wide"
)

# Colorful CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
}

.title {
    text-align: center;
    color: white;
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: white;
    font-size: 20px;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    margin-top: 20px;
}

.result {
    background: linear-gradient(135deg, #11998e, #38ef7d);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: bold;
}

.footer {
    text-align: center;
    color: white;
    margin-top: 40px;
    font-size: 17px;
}

</style>
""", unsafe_allow_html=True)


# Load model
try:
    with open("salary_model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error("❌ Model could not be loaded.")
    st.error(str(e))
    st.stop()


# Title
st.markdown(
    '<div class="title">💼 Employee Salary Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">🤖 AI Based Employee Salary Prediction System</div>',
    unsafe_allow_html=True
)


# Input section
st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("👤 Enter Employee Details")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "🎂 Age",
        min_value=18,
        max_value=70,
        value=25
    )

    gender = st.selectbox(
        "⚧ Gender",
        ["Male", "Female", "Other"]
    )

    experience = st.number_input(
        "⏳ Years of Experience",
        min_value=0.0,
        max_value=50.0,
        value=1.0,
        step=0.5
    )

with col2:

    education = st.selectbox(
        "🎓 Education Level",
        [
            "Bachelor's Degree",
            "Master's Degree",
            "PhD"
        ]
    )

    job_title = st.selectbox(
        "💼 Job Title",
        [
            "Software Engineer",
            "Data Scientist",
            "Data Analyst",
            "Senior Manager",
            "Sales Associate",
            "Director",
            "Software Developer",
            "Project Manager",
            "Business Analyst",
            "Web Developer"
        ]
    )

st.markdown("</div>", unsafe_allow_html=True)


# Prediction button
if st.button("🚀 Predict Salary"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Education Level": [education],
        "Job Title": [job_title],
        "Years of Experience": [experience]
    })

    try:

        prediction = model.predict(input_data)

        salary = prediction[0]

        st.markdown(
            f"""
            <div class="result">
                💰 Predicted Annual Salary<br><br>
                ₹ {salary:,.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success("✅ Salary prediction completed successfully!")

        st.subheader("📋 Employee Details")

        st.dataframe(
            input_data,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:

        st.error("❌ Prediction failed.")
        st.code(str(e))


# Footer
st.markdown(
    """
    <div class="footer">
        ✨ Created by <b>Chandana Pallemidi</b> & 
        <b>Molankula Reshma</b> ✨
        <br>
        Employee Salary Prediction Project
    </div>
    """,
    unsafe_allow_html=True
)