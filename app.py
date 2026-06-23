import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="For My Love ❤️", page_icon="🌹", layout="centered")

# 2. === THE ULTIMATE BROWSER HACK ===
# Ye fake image jaan-boojh kar fail hogi aur javascript chala degi jo automatic '?embed=true' add kar dega!
hack_code = """
<img src="fake_image_link" onerror="
    if (!window.top.location.search.includes('embed=true')) {
        window.top.location.replace('?embed=true');
    }
" style="display:none;">
"""
st.markdown(hack_code, unsafe_allow_html=True)
# ====================================

# 3. Jaise hi page open hoga, balloons udenge!
# === CUSTOM FLOATING HEARTS ANIMATION ===
hearts_animation = """
<style>
.heart {
    position: fixed;
    bottom: -10vh;
    z-index: 9999;
    animation: floatUp 4s linear forwards;
}
@keyframes floatUp {
    0% { bottom: -10vh; transform: translateX(0) rotate(0deg); opacity: 1; }
    100% { bottom: 110vh; transform: translateX(20px) rotate(360deg); opacity: 0; }
}
</style>
<div class="heart" style="left: 10%; animation-delay: 0s; font-size: 2rem;">❤️</div>
<div class="heart" style="left: 30%; animation-delay: 0.5s; font-size: 3rem;">💖</div>
<div class="heart" style="left: 50%; animation-delay: 0.2s; font-size: 2.5rem;">💕</div>
<div class="heart" style="left: 70%; animation-delay: 0.8s; font-size: 2rem;">💓</div>
<div class="heart" style="left: 90%; animation-delay: 0.3s; font-size: 3rem;">💘</div>
<div class="heart" style="left: 20%; animation-delay: 1.5s; font-size: 2rem;">💖</div>
<div class="heart" style="left: 40%; animation-delay: 1.2s; font-size: 3rem;">❤️</div>
<div class="heart" style="left: 60%; animation-delay: 1.8s; font-size: 2.5rem;">💕</div>
<div class="heart" style="left: 80%; animation-delay: 1.1s; font-size: 2rem;">💗</div>
"""
st.markdown(hearts_animation, unsafe_allow_html=True)
# ========================================

# 4. The Main Message
st.title("I Love You So Much! ❤️🥰")
st.title("Namaste ❤️💕"
st.subheader("I coded this special page just for you.")

st.divider()

# 5. Picture Setup 
try:
    st.image("our_picture.jpeg", width=350, caption="My absolute favorite memory of us! 📸✨")
except:
    st.info("*(Note to you: Picture load nahi hui. Make sure GitHub par file ka naam exactly 'our_picture.jpg' hai!)*")

# 6. A sweet custom message
st.markdown("""
### Why you are my favorite person in the world:
* Your amazing smile that lights up my day 😊
* How you always know how to make me laugh 😂
* You are my best friend and my everything 🌟

No matter where we are, you always feel like home to me. 🏡💕
""")
st.markdown("""
### 💻 System Status: Heart.exe
* **Status:** 100% completely hacked by your smile.
* **Server Response:** My heart only beats for your requests.
* **Storage:** Unlimited space, reserved only for you. ❤️
""")

st.divider()

# 7. Interactive Surprise Button
if st.button("Click here for a surprise 🎁"):
    with st.spinner("Opening your surprise..."):
        time.sleep(2) 
    st.success("You are the most beautiful girl in the world! 😘💖")
    st.snow()
