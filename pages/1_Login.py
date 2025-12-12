import streamlit as st
import json, os

# ------------------ SESSION INIT ------------------
if "user" not in st.session_state:
    st.session_state.user = None

st.set_page_config(page_title="Login", layout="wide")

# ------------------- NAVBAR -------------------
def navbar(active="login"):
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
            st.switch_page("app.py")

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
            st.switch_page("pages/4_AdminPanel.py")
            
# CALL NAVBAR
navbar("login")
            


# ------------------ USER DB ------------------
USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        return json.load(open(USERS_FILE, "r"))
    except:
        return {}

users = load_users()


# ------------------ CUSTOM STYLING ------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
}


/* Heading */
.login-title {
    font-size: 40px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 10px;
}

/* Subtitle */
.login-sub {
    color: #dcdcdc;
    font-size: 16px;
    margin-bottom: 25px;
}

/* Input fields */
.stTextInput>div>div>input {
    background: rgba(255,255,255,0.15);
    color: white;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.25);
    padding: 12px;
}

.stTextInput>div>div>input::placeholder {
    color: #cccccc;
}

/* Login button */
.stButton>button {
    width: 100%;
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    padding: 12px 0;
    font-size: 18px;
    border-radius: 10px;
    border: none;
    color: white;
    font-weight: 600;
    margin-top: 15px;
    transition: 0.3s;
    box-shadow: 0 5px 20px rgba(37,117,252,0.35);
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0 8px 25px rgba(37,117,252,0.55);
}

/* Register link */
.register-link {
    margin-top: 15px;
    color: #dcdcdc;
    font-size: 14px;
}
.register-link a {
    color: #76a9ff;
    font-weight: 600;
    text-decoration: none;
}
.register-link a:hover {
    text-decoration: underline;
}

</style>
""", unsafe_allow_html=True)



# ------------------ UI LAYOUT ------------------
st.markdown("<div class='login-box'>", unsafe_allow_html=True)

st.markdown("<div class='login-title'>🔐 Login</div>", unsafe_allow_html=True)
st.markdown("<div class='login-sub'>Access your AI Document Summarizer account</div>", unsafe_allow_html=True)

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", type="password", placeholder="Enter your password")


# ------------------ LOGIN LOGIC ------------------
if st.button("Login"):
    if username in users and users[username]["password"] == password:
        st.success("Login Successful! Redirecting…")
        st.session_state.user = username
        
        # FIX: Correct page path
        st.switch_page("pages/3_Summarizer.py")

    else:
        st.error("Invalid username or password ❌")


# Register page link
st.markdown("<br>", unsafe_allow_html=True)

# Register page link (FIXED)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("Not have an account? 🔐 Create one"):
        st.switch_page("pages/2_Register.py")



st.markdown("</div>", unsafe_allow_html=True)
