import os
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="HealthMate Pro AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

/* ---------------- GLOBAL ---------------- */

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

/* Main Background */
.stApp {
    background:
    linear-gradient(rgba(7, 15, 30, 0.92),
    rgba(15, 23, 42, 0.96)),
    url("https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?q=80&w=2070&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
}

/* Remove Streamlit Header/Footer */
header, footer {
    visibility: hidden;
}

/* Main Wrapper */
.main-container {
    max-width: 1050px;
    margin: auto;
    padding-top: 20px;
}

/* ---------------- TOP NAVBAR ---------------- */

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 18px 28px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    backdrop-filter: blur(12px);
    margin-bottom: 30px;
}

/* Brand */
.brand {
    font-size: 28px;
    font-weight: 700;
    color: white;
}

/* Status Badge */
.badge {
    background: rgba(16,185,129,0.18);
    color: #34d399;
    padding: 8px 16px;
    border-radius: 30px;
    font-size: 14px;
    border: 1px solid rgba(52,211,153,0.3);
}

/* ---------------- HERO SECTION ---------------- */

.hero {
    text-align: center;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 62px;
    font-weight: 800;
    margin-bottom: 10px;
    color: white;
    letter-spacing: -1px;
}

.hero p {
    font-size: 20px;
    color: #cbd5e1;
    max-width: 750px;
    margin: auto;
    line-height: 1.7;
}

/* ---------------- MAIN CARD ---------------- */

.glass-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 28px;
    padding: 35px;
    backdrop-filter: blur(18px);
    box-shadow: 0px 10px 40px rgba(0,0,0,0.35);
}

/* Section Title */
.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 20px;
    color: white;
}

/* ---------------- INPUT ---------------- */

.stTextInput input {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    color: white !important;
    border-radius: 16px !important;
    padding: 16px !important;
    font-size: 17px !important;
}

.stTextInput input::placeholder {
    color: #cbd5e1;
}

/* ---------------- BUTTON ---------------- */

.stButton button {
    width: 100%;
    border-radius: 16px;
    border: none;
    padding: 14px;
    font-size: 18px;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #06b6d4, #14b8a6);
    transition: 0.3s ease;
    margin-top: 10px;
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 8px 25px rgba(20,184,166,0.35);
}

/* ---------------- RESPONSE ---------------- */

.response-card {
    margin-top: 28px;
    background: rgba(255,255,255,0.07);
    border-left: 5px solid #14b8a6;
    border-radius: 18px;
    padding: 28px;
}

.response-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 15px;
    color: #5eead4;
}

.response-text {
    font-size: 17px;
    line-height: 1.9;
    color: #e2e8f0;
}

/* ---------------- FEATURE BOXES ---------------- */

.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin-top: 35px;
}

.feature-box {
    background: rgba(255,255,255,0.05);
    padding: 22px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    text-align: center;
}

.feature-box h3 {
    color: white;
    margin-top: 12px;
}

.feature-box p {
    color: #cbd5e1;
    font-size: 15px;
}

/* ---------------- FOOTER ---------------- */

.footer {
    text-align: center;
    margin-top: 40px;
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.8;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ---------------- #

st.markdown("""
<div class="main-container">

<div class="navbar">
    <div class="brand">🩺 HealthMate Pro AI</div>
    <div class="badge">● AI Health Assistant Online</div>
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ---------------- #

st.markdown("""
<div class="main-container">

<div class="hero">
    <h1>Your Smart Healthcare Companion</h1>
    <p>
        Get AI-powered wellness guidance, symptom insights, and personalized health recommendations 
        through a modern intelligent healthcare assistant.
    </p>
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- PROMPT ---------------- #

with open("Template.txt", "r", encoding="utf-8") as file:
    template = file.read()

Prompt = ChatPromptTemplate([
    ('system', template),
    ('human', "{question}")
])

# ---------------- MODEL ---------------- #

model = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant"
)
chain = Prompt | model

# ---------------- MAIN CARD ---------------- #

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
<div class="section-title">💬 Describe Your Symptoms or Health Concern</div>
""", unsafe_allow_html=True)

user_input = st.text_input(
    "",
    placeholder="Example: I have fever, headache, and body pain since yesterday..."
)

if st.button("✨ Generate AI Health Guidance"):

    if user_input.strip() == "":
        st.warning("Please enter your health concern.")
    else:
        with st.spinner("Analyzing symptoms..."):

            response = chain.invoke({
                "question": user_input
            })

            st.markdown(f"""
            <div class="response-card">
                <div class="response-title">🧠 AI Health Analysis</div>
                <div class="response-text">
                    {response.content}
                </div>
            </div>
            """, unsafe_allow_html=True)


st.markdown("""
<div class="footer">

⚠️ <b>Disclaimer:</b> HealthMate Pro AI provides general wellness information only 
and should not be considered a substitute for professional medical advice, diagnosis, or treatment.

<br><br>

© 2026 HealthMate Pro AI • Intelligent Healthcare Assistant

</div>
""", unsafe_allow_html=True)

