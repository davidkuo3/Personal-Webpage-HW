import streamlit as st
import streamlit.components.v1 as components
import os

# Set page config
st.set_page_config(
    page_title="郭子熠 | 個人主頁",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit elements with CSS
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp {
                margin: 0;
                padding: 0;
            }
            iframe {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                border: none;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML in full-screen iframe
components.html(html_content, height=1000) # Height will be overridden by CSS iframe style above
