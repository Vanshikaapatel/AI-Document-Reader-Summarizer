import streamlit as st

st.set_page_config(
    page_title="AI Homepage",
    layout="wide",
    page_icon="📝"
)

# ---- HIDE STREAMLIT SIDEBAR & TOGGLE ICON ----
st.markdown("""
<style>
/* Hide sidebar completely */
section[data-testid="stSidebar"] {
    display: none !important;
}

/* Hide sidebar toggle icon (keyboard_double_arrow_right) */
button[kind="header"] {
    display: none !important;
}

/* Extra safety: hide material icons text */
.material-icons {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)


# ------------------- PREMIUM BLUE NAVBAR -------------------
def navbar(active="Home"):
    st.markdown("""
    <style>

    /* NAVBAR BOX */
    .nav-container {
        width: 100%;
        padding: 18px 0;
        display: flex;
        justify-content: center;
        gap: 40px;
        background: rgba(30, 58, 138, 0.35); /* 🔵 Blue glass effect */
        backdrop-filter: blur(14px);
        border-radius: 16px;
        margin-bottom: 28px;
        box-shadow: 0 6px 28px rgba(0,0,0,0.25);
    }

    /* BUTTON STYLE */
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6, #06b6d4); /* 🔵 Blue gradient */
        color: white;
        font-size: 18px;
        padding: 12px 26px;
        font-weight: 700;
        border-radius: 12px;
        border: none;
        cursor: pointer;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.35);
        transition: 0.25s ease;
    }

    /* HOVER EFFECT */
    .stButton>button:hover {
        transform: scale(1.12);
        background: linear-gradient(135deg, #06b6d4, #3b82f6); /* reverse gradient */
        box-shadow: 0 10px 32px rgba(6, 182, 212, 0.55);
    }

    /* ACTIVE BUTTON */
    .active-nav {
        background: linear-gradient(135deg, #1e40af, #2563eb) !important;
        color: #ffffff !important;
        box-shadow: 0 10px 32px rgba(37, 99, 235, 0.65) !important;
        transform: scale(1.12);
    }

    </style>
    """, unsafe_allow_html=True)

    # NAVBAR BUTTON ROW
    col1, col2, col3, col4, col5 = st.columns(5)

    # -------- HOME ----------
    with col1:
        if st.button("🏠 Home"):
            st.switch_page("App.py")

    # -------- LOGIN ----------
    with col2:
        if st.button("🔐 Login"):
            st.switch_page("pages/1_Login.py")

    # -------- REGISTER ----------
    with col3:
        if st.button("📝 Register"):
            st.switch_page("pages/2_Register.py")

    # -------- SUMMARIZER ----------
    with col4:
        if st.button("🧠 Summarizer"):
            st.switch_page("pages/3_Summarizer.py")

    # -------- ADMIN ----------
    with col5:
        if st.button("👑 Admin"):
            st.switch_page("pages/4_Admin.py")

# CALL NAVBAR
navbar("Home")

# -------------------------
# CUSTOM STYLING
# -------------------------
st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
    * {
        font-family: "Poppins", sans-serif !important;
    }

    /* Title */
    .main-title {
        font-size: 56px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #6a11cb, #2575fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 22px;
        text-align: center !important;
        opacity: 0.85;
        margin-bottom: 35px;
    }
    
    /* Center Get Started Button */
.start-btn {
    display: flex;
    justify-content: center;
    margin-top: 40px;     /* More spacing */
}

/* Styled Button */
.get-started-btn {
    background: linear-gradient(135deg, #ff4b2b, #ff416c); /* 🔥 Upgraded vibrant gradient */
    padding: 26px 75px;       /* Bigger Button */
    font-size: 30px;          /* Bigger Text */
    border-radius: 18px;      /* Smoother Rounded Corners */
    color: white;
    font-weight: 800;
    border: none;
    cursor: pointer;
    box-shadow: 0 12px 28px rgba(255, 65, 108, 0.45); /* Stronger shadow */
    transition: 0.3s ease;
}

/* Hover Animation */
.get-started-btn:hover {
    transform: scale(1.12);   /* Bigger animation */
    box-shadow: 0 18px 40px rgba(255, 65, 108, 0.65); /* Deeper glow */
    background: linear-gradient(135deg, #ff416c, #ff4b2b); /* Reverse gradient */
}


    /* Note */
    .note-box {
    margin-top: 35px;
    font-size: 16px;
    color: #1e3a8a;
    background: #dbeafe;   /* Light blue */
    padding: 15px;
    border-radius: 10px;
    border-left: 6px solid #3b82f6;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
    }





    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# HERO SECTION
# -------------------------
st.markdown("<div class='hero-container'>", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📝 AI Document Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Upload → Extract → Summarize → Export using AI-powered NLP</p>", unsafe_allow_html=True)

# Centered Button Block
# Centered & Styled Streamlit Button
col1, col2, col3 = st.columns([1, 2, 1])  # center layout

with col2:  # center column
    btn = st.button("🚀 Get Started", key="start_btn")

    if btn:
        st.switch_page("pages/1_Login.py")

# -------------------------
# USER NOTE SECTION
# -------------------------
st.markdown(
    """
    <div class='note-box'>
        ⭐ <b>Note:</b> Use this AI tool to quickly summarize long PDFs such as notes, books, research papers, assignments, 
        project documents, or study materials.  
        It supports <b>OCR</b>, <b>Extractive/Abstractive Summaries</b>, audio output, and multiple export formats.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
