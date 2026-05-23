import streamlit as st

st.set_page_config(
    page_title="CHAPTER 48",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  AUDIO
# ─────────────────────────────────────────────
audio_url = "https://raw.githubusercontent.com/Jer523/Douglas/main/assets/brahms_op118_no2.mp3.mp3"
audio_tag = f'<audio controls preload="none" style="display:block;width:100%;max-width:380px;margin:0 auto;accent-color:#9B8B75;opacity:0.85;"><source src="{audio_url}" type="audio/mpeg"></audio>'

# ─────────────────────────────────────────────
st.markdown(f"""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap');

  /* ── KILL DEFAULT STREAMLIT BACKGROUND & PADDING ── */
  html, body,
  [data-testid="stAppViewContainer"],
  [data-testid="stAppViewBlockContainer"],
  .main, .block-container {{
    background: #FDFBF7 !important;
    color-scheme: light !important;
    padding: 0 !important;
    margin: 0 !important;
    overflow: hidden !important;
  }}

  /* ── FULL-SCREEN OVERLAY: this IS the page ── */
  #chapter-page {{
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: #FDFBF7;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding-top: 26vh;
    padding-left: 2rem;
    padding-right: 2rem;
    font-family: 'Playfair Display', Georgia, serif;
    color: #4A4A4A;
    -webkit-font-smoothing: antialiased;
    z-index: 99999;
    text-align: center;
    overflow: hidden;
  }}

  /* ── FADE-IN KEYFRAMES ── */
  @keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(14px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
  }}

  /* ── TITLE ── */
  #chapter-page .title {{
    font-size: 50px;
    font-weight: 500;
    letter-spacing: 0.05em;
    color: #2E2E2E;
    line-height: 1.1;
    margin-bottom: 1rem;
    animation: fadeUp 1.6s ease-out 0.5s both;
  }}

  /* ── SUBTITLE ── */
  #chapter-page .subtitle {{
    font-size: 15.6px;
    font-style: italic;
    font-weight: 400;
    color: #6A6A6A;
    letter-spacing: 0.02em;
    line-height: 1.6;
    margin-bottom: 3rem;
    animation: fadeUp 1.6s ease-out 1.5s both;
  }}

  /* ── PLAYER BLOCK ── */
  #chapter-page .player-block {{
    width: 100%;
    max-width: 420px;
    animation: fadeUp 1.4s ease-out 2.5s both;
  }}

  /* ── DIVIDER ── */
  #chapter-page .divider {{
    width: 280px;
    height: 1px;
    background-color: #C8BFB0;
    margin: 0 auto 2rem auto;
  }}

  /* ── TRACK INFO ── */
  #chapter-page .track {{
    font-size: 12.3px;
    color: #9B9083;
    letter-spacing: 0.08em;
    margin-bottom: 0.8rem;
    line-height: 1.6;
    font-family: 'Playfair Display', Georgia, serif;
  }}

  /* ── AUDIO ── */
  #chapter-page audio {{
    display: block;
    width: 100%;
    max-width: 380px;
    margin: 0 auto;
    accent-color: #9B8B75;
    opacity: 0.85;
  }}

  /* ── FOOTNOTE — truly fixed to bottom of screen ── */
  #chapter-footnote {{
    position: fixed;
    bottom: 1.6rem;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 9px;
    font-family: 'Playfair Display', Georgia, serif;
    color: #C0B8B0;
    letter-spacing: 2em;
    text-transform: uppercase;
    z-index: 99999;
    animation: fadeUp 1.2s ease-out 3.5s both;
  }}
</style>

<!-- MAIN PAGE DIV — covers entire screen -->
<div id="chapter-page">
  <p class="title">Chapter 48</p>
  <p class="subtitle">An intermezzo before the pages ahead</p>
  <div class="player-block">
    <div class="divider"></div>
    <p class="track">Brahms: Intermezzo Op. 118, No. 2 (1893)</p>
    {audio_tag}
  </div>
</div>

<!-- FOOTNOTE — separate fixed element -->
<p id="chapter-footnote">Douglas</p>
""", unsafe_allow_html=True)
