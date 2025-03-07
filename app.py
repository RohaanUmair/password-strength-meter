import re
import streamlit as st
import string
import random

def check_password_strength(password):
    score = 0
    
    # Commonly used passwords Check
    if password == 'password123' or password == '123456':
        st.error("❌ This password is used commonly, try Another.")
        return

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
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")


# Title
st.title('Password Strength Meter')

# Get user input
password = st.text_input('Input Your Password to Check its Strength')


# Check Password Strength
if password:
    check_password_strength(password)



# Generate Strong Password
st.header('Generate Strong Password')
generate_pass_btn = st.button('Generate')


if generate_pass_btn:
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_chars = '!@#$%^&*'

    strong_password = random.sample(uppercase_letters, 2) + random.sample(lowercase_letters, 3) + random.sample(numbers, 2) + [random.choice(special_chars)]
    random.shuffle(strong_password)
    strong_password = ''.join(strong_password)

    st.success(f"🔑 Generated Password: `{strong_password}`")