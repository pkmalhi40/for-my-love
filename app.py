import streamlit as st
import time

# 1. Page Configuration (Browser tab title aur icon)
st.set_page_config(page_title="For My Love ❤️", page_icon="🌹", layout="centered")

# 2. === THE ULTIMATE BADGE KILLER CSS ===
# Ye Streamlit ka logo, menu, aur badge block kar dega
hide_badge = """
<style>
/* Header aur footer hide karne ke liye */
#MainMenu {visibility: hidden !important;}
footer {visibility: hidden !important;}
header {visibility: hidden !important;}

/* Streamlit Cloud floating badge block karne ke liye */
.viewerBadge_container {display: none !important;}
.viewerBadge_link {display: none !important;}
div[class^="viewerBadge"] {display: none !important;}

/* Naya iframe blocker */
iframe[title="Streamlit Community Cloud badge"] {display: none !important;}
iframe[src^="https://share.streamlit.io"] {display: none !important;}
</style>
"""
st.markdown(hide_badge, unsafe_allow_html=True)
# =====================================

# 3. Jaise hi page open hoga, balloons udenge!
st.balloons()

# 4. The Main Message
st.title("I Love You So Much! ❤️🥰")
st.subheader("I coded this special page just for you.")

st.divider() # Ek pyari si line

# 5. Picture Setup (width=350 set kar diya hai mobile view ke liye)
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
        time.sleep(2) # 2 second ka suspense
    st.success("You are the most beautiful girl in the world! 😘💖")
    st.snow() # Snow animation chalegi
