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
st.balloons()

# 4. The Main Message
st.title("I Love You So Much! ❤️🥰")
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

st.divider()

# 7. Interactive Surprise Button
if st.button("Click here for a surprise 🎁"):
    with st.spinner("Opening your surprise..."):
        time.sleep(2) 
    st.success("You are the most beautiful girl in the world! 😘💖")
    st.snow()
