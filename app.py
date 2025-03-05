import re
import streamlit as st

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        st.text("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.text("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        st.text("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.text("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        st.text("✅ Strong Password!")
    elif score == 3:
        st.text("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.text("❌ Weak Password - Improve it using the suggestions above.")


# Title
st.title('Password Strength Meter')

# Get user input
password = st.text_input('Input Your Password to Check its Strength')


# Check Password Strength
if password:
    check_password_strength(password)