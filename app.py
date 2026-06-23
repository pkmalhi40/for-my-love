import streamlit as st
import time

# 1. Page Configuration (This sets the tab title and icon)
st.set_page_config(page_title="For My Love ❤️", page_icon="🌹", layout="centered")

# 2. Trigger a cute balloon animation when she opens the link!
st.balloons()

# 3. The Main Message
st.title("I Love You So Much! ❤️🥰")
st.subheader("I coded this special page just for you.")

st.divider() # Adds a nice horizontal line

# 4. Add your favorite picture
# Make sure "our_picture.jpg" is in the same folder as this script.
try:
    st.image("our_picture.jpeg", caption="You Changed Me Alot! 📸✨")
except:
    st.info("*(Note to you: Put an image named 'our_picture.jpeg' in the folder to see it here!)*")
# === HIDE STREAMLIT BRANDING (SUPER STRONG) ===
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
# ==============================================
# 5. A sweet custom message using emojis
st.markdown("""
### Why you are my favorite person in the world:
* Your amazing smile that lights up my day 😊
* How you always know how to make me laugh 😂
* You are my best friend and my everything 🌟

No matter where we are, you always feel like home to me. 🏡💕
""")

st.divider()

# 6. Interactive Surprise Button
if st.button("Click here for a surprise 🎁"):
    with st.spinner("Opening your surprise..."):
        time.sleep(2) # Pauses for 2 seconds for suspense
    st.success("You are the most beautiful girl in the world! 😘💖")
    st.snow() # Triggers a snow animation
