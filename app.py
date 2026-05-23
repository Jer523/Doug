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
    from {{ opacity:0; transform:translateY(14px); }}
    to   {{ opacity:1; transform:translateY(0); }}
  }}

  .page {{
    display:flex;
    flex-direction:column;
    align-items:center;
    text-align:center;
    padding:26vh 2rem 0 2rem;
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
    margin-bottom:1.2rem;
    line-height:1.6;
  }}

  /* ── Visualizer ── */
  .viz-wrap {{
    width:100%;
    max-width:270px;
    /* align with the progress bar: skip the button width + gap */
    padding-left: calc(10px + 36px + 24px); /* player padding-left + btn width + gap */
    margin:0 auto 10px auto;
    box-sizing:border-box;
  }}
  #viz-canvas {{
    display:block;
    width:100%;
    height:32px;
  }}

  /* ── Player row ── */
  .player-wrap {{
    width:100%;
    max-width:270px;
    margin:0 auto;
    display:flex;
    align-items:center;
    gap:24px;          /* ← increased from 14px */
    padding-left:10px; /* ← shift button right */
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
    padding:0;
    -webkit-tap-highlight-color:transparent;
  }}
  #play-btn svg {{ width:13px; height:13px; fill:#7A6E65; }}

  .progress-wrap {{
    flex:1;
    position:relative;
    height:44px;
    display:flex;
    align-items:center;
    cursor:pointer;
    touch-action:none;
  }}

  .progress-track {{
    width:100%;
    height:1px;
    background:#DDD6CE;
    position:relative;
    border-radius:1px;
    pointer-events:none;
  }}

  #progress-fill {{
    height:100%;
    width:0%;
    background:#9B8B75;
    border-radius:1px;
  }}

  #scrubber {{
    position:absolute;
    top:50%; left:0%;
    transform:translate(-50%,-50%);
    width:9px; height:9px;
    border-radius:50%;
    background:#9B8B75;
  }}

  #time-tooltip {{
    position:absolute;
    top:2px;
    left:0%;
    transform:translateX(-50%);
    font-size:9px;
    color:#9B9083;
    white-space:nowrap;
    opacity:0;
    transition:opacity 0.2s;
    pointer-events:none;
  }}

  .vol-wrap {{
    display:none; /* keep vol hidden as before */
  }}

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

    <!-- Visualizer sits above the player row, aligned with the progress bar -->
    <div class="viz-wrap">
      <canvas id="viz-canvas"></canvas>
    </div>

    <div class="player-wrap">
      <button id="play-btn">
        <svg id="icon-play" viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        <svg id="icon-pause" viewBox="0 0 24 24" style="display:none">
          <rect x="5" y="3" width="4" height="18"/>
          <rect x="15" y="3" width="4" height="18"/>
        </svg>
      </button>

      <div class="progress-wrap" id="progress-wrap">
        <div id="time-tooltip"></div>
        <div class="progress-track">
          <div id="progress-fill"></div>
          <div id="scrubber"></div>
        </div>
      </div>
    </div>
  </div>
</div>

<p class="footnote">Douglas</p>

<script>
  const audio        = document.getElementById('audio-el');
  const iconPlay     = document.getElementById('icon-play');
  const iconPause    = document.getElementById('icon-pause');
  const fill         = document.getElementById('progress-fill');
  const scrubber     = document.getElementById('scrubber');
  const progressWrap = document.getElementById('progress-wrap');
  const tooltip      = document.getElementById('time-tooltip');

  let tooltipTimer     = null;
  let draggingProgress = false;

  // ── helpers ──
  function fmt(s) {{
    if (!isFinite(s) || isNaN(s) || s < 0) return '';
    return Math.floor(s/60) + ':' + String(Math.floor(s%60)).padStart(2,'0');
  }}
  function showTooltip(pct, t) {{
    const label = fmt(t);
    if (!label) return;
    tooltip.textContent = label;
    tooltip.style.left = Math.max(5, Math.min(95, pct*100)) + '%';
    tooltip.style.opacity = '1';
    clearTimeout(tooltipTimer);
    tooltipTimer = setTimeout(() => tooltip.style.opacity='0', 1
