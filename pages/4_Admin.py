import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="Admin", layout="wide")

import streamlit as st

def navbar(active="Admin"):
    st.markdown("""
    <style>
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 35px;
        padding: 18px;
        margin-bottom: 15px;
    }

    .nav-btn {
        padding: 8px 22px;
        border-radius: 8px;
        background: rgba(255,255,255,0.08);
        cursor: pointer;
        color: #e0e0e0;
        font-weight: 600;
        text-decoration: none;
        transition: 0.3s;
    }
    .nav-btn:hover {
        background: rgba(255,255,255,0.18);
        transform: translateY(-2px);
    }

    .active {
        background: linear-gradient(90deg,#6a11cb,#2575fc);
        color: white !important;
        box-shadow: 0 4px 12px rgba(37,117,252,0.4);
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- NAVBAR BUTTONS ----------
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("Home", key="home_btn"):
            st.switch_page("App.py")

    with col2:
        if st.button("Login", key="login_btn"):
            st.switch_page("pages/1_Login.py")

    with col3:
        if st.button("Register", key="register_btn"):
            st.switch_page("pages/2_Register.py")

    with col4:
        if st.button("Summarizer", key="summ_btn"):
            st.switch_page("pages/3_Summarizer.py")

    with col5:
        if st.button("Admin", key="admin_btn"):
            st.switch_page("pages/4_Admin.py")
            navbar("Admin")


# Check if logged in
if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first.")
    st.stop()

# Only admin allowed (define admin username)
ADMIN_USERNAME = "Admin"

if st.session_state.user != ADMIN_USERNAME:
    st.error("Access denied. You are not an admin.")
    st.stop()

# Load users
users = json.load(open("users.json"))

st.title("🛠 Admin Dashboard")
st.markdown("### Manage Users & View Analytics")

# Convert user data to table
table_data = []

for username, details in users.items():

    # If the user entry is old format (only password)
    if isinstance(details, str):
        # Convert it to new format
        details = {
            "password": details,
            "created_at": "N/A",
            "upload_count": 0,
            "summary_count": 0
        }
        users[username] = details
        json.dump(users, open("users.json", "w"), indent=4)

    table_data.append({
        "Username": username,
        "Created On": details.get("created_at", "N/A"),
        "Uploads": details.get("upload_count", 0),
        "Summaries": details.get("summary_count", 0)
    })


df = pd.DataFrame(table_data)

st.dataframe(df, use_container_width=True)

# Analytics Section
st.subheader("📊 Usage Analytics")

total_users = len(users)
total_uploads = sum(d.get("upload_count", 0) for d in users.values())
total_summaries = sum(d.get("summary_count", 0) for d in users.values())

col1, col2, col3 = st.columns(3)
col1.metric("👥 Total Users", total_users)
col2.metric("📁 Total Uploads", total_uploads)
col3.metric("📝 Summaries Generated", total_summaries)

