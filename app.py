import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CHAPTER 48",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
.main, .block-container {
    background: #FDFBF7 !important;
    color-scheme: light !important;
    padding: 0 !important;
    margin: 0 !important;
    overflow: hidden !important;
}
</style>
""", unsafe_allow_html=True)

AUDIO_URL = "https://raw.githubusercontent.com/Jer523/Douglas/main/assets/brahms_op118_no2.mp3.mp3"

components.html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap" rel="stylesheet">
<style>
  * {{
    margin:0; padding:0; box-sizing:border-box;
    -webkit-user-select:none;
    user-select:none;
  }}
  html, body {{
    width:100%; height:100%;
    background:#FDFBF7;
    font-family:'Playfair Display', Georgia, serif;
    color:#4A4A4A;
    -webkit-font-smoothing:antialiased;
    overflow:hidden;
  }}
  @keyframes fadeUp {{
    from {{ opacity:0; transform:translateY(14
