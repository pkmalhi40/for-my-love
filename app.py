import streamlit as st
import streamlit.components.v1 as components

# Screen ka layout set karna
st.set_page_config(page_title="A Special Question...", layout="wide")

# Custom HTML, CSS, aur JavaScript jo magic karega
romantic_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proposal</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 90vh;
            background-color: #ffe6e6;
            font-family: 'Comic Sans MS', cursive, sans-serif;
            text-align: center;
            overflow: hidden;
            margin: 0;
        }
        h1 {
            color: #ff4d4d;
            font-size: 3em;
            margin-bottom: 50px;
        }
        .btn {
            font-size: 24px;
            padding: 15px 40px;
            margin: 20px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: bold;
            transition: 0.3s;
        }
        #yesBtn {
            background-color: #ff4d4d;
            color: white;
            box-shadow: 0 4px 15px rgba(255, 77, 77, 0.4);
        }
        #yesBtn:hover {
            background-color: #ff1a1a;
            transform: scale(1.1);
        }
        #noBtn {
            background-color: #cccccc;
            color: black;
            position: absolute; /* Ye zaroori hai bhaagne ke liye */
        }
        #animation-container {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #ffe6e6;
            z-index: 999;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        #animation-container h1 {
            font-size: 5em;
            animation: heartbeat 1s infinite alternate;
        }
        @keyframes heartbeat {
            from { transform: scale(1); }
            to { transform: scale(1.2); }
        }
        .heart {
            color: red;
            font-size: 40px;
            position: absolute;
            animation: fall 3s linear infinite;
        }
        @keyframes fall {
            to { transform: translateY(100vh); }
        }
    </style>
</head>
<body>

    <div id="main-content">
        <h1>Payal, will you marry me? 💍</h1>
        
        <button id="yesBtn" onclick="sayYes()">Yes! ❤️</button>
        <button id="noBtn" onmouseover="moveNoButton()" onclick="moveNoButton()">No 😢</button>
    </div>

    <div id="animation-container">
        <h1>I LOVE YOU! 💖🎉</h1>
    </div>

    <script>
        function moveNoButton() {
            var btn = document.getElementById('noBtn');
            // Screen ki width aur height ke hisab se random position nikalna
            var x = Math.random() * (window.innerWidth - btn.offsetWidth);
            var y = Math.random() * (window.innerHeight - btn.offsetHeight);
            
            btn.style.left = x + 'px';
            btn.style.top = y + 'px';
        }

        function sayYes() {
            document.getElementById('main-content').style.display = 'none';
            var animContainer = document.getElementById('animation-container');
            animContainer.style.display = 'flex';

            // Barish wale hearts banana
            for (let i = 0; i < 50; i++) {
                let heart = document.createElement('div');
                heart.innerHTML = '❤️';
                heart.className = 'heart';
                heart.style.left = Math.random() * 100 + 'vw';
                heart.style.animationDuration = (Math.random() * 2 + 2) + 's';
                animContainer.appendChild(heart);
            }
        }
    </script>
</body>
</html>
"""

# HTML ko Streamlit mein poori screen par dikhana
components.html(romantic_html, height=700, scrolling=False)
