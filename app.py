import streamlit as st
import time

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Only Yours 🥺❤️", page_icon="💖", layout="centered")

# 2. HIDE STREAMLIT BADGES & EXTRA MENUS
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.viewerBadge_container {display: none !important;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. FLOATING HEARTS BACKGROUND (Continuous Romantic Vibe)
hearts_bg = """
<style>
.heart-bg {
    position: fixed;
    font-size: 28px;
    z-index: -1;
    opacity: 0.6;
    animation: floatUp infinite linear;
}
@keyframes floatUp {
    0% { bottom: -10%; transform: translateX(0px) rotate(0deg) scale(1); }
    100% { bottom: 120%; transform: translateX(40px) rotate(360deg) scale(1.5); }
}
</style>
<div class="heart-bg" style="left: 10%; animation-duration: 6s; animation-delay: 0s;">❤️</div>
<div class="heart-bg" style="left: 30%; animation-duration: 8s; animation-delay: 2s;">💖</div>
<div class="heart-bg" style="left: 50%; animation-duration: 5s; animation-delay: 1s;">💕</div>
<div class="heart-bg" style="left: 70%; animation-duration: 7s; animation-delay: 3s;">💓</div>
<div class="heart-bg" style="left: 85%; animation-duration: 9s; animation-delay: 0.5s;">💘</div>
"""
st.markdown(hearts_bg, unsafe_allow_html=True)

# 4. GLOWING HEADING CSS
glowing_text_css = """
<style>
.glow-text {
    font-size: 40px;
    font-weight: 900;
    text-align: center;
    background: -webkit-linear-gradient(45deg, #ff3366, #ff9933);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 2s ease-in-out infinite alternate;
}
@keyframes glow {
    from {text-shadow: 0 0 5px #ff9933, 0 0 10px #ff3366;}
    to {text-shadow: 0 0 15px #ff9933, 0 0 25px #ff3366;}
}
</style>
"""
st.markdown(glowing_text_css, unsafe_allow_html=True)

# --- MAIN APP UI STARTS HERE ---

st.markdown('<div class="glow-text">The Two Sides of Me 🎭❤️</div>', unsafe_allow_html=True)
st.write("")

# 5. THE PERSONALITY SWITCH (Interactive Radio Buttons)
st.write("### 🔍 Select who I am talking to:")
persona = st.radio("", ["The Rest of the World 🌍", "You (My Whole World) 💖"], index=0)

st.divider()

# 6. DYNAMIC CONTENT BASED ON SELECTION
if persona == "The Rest of the World 🌍":
    st.error("😎 **Status:** 100% Attitude | Careless | Thoda Harami")
    st.markdown("""
    **Duniya ke liye mera rule simple hai:**
    Mujhe kisi ki parwah nahi hai. Main jaisa bhi hoon, thoda harami, thoda badtameez, aur apne dosto ke sath bilkul careless. 
    Duniya ke samne mera koi 'soft' version nahi hai. Jo bhi hai, yahi hai! 🤷‍♂️
    """)
    st.info("*(Now click on the 2nd option to see the truth...)*")

elif persona == "You (My Whole World) 💖":
    st.success("🥺 **Status:** 0% Attitude | 100% Loyal | Pighal Gaya!")
    st.markdown("""
    **Par Apke liye sachai kuch aur hi hai...**
    Duniya chahe mujhe jaisa bhi samjhe, par Apke  saamne aate hi mera saara 'harami-pan' gayab ho jata hai. 
    Apke  liye main duniya ka sabse seedha, caring aur loyal insaan hoon. 
    
    Kyunki jab Ap mere paas hoti ho, toh mera dil sirf aur sirf Apka ban kar reh jata hai. ❤️
    """)
    
    st.write("---")
    
    # Hand Holding Message inside her special section
    st.write("### 🤝 The safest place in the world...")
    st.markdown("""
    Jab Apka haath mere haathon mein hota hai, toh lagta hai jaise waqt wahin ruk gaya ho. 
    Apke haathon ki wo narmi aur unhe thaam kar chalne ka ehsaas... mere liye duniya ki sabse keemti feeling hai. 
    Meri bas yahi khwahish hai ki in haathon ko main apni aakhri saans tak aise hi thaam kar rakhun. 👩‍❤️‍👨
    """)

st.divider()

# 7. FINAL LOVE BUTTON
if st.button("Click to see my Final Confession 💌"):
    with st.spinner("Decoding my heart for you..."):
        time.sleep(2)
    st.success("Sari duniya ek taraf, aur Apka pyaar ek taraf! I am completely, madly, and forever in love with you! 😘🌹")
    st.snow() # Sweet sparkling effect at the end
