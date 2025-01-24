import streamlit as st
from gtts import gTTS
import os

# Function to read text aloud using gTTS
def read_text(text, speed):
    tts = gTTS(text=text, lang='en', slow=(speed < 150))
    tts.save("temp_audio.mp3")
    audio_file = open("temp_audio.mp3", "rb")
    st.audio(audio_file, format="audio/mp3")
    os.remove("temp_audio.mp3")  # Clean up the file after playing

# Main content
st.set_page_config(page_title="Text Reader", layout="centered", initial_sidebar_state="collapsed")
st.title("Text Reader")
st.write("### A simple app to convert text into speech.")

# Sidebar for speed adjustment
st.sidebar.header("Settings")
speed = st.sidebar.slider("Reading Speed", min_value=50, max_value=300, value=150, step=10)

# Beautiful Text Input Section
st.markdown(
    """
    <style>
        .stTextArea textarea {
            border-radius: 10px;
            border: 1px solid #4CAF50;
            padding: 10px;
            font-size: 16px;
            width: 100%;
            box-sizing: border-box;
            height: 200px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            width: 100%;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .stTitle {
            text-align: center;
            color: #2c3e50;
        }
    </style>
    """, unsafe_allow_html=True
)

# User Input for Text
text_input = st.text_area("Enter the text you want to read aloud", "", height=200)

# Action Button to trigger speech
if st.button("Read Aloud"):
    if text_input.strip():
        read_text(text_input, speed)
    else:
        st.warning("Please enter some text to read aloud.")
        
# Footer for aesthetic
st.write("---")
st.write("Made with ❤️ using Streamlit & gTTS")
