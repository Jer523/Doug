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

AUDIO_URL = "https://raw.githubusercontent.com/Jer523/Douglas/main/assets/brahms_op118_no2.mp3"

components.html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}

  html, body {{
    width:100%; height:100%;
    background:#FDFBF7;
    font-family:'Playfair Display', Georgia, serif;
    color:#4A4A4A;
    -webkit-font-smoothing:antialiased;
    overflow:hidden;
  }}

  @keyframes fadeUp {{
    from {{ opacity:0; transform:translateY(14px); }}
    to   {{ opacity:1; transform:translateY(0); }}
  }}

  .page {{
    display:flex;
    flex-direction:column;
    align-items:center;
    text-align:center;
    padding: 26vh 2rem 0 2rem;
    max-width:560px;
    margin:0 auto;
  }}

  .title {{
    font-size:50px;
    font-weight:500;
    letter-spacing:0.05em;
    color:#2E2E2E;
    line-height:1.1;
    margin-bottom:1rem;
    animation:fadeUp 1.6s ease-out 0.5s both;
  }}

  .subtitle {{
    font-size:15.6px;
    font-style:italic;
    color:#6A6A6A;
    letter-spacing:0.02em;
    line-height:1.6;
    margin-bottom:3rem;
    animation:fadeUp 1.6s ease-out 1.5s both;
  }}

  .player-block {{
    width:100%;
    max-width:420px;
    animation:fadeUp 1.4s ease-out 2.5s both;
  }}

  .divider {{
    width:260px;
    height:1px;
    background:#C8BFB0;
    margin:0 auto 2rem auto;
  }}

  .track {{
    font-size:12px;
    color:#9B9083;
    letter-spacing:0.08em;
    margin-bottom:1.4rem;
    line-height:1.6;
  }}

  /* ── 原生 audio 样式 ── */
  audio {{
    display:block;
    width:100%;
    max-width:340px;
    margin:0 auto;
    /* 用 accent-color 给进度条和控件上暖色调 */
    accent-color: #9B8B75;
    opacity:0.9;
    /* 让背景透明，融入页面 */
    background: transparent;
    border-radius: 8px;
  }}

  /* footnote */
  .footnote {{
    position:fixed;
    bottom:1.6rem;
    left:0; right:0;
    text-align:center;
    font-size:9px;
    color:#C0B8B0;
    letter-spacing:2em;
    text-transform:uppercase;
    animation:fadeUp 1.2s ease-out 3.5s both;
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
    <audio controls preload="none">
      <source src="{AUDIO_URL}" type="audio/mpeg">
    </audio>
  </div>
</div>

<p class="footnote">Douglas</p>

<script>
  // iframe 撑满屏幕
  try {{
    window.parent.document.querySelectorAll('iframe').forEach(f => {{
      f.style.height = window.screen.height + 'px';
      f.style.position = 'fixed';
      f.style.top = '0';
      f.style.left = '0';
      f.style.width = '100%';
      f.style.border = 'none';
      f.style.zIndex = '99999';
    }});
  }} catch(e) {{}}
</script>

</body>
</html>
""", height=900, scrolling=False)
