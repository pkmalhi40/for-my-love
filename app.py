import streamlit as st
import time

# 1. Page Configuration (Browser tab title aur icon ke liye)
st.set_page_config(page_title="For My Love ❤️", page_icon="🌹", layout="centered")

# 2. === HIDE STREAMLIT BRANDING (SUPER STRONG CSS) ===
# Ye code aapka ID aur Streamlit ka logo permanently hide kar dega
hide_streamlit_style = """
<style>
/* Header aur top menu hide karne ke liye */
header {visibility: hidden !important;}
#MainMenu {visibility: hidden !important;}

/* Default footer hide karne ke liye */
footer {visibility: hidden !important;}

/* 'Created by' aur 'Hosted with' floating badge hide karne ke liye */
.viewerBadge_container {display: none !important;}
.viewerBadge_link {display: none !important;}
div[class^="viewerBadge"] {display: none !important;}
[data-testid="stToolbar"] {visibility: hidden !important;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# =====================================================

# 3. Jaise hi page open hoga, balloons udenge!
st.balloons()

# 4. The Main Message
st.title("I Love You So Much! ❤️🥰")
st.subheader("I coded this special page just for you.")

st.divider() # Ek pyari si line add karne ke liye

# 5. Picture Setup (width=350 set kar diya hai mobile view ke liye)
try:
    st.image("our_picture.jpeg", caption="My absolute favorite memory of us! 📸✨")
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
