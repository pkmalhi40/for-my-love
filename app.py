import streamlit as st
import time

# 1. PAGE CONFIGURATION (Yeh hamesha sabse upar hona chahiye warna app crash hoti hai)
st.set_page_config(page_title="For My Love ❤️", page_icon="🌹", layout="centered")

# 2. HIDE STREAMLIT EXTRA LOGOS & MENU
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.viewerBadge_container {display: none !important;}
.viewerBadge_link {display: none !important;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. FLOATING HEARTS ANIMATION (Balloons ki jagah ❤️ hawa me udenge)
floating_hearts_css = """
<style>
@keyframes floatingHeart {
    0% { transform: translateY(0px) rotate(0deg); opacity: 1; }
    100% { transform: translateY(-1000px) rotate(360deg); opacity: 0; }
}
.floating-heart {
    position: fixed;
    bottom: -50px;
    font-size: 32px;
    user-select: none;
    pointer-events: none;
    z-index: 999999;
    animation: floatingHeart 5s linear infinite;
}
</style>
<div class="floating-heart" style="left: 15%; animation-duration: 4.5s; animation-delay: 0s;">❤️</div>
<div class="floating-heart" style="left: 35%; animation-duration: 5.2s; animation-delay: 1.2s;">💖</div>
<div class="floating-heart" style="left: 55%; animation-duration: 3.8s; animation-delay: 0.5s;">💕</div>
<div class="floating-heart" style="left: 75%; animation-duration: 4.9s; animation-delay: 2.1s;">💓</div>
<div class="floating-heart" style="left: 85%; animation-duration: 6.1s; animation-delay: 0.8s;">💘</div>
"""
st.markdown(floating_hearts_css, unsafe_allow_html=True)

# 4. MAIN TITLES
st.title("I Love You So Much! ❤️🥰")
st.subheader("I coded this special page just for you.")

st.divider() 

# 5. PICTURE SETUP (Safe loading ke sath)
try:
    st.image("our_picture.jpg", width=350, caption="My absolute favorite memory of us! 📸✨")
except Exception as e:
    st.info("*(Note to you: Picture load nahi hui. Make sure GitHub par file ka naam exactly 'our_picture.jpg' hai!)*")

# 6. ROMANTIC TEXT
st.markdown("""
### Why you are my favorite person in the world:
* Your amazing smile that lights up my day 😊
* How you always know how to make me laugh 😂
* You are my best friend and my everything 🌟

No matter where we are, you always feel like home to me. 🏡💕
""")

st.divider()

# 7. SURPRISE BUTTON
if st.button("Click here for a surprise 🎁"):
    with st.spinner("Opening your surprise..."):
        time.sleep(2) 
    st.success("You are the most beautiful girl in the world! 😘💖")
    st.snow()
