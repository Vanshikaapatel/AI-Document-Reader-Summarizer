import streamlit as st
import json, os
import datetime

# ------------------ SESSION INIT ------------------
if "user" not in st.session_state:
    st.session_state.user = None

st.set_page_config(page_title="Register", layout="wide")

# ------------------- NAVBAR -------------------
def navbar(active="regiter"):
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
navbar("register")


# ------------------ USER DB ------------------
USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        return json.load(open(USERS_FILE, "r"))
    except:
        return {}

def save_users(data):
    json.dump(data, open(USERS_FILE, "w"), indent=4)

users = load_users()


# ------------------ CUSTOM STYLING ------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
}


/* Page Title */
.register-title {
    font-size: 38px;
    font-weight: 700;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.register-sub {
    color: #e8e8e8;
    font-size: 16px;
    margin-bottom: 25px;
}

/* Input fields */
.stTextInput>div>div>input {
    background: rgba(255,255,255,0.18);
    color: white;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.3);
    padding: 12px;
}

.stTextInput>div>div>input::placeholder {
    color: #cccccc;
}

/* Register button */
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
    transition: 0.3s ease;
    box-shadow: 0 5px 20px rgba(255, 65, 108, 0.4);
}

.stButton>button:hover {
    transform: scale(1.04);
    box-shadow: 0 8px 28px rgba(255, 65, 108, 0.55);
}

/* Login link */
.login-link {
    margin-top: 15px;
    color: #dcdcdc;
    font-size: 14px;
}
.login-link a {
    color: #90c9ff;
    font-weight: 600;
    text-decoration: none;
}
.login-link a:hover {
    text-decoration: underline;
}

</style>
""", unsafe_allow_html=True)


# ------------------ UI LAYOUT ------------------
st.markdown("<div class='register-box'>", unsafe_allow_html=True)

st.markdown("<div class='register-title'>📝 Create Account</div>", unsafe_allow_html=True)
st.markdown("<div class='register-sub'>Join the AI Document Summarizer Platform</div>", unsafe_allow_html=True)

username = st.text_input("Choose Username", placeholder="Enter username")
password = st.text_input("Password", type="password", placeholder="Enter password")
confirm = st.text_input("Confirm Password", type="password", placeholder="Re-enter password")


# ------------------ REGISTER LOGIC ------------------
if st.button("Register"):
    if password != confirm:
        st.error("Passwords do not match!")
    elif username in users:
        st.error("User already exists!")
    else:
        users[username] = {
            "password": password,
            "created_at": str(datetime.date.today()),
            "uploads": 0
        }
        save_users(users)
        st.success("Account created! Please login.")
        st.switch_page("pages/1_Login.py")


# Link to login
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("Already have account?🔐 Login Here"):
        st.switch_page("pages/1_Login.py")


st.markdown("</div>", unsafe_allow_html=True)
