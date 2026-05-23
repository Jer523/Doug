import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CHAPTER 48",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome, set background
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

  /* 分割线 — 改 width 调长度 */
  .divider {{
    width:260px;
    height:1px;
    background:#C8BFB0;
    margin:0 auto 2rem auto;
  }}

  /* 曲名 */
  .track {{
    font-size:12px;
    color:#9B9083;
    letter-spacing:0.08em;
    margin-bottom:1.4rem;
    line-height:1.6;
  }}

  /* ── 自定义播放器 ── */
  .player-wrap {{
    width:100%;
    max-width:380px;
    margin:0 auto;
    display:flex;
    align-items:center;
    gap:14px;
  }}

  #play-btn {{
    flex-shrink:0;
    width:36px; height:36px;
    border-radius:50%;
    border:1px solid #C8BFB0;
    background:transparent;
    cursor:pointer;
    display:flex;
    align-items:center;
    justify-content:center;
    transition:border-color 0.3s, opacity 0.3s;
    padding:0;
  }}
  #play-btn:hover {{ border-color:#9B8B75; opacity:0.8; }}
  #play-btn svg {{ width:13px; height:13px; fill:#7A6E65; }}

  .progress-track {{
    flex:1;
    height:1px;
    background:#DDD6CE;
    position:relative;
    cursor:pointer;
    border-radius:1px;
  }}

  #progress-fill {{
    height:100%;
    width:0%;
    background:#9B8B75;
    border-radius:1px;
    pointer-events:none;
  }}

  #scrubber {{
    position:absolute;
    top:50%; left:0%;
    transform:translate(-50%,-50%);
    width:7px; height:7px;
    border-radius:50%;
    background:#9B8B75;
    pointer-events:none;
  }}

  #time-display {{
    flex-shrink:0;
    font-size:9px;
    color:#B8B0A5;
    letter-spacing:0.05em;
    min-width:72px;
    text-align:right;
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

    <audio id="audio-el" preload="none">
      <source src="{AUDIO_URL}" type="audio/mpeg">
    </audio>

    <div class="player-wrap">
      <button id="play-btn" onclick="togglePlay()">
        <svg id="icon-play" viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        <svg id="icon-pause" viewBox="0 0 24 24" style="display:none">
          <rect x="5" y="3" width="4" height="18"/>
          <rect x="15" y="3" width="4" height="18"/>
        </svg>
      </button>
      <div class="progress-track" id="progress-track" onclick="seek(event)">
        <div id="progress-fill"></div>
        <div id="scrubber"></div>
      </div>
      <span id="time-display">0:00 / —:——</span>
    </div>

  </div>
</div>

<p class="footnote">Douglas</p>

<script>
  const audio = document.getElementById('audio-el');
  const iconPlay = document.getElementById('icon-play');
  const iconPause = document.getElementById('icon-pause');
  const fill = document.getElementById('progress-fill');
  const scrubber = document.getElementById('scrubber');
  const timeDisplay = document.getElementById('time-display');

  function fmt(s) {{
    if (isNaN(s) || s === Infinity) return '—:——';
    const m = Math.floor(s / 60);
    const sec = String(Math.floor(s % 60)).padStart(2, '0');
    return m + ':' + sec;
  }}

  function togglePlay() {{
    audio.paused ? audio.play() : audio.pause();
  }}

  audio.addEventListener('play', () => {{
    iconPlay.style.display = 'none';
    iconPause.style.display = 'block';
  }});

  audio.addEventListener('pause', () => {{
    iconPlay.style.display = 'block';
    iconPause.style.display = 'none';
  }});

  audio.addEventListener('timeupdate', () => {{
    if (!audio.duration) return;
    const pct = (audio.currentTime / audio.duration) * 100;
    fill.style.width = pct + '%';
    scrubber.style.left = pct + '%';
    timeDisplay.textContent = fmt(audio.currentTime) + ' / ' + fmt(audio.duration);
  }});

  audio.addEventListener('ended', () => {{
    iconPlay.style.display = 'block';
    iconPause.style.display = 'none';
    fill.style.width = '0%';
    scrubber.style.left = '0%';
  }});

  function seek(e) {{
    if (!audio.duration) return;
    const rect = document.getElementById('progress-track').getBoundingClientRect();
    const pct = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
    audio.currentTime = pct * audio.duration;
  }}

  // Resize iframe to fill screen
  window.parent.document.querySelectorAll('iframe').forEach(f => {{
    f.style.height = window.screen.height + 'px';
    f.style.position = 'fixed';
    f.style.top = '0';
    f.style.left = '0';
    f.style.width = '100%';
    f.style.border = 'none';
    f.style.zIndex = '99999';
  }});
</script>

</body>
</html>
""", height=900, scrolling=False)
