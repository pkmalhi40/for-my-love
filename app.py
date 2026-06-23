import streamlit as st
import streamlit.components.v1 as components
import time

# 1. Page Configuration (Browser tab title aur icon)
st.set_page_config(page_title="For My Love ❤️", page_icon="🌹", layout="centered")

# 2. === THE REAL CODER'S MAGIC (JavaScript Auto-Redirect) ===
# Ye script background me chalegi aur automatic URL me embed=true laga degi
components.html(
    """
    <script>
        const currentUrl = window.parent.location.href;
        if (!currentUrl.includes('embed=true')) {
            // Agar link me embed nahi hai, toh automatic add karke page reload kardo
            window.parent.location.href = currentUrl + (currentUrl.includes('?') ? '&' : '?') + 'embed=true';
        }
    </script>
    """,
    height=0, width=0
)
# ============================================================

# 3. CSS for extra safety (Top menu aur footer hide karne ke liye)
hide_css = """
<style>
#MainMenu {visibility: hidden !important;}
header {visibility: hidden !important;}
footer {visibility: hidden !important;}
</style>
"""
st.markdown(hide_css, unsafe_allow_html=True)

# 4. Jaise hi page open hoga, balloons udenge!
st.balloons()

# 5. The Main Message
st.title("I Love You So Much! ❤️🥰")
st.subheader("I coded this special page just for you.")

st.divider() # Ek pyari si line

# 6. Picture Setup (width=350 set kar diya hai mobile view ke liye)
try:
    st.image("our_picture.jpeg", width=350, caption="My absolute favorite memory of us! 📸✨")
except:
    st.info("*(Note to you: Picture load nahi hui. Make sure GitHub par file ka naam exactly 'our_picture.jpg' hai!)*")

# 7. A sweet custom message using emojis
st.markdown("""
### Why you are my favorite person in the world:
* Your amazing smile that lights up my day 😊
* How you always know how to make me laugh 😂
* You are my best friend and my everything 🌟

No matter where we are, you always feel like home to me. 🏡💕
""")

st.divider()

# 8. Interactive Surprise Button
if st.button("Click here for a surprise 🎁"):
    with st.spinner("Opening your surprise..."):
        time.sleep(2) # 2 second ka suspense
    st.success("You are the most beautiful girl in the world! 😘💖")
    st.snow() # Snow animation chalegi
