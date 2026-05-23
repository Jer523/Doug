import streamlit as st
import os
import base64

st.set_page_config(
    page_title="CHAPTER 48",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
.main, .block-container,
iframe, [data-testid="stIFrame"] {
    background-color: #FDFBF7 !important;
    color-scheme: light !important;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  AUDIO
# ─────────────────────────────────────────────
AUDIO_PATH = "assets/brahms_op118_no2.mp3"

audio_tag = ""
if os.path.exists(AUDIO_PATH):
    with open(AUDIO_PATH, "rb") as f:
        audio_b64 = base64.b64encode(f.read()).decode()
    audio_tag = f'<audio controls preload="metadata" style="display:block;width:100%;max-width:380px;margin:0 auto;accent-color:#9B8B75;opacity:0.85;"><source src="data:audio/mpeg;base64,{audio_b64}" type="audio/mpeg"></audio>'

# ─────────────────────────────────────────────
#  FULL PAGE via components.html
#  This bypasses Streamlit's iframe sandbox entirely,
#  giving us full CSS control including fixed positioning.
# ─────────────────────────────────────────────
import streamlit.components.v1 as components

components.html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap" rel="stylesheet">
<style>

  * {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }}

  html, body {{
    width: 100%;
    height: 100%;
    background-color: #FDFBF7;
    font-family: 'Playfair Display', Georgia, 'Times New Roman', serif;
    color: #4A4A4A;
    -webkit-font-smoothing: antialiased;
  }}

  /* ── FADE-IN KEYFRAMES ── */
  @keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(7px); }}
    to   {{ opacity: 1; transform: translateY(0);   }}
  }}

  /* ── MAIN CONTENT BLOCK ── */
  .page {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 22vh 2rem 6rem 2rem;
    max-width: 560px;
    margin: 0 auto;
  }}

  /* ── TITLE ── */
  .title {{
    font-size: 50px;
    font-weight: 500;
    letter-spacing: 0.05em;
    color: #2E2E2E;
    line-height: 1.1;
    margin-bottom: 1rem;
    animation: fadeUp 1.6s ease-out 0.5s both;
  }}

  /* ── SUBTITLE ── */
  .subtitle {{
    font-size: 15.6px;
    font-style: italic;
    font-weight: 400;
    color: #6A6A6A;
    letter-spacing: 0.02em;
    line-height: 1.6;
    margin-bottom: 3rem;
    animation: fadeUp 1.6s ease-out 1.0s both;
  }}

  /* ── PLAYER BLOCK (track info + audio) ── */
  .player-block {{
    width: 100%;
    animation: fadeUp 1.4s ease-out 1.5s both;
  }}

  /* ── DIVIDER ── */
  .divider {{
    width: 36px;
    height: 1px;
    background-color: #C8BFB0;
    margin: 0 auto 2rem auto;
  }}

  /* ── TRACK INFO ── */
  .track {{
    font-size: 12px;
    color: #9B9083;
    letter-spacing: 0.08em;
    margin-bottom: 0.8rem;
    line-height: 1.6;
  }}

  /* ── AUDIO ELEMENT ── */
  audio {{
    display: block;
    width: 100%;
    max-width: 380px;
    margin: 0 auto;
    accent-color: #9B8B75;
    opacity: 0.85;
  }}

  /* ── FOOTNOTE — fixed to bottom ── */
  .footnote {{
    position: fixed;
    bottom: 1.6rem;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 9px;
    color: #C0B8B0;
    letter-spacing: 1.6em;
    text-transform: uppercase;
    animation: fadeUp 1.2s ease-out 2.0s both;
  }}

</style>
</head>
<body>

  <div class="page">

    <p class="title">Chapter 48</p>

    <p class="subtitle">An intermezzo before the pages ahead</p>

    <div class="player-block">
      <div class="divider"></div>
      <p class="track">Brahms: Intermezzo Op. 118, No. 2 (1893)</p>
      {audio_tag}
    </div>

  </div>

  <p class="footnote">Douglas</p>

</body>
</html>
""", height=800, scrolling=False)
