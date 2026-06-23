import streamlit as st
import time

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="I am Sorry 🥺", page_icon="💔", layout="centered")

# 2. HIDE STREAMLIT MENU & BADGES
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. ALL ANIMATIONS (Floating Emojis, Pulsing Text, Wiggling Teddy)
custom_animations = """
<style>
/* Floating Emojis Animation */
@keyframes floatUp {
    0% { transform: translateY(0px) rotate(0deg); opacity: 1; }
    100% { transform: translateY(-800px) rotate(360deg); opacity: 0; }
}
.floating-emoji {
    position: fixed;
    bottom: -50px;
    font-size: 35px;
    z-index: 9999;
    animation: floatUp 6s linear infinite;
    pointer-events: none;
}

/* Pulsing Text Animation */
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); color: #ff4b4b; }
    100% { transform: scale(1); }
}
.sorry-text {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #ff3333;
    animation: pulse 2s infinite;
}

/* Wiggling Teddy Bear */
@keyframes wiggle {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(-15deg); }
    50% { transform: rotate(0deg); }
    75% { transform: rotate(15deg); }
    100% { transform: rotate(0deg); }
}
.wiggle-teddy {
    font-size: 80px;
    text-align: center;
    animation: wiggle 2s infinite;
}
</style>

<div class="floating-emoji" style="left: 15%; animation-duration: 4.5s; animation-delay: 0s;">🥺</div>
<div class="floating-emoji" style="left: 35%; animation-duration: 5.2s; animation-delay: 1.2s;">😭</div>
<div class="floating-emoji" style="left: 55%; animation-duration: 3.8s; animation-delay: 0.5s;">🙏</div>
<div class="floating-emoji" style="left: 75%; animation-duration: 4.9s; animation-delay: 2.1s;">💔</div>
<div class="floating-emoji" style="left: 85%; animation-duration: 6.1s; animation-delay: 0.8s;">🥺</div>
"""
st.markdown(custom_animations, unsafe_allow_html=True)

# 4. MAIN VISUALS
st.markdown('<div class="wiggle-teddy">🧸</div>', unsafe_allow_html=True)
st.markdown('<div class="sorry-text">I am So Sorry!</div>', unsafe_allow_html=True)

st.write("---")

# 5. THE APOLOGY MESSAGE
st.markdown("""
### Please forgive me... 🥺
Mujhse galti ho gayi. Tumhare bina sab kuch adhoora lagta hai. 
Main janta hoon maine tumhe hurt kiya, par mera intention kabhi wo nahi tha.
Tum meri smile ho, meri best friend ho, aur mera sab kuch ho.

**Meri is galti ko chota sa samajh kar maaf kar do na? Please?** 🙏
""")

st.write("---")

# 6. INTERACTIVE FORGIVENESS BUTTONS
st.write("### Will you forgive me? 🥺")

# Do buttons ko side-by-side rakhne ke liye columns
col1, col2 = st.columns(2)

with col1:
    if st.button("Yes, I Forgive You ❤️"):
        st.balloons() # Maaf karne par khushi ke balloons!
        st.success("Yayyy! Thank you so much! You are the best! I love you! 🥰💖")

with col2:
    if st.button("No, I'm still mad 😤"):
        st.error("Ouch... Pleaseee maan jao na! 😭 (Click the other button!)")
