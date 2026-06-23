import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="For My Love ❤️", page_icon="🌹", layout="centered")

# 2. === THE ULTIMATE BADGE KILLER CSS ===
hide_badge = """
<style>
#MainMenu {visibility: hidden !important;}
footer {visibility: hidden !important;}
header {visibility: hidden !important;}
.viewerBadge_container {display: none !important;}
.viewerBadge_link {display: none !important;}
div[class^="viewerBadge"] {display: none !important;}
iframe[title="Streamlit Community Cloud badge"] {display: none !important;}
iframe[src^="https://share.streamlit.io"] {display: none !important;}
</style>
"""
st.markdown(hide_badge, unsafe_allow_html=True)
# =====================================

# 3. === MAGICAL FLOATING HEARTS BACKGROUND ===
# (Yahan st.balloons() ko hata kar hearts lagaye gaye hain)
st.markdown("""
<style>
.heart {
    position: fixed;
    font-size: 2.5rem;
    z-index: 99999;
    pointer-events: none;
    animation: floatUp infinite ease-in;
}
@keyframes floatUp {
    0% { bottom: -10%; opacity: 1; transform: translateX(0px) rotate(0deg) scale(1); }
    100% { bottom: 120%; opacity: 0; transform: translateX(50px) rotate(360deg) scale(1.5); }
}
</style>
<div class="heart" style="left: 10%; animation-duration: 4s; animation-delay: 0s;">❤️</div>
<div class="heart" style="left: 30%; animation-duration: 5s; animation-delay: 1s;">💖</div>
<div class="heart" style="left: 50%; animation-duration: 3.5s; animation-delay: 0.5s;">💕</div>
<div class="heart" style="left: 70%; animation-duration: 4.5s; animation-delay: 2s;">💓</div>
<div class="heart" style="left: 85%; animation-duration: 6s; animation-delay: 0.8s;">💘</div>
""", unsafe_allow_html=True)
# ==========================================

# 4. The Main Message
st.title("I Love You So Much! ❤️🥰")
st.title("Namaste ❤️💕😊")  
st.subheader("I coded this special page just for you.")

st.divider() 

# 5. Picture Setup 
try:
    st.image("our_picture.jpg", width=350, caption="My absolute favorite memory of us! 📸✨")
except:
    st.info("*(Note to you: Picture load nahi hui. Make sure GitHub par file ka naam exactly 'our_picture.jpg' hai!)*")

# 6. A sweet custom message using emojis
st.markdown("""
### Why you are my favorite person in the world:
* Your amazing smile that lights up my day 😊
* How you always know how to make me laugh 😂
* You are my best friend and my everything 🌟

No matter where we are, you always feel like home to me. 🏡💕
""")

st.divider()

# 7. Interactive Surprise Button
if st.button("Click here for a surprise 🎁"):
    with st.spinner("Opening your surprise..."):
        time.sleep(2) 
    st.success("You are the most beautiful girl in the world! 😘💖")
    st.snow() # Button click par snow giregi
