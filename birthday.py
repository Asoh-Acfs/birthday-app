import streamlit as st
from datetime import date
from PIL import Image
import streamlit.components.v1 as components

# App setup
st.set_page_config(page_title="Happy Birthday Umma Hani!", layout="centered")

# Confetti Animation
components.html("""
    <script src="https://cdn.jsdelivr.net/npm/confetti-js@0.0.18/dist/index.min.js"></script>
    <canvas id="confetti-canvas" style="position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;"></canvas>
    <script>
    var confettiSettings = { target: 'confetti-canvas', max: 150, size: 1.2, animate: true };
    var confetti = new ConfettiGenerator(confettiSettings);
    confetti.render();
    </script>
""", height=0)

# Title and name
st.title("**Happy 17th Birthday, Gambo Musa Umma Hani!**")
st.markdown("### Wishing you the most beautiful and joyful year ahead!")

# Age info
birthday_year = date.today().year - 17
st.markdown(f"**Born in {birthday_year}, and now you're 17 — a shining star full of purpose and grace!**")

# Birthday prayer
st.markdown("---")
st.markdown("### A Birthday Prayer for You")
st.markdown("""
*May Allah (SWT) bless you abundantly in this new age.  
May He protect you, guide your steps, and fill your heart with joy, peace, and faith.  
May all your dreams come true in the most beautiful way, and may you grow in wisdom and strength.  
Ameen.*  
""")

# Birthday quote
st.markdown("---")
st.markdown("### Birthday Quote")
st.markdown("> *“Every year of your life is a beautiful story written by Allah. Let this chapter be your best one yet.”*")

# Load the first image
image1 = Image.open('umma1.png')
st.image(image1, caption='I swear you are so beautiful', use_container_width=True)

# Load the second image
image2 = Image.open('umma2.png')
st.image(image2, caption='Forget filter, you too fine, omo Alaja', use_container_width=True)

# Balloons
st.balloons()
