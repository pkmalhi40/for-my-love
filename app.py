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
    st.image("our_picture.jpg", caption="My absolute favorite memory of us! 📸✨")
except:
    st.info("*(Note to you: Put an image named 'our_picture.jpg' in the folder to see it here!)*")

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