import streamlit as st
import time

# 1. PAGE CONFIGURATION (Premium Title)
st.set_page_config(page_title="My Universe 🌌❤️", page_icon="💖", layout="centered")

# 2. PREMIUM CSS & HIDING BADGES (Glowing Text & Clean UI)
premium_css = """
<style>
/* Streamlit ke faltu menus hide karne ke liye */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.viewerBadge_container {display: none !important;}

/* Glowing Title Text ka Magic */
.glowing-text {
    font-size: 45px;
    font-weight: 900;
    text-align: center;
    background: -webkit-linear-gradient(45deg, #ff007f, #ff7eb3);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 2s ease-in-out infinite alternate;
    margin-bottom: 20px;
}
@keyframes glow {
    from {text-shadow: 0 0 10px #ff7eb3, 0 0 20px #ff007f;}
    to {text-shadow: 0 0 20px #ff7eb3, 0 0 30px #ff007f;}
}

/* Floating Hearts Background (Romantic Vibe) */
.heart-bg {
    position: fixed;
    font-size: 25px;
    z-index: -1;
    opacity: 0.4;
    animation: floatUp infinite linear;
}
@keyframes floatUp {
    0% { bottom: -10%; transform: translateX(0px) rotate(0deg); }
    100% { bottom: 120%; transform: translateX(30px) rotate(360deg); }
}
</style>

<div class="heart-bg" style="left: 10%; animation-duration: 8s;">💖</div>
<div class="heart-bg" style="left: 40%; animation-duration: 12s;">💕</div>
<div class="heart-bg" style="left: 70%; animation-duration: 9s;">✨</div>
<div class="heart-bg" style="left: 90%; animation-duration: 15s;">❤️</div>
"""
st.markdown(premium_css, unsafe_allow_html=True)

# 3. GLOWING MAIN TITLE
st.markdown('<div class="glowing-text">You Are My Universe 🌌💖</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: gray;'>Designed with love, strictly for you.</p>", unsafe_allow_html=True)
st.divider()

# 4. HIGH-QUALITY PICTURE SECTION
# (Koshish karna yahan koi ultra-HD 4K jaisi clear photo lagao, aur bhi premium lagega!)
try:
    st.image("our_picture.jpg", use_container_width=True, caption="The best thing that ever happened to me ✨")
except Exception as e:
    st.info("*(Picture load nahi hui. 'our_picture.jpg' naam check kar lena GitHub par!)*")

# 5. INTERACTIVE LOVE METER (Slider)
st.write("### 🎚️ How much do I love you?")
love_score = st.slider("", min_value=0, max_value=100, value=10)

if love_score == 100:
    st.success("Wait... the meter just broke! My love for you is infinity! 🚀💖")
    st.balloons()
elif love_score > 50:
    st.info("Keep going... it's way more than this! 😉")
else:
    st.warning("Slide it all the way to the right! 👉")

st.divider()

# 6. SECRET LOVE VAULT (Expander - Click to open)
st.write("### 🔐 A Secret Vault just for you")
with st.expander("Click here to unlock my heart 🔓"):
    st.write("""
    **Mere Dil Ki Baat:**
    Ap meri zindagi ka wo hissa ho jise main kabhi khona nahi chahta. 
    Ap ki har chhoti-chhoti aadat, Ap ki smile, aur Ap ki  baatein mere din ko perfect bana deti hain. 
    
    *I promise to always annoy you, protect you, and love you endlessly!* 🥰
    """)

st.divider()

# 7. THE FINAL SURPRISE BUTTON
st.write("### 🎁 One Last Surprise...")
if st.button("Touch this magical button ✨"):
    with st.spinner("Casting a love spell... 🪄"):
        time.sleep(2)
    
    # Toast notification (Chota sa popup jo neeche se aata hai)
    st.toast("I Love You! ❤️", icon="😍")
    st.toast("Forever & Always! ♾️", icon="💖")
    
    st.success("You are my Princes, the most beautiful girl in the world! 🌹")
    st.snow() # Magical snow effect
