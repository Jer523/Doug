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
    margin-bottom:1.4rem;
    line-height:1.6;
  }}

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
    padding:0;
    -webkit-tap-highlight-color:transparent;
  }}
  #play-btn svg {{ width:13px; height:13px; fill:#7A6E65; }}

  .progress-wrap {{
    flex:1;
    position:relative;
    height:20px;
    display:flex;
    align-items:center;
  }}

  .progress-track {{
    width:100%;
    height:1px;
    background:#DDD6CE;
    position:relative;
    border-radius:1px;
    touch-action:none;
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
    width:9px; height:9px;
    border-radius:50%;
    background:#9B8B75;
    pointer-events:none;
  }}

  #time-tooltip {{
    position:absolute;
    top:-20px;
    left:0%;
    transform:translateX(-50%);
    font-size:9px;
    color:#9B9083;
    white-space:nowrap;
    opacity:0;
    transition:opacity 0.2s;
    pointer-events:none;
  }}

  /* ── 音量：用原生 range 横条，套在右侧小区域 ── */
  .vol-wrap {{
    flex-shrink:0;
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:5px;
    width:18px;
  }}

  .vol-icon svg {{
    width:11px; height:11px;
    fill:#B8B0A5;
    display:block;
  }}

  /* 用 rotate 把横条变成竖条，兼容所有手机浏览器 */
  .vol-rotate-wrap {{
    width:18px;
    height:52px;
    display:flex;
    align-items:center;
    justify-content:center;
    overflow:visible;
  }}

  #vol-slider {{
    -webkit-appearance:none;
    appearance:none;
    width:52px;
    height:2px;
    background:#DDD6CE;
    outline:none;
    border:none;
    cursor:pointer;
    transform:rotate(-90deg);
    transform-origin:center center;
    accent-color:#9B8B75;
    touch-action:none;
  }}
  #vol-slider::-webkit-slider-thumb {{
    -webkit-appearance:none;
    width:9px; height:9px;
    border-radius:50%;
    background:#9B8B75;
    cursor:pointer;
  }}
  #vol-slider::-moz-range-thumb {{
    width:9px; height:9px;
    border-radius:50%;
    background:#9B8B75;
    border:none;
    cursor:pointer;
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

    <div class="player-wrap">

      <button id="play-btn">
        <svg id="icon-play" viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        <svg id="icon-pause" viewBox="0 0 24 24" style="display:none">
          <rect x="5" y="3" width="4" height="18"/>
          <rect x="15" y="3" width="4" height="18"/>
        </svg>
      </button>

      <div class="progress-wrap">
        <div id="time-tooltip"></div>
        <div class="progress-track" id="progress-track">
          <div id="progress-fill"></div>
          <div id="scrubber"></div>
        </div>
      </div>

      <div class="vol-wrap">
        <span class="vol-icon">
          <svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02z"/></svg>
        </span>
        <div class="vol-rotate-wrap">
          <input type="range" id="vol-slider" min="0" max="1" step="0.01" value="0.8">
        </div>
      </div>

    </div>
  </div>
</div>

<p class="footnote">Douglas</p>

<script>
  const audio     = document.getElementById('audio-el');
  const iconPlay  = document.getElementById('icon-play');
  const iconPause = document.getElementById('icon-pause');
  const fill      = document.getElementById('progress-fill');
  const scrubber  = document.getElementById('scrubber');
  const trackEl   = document.getElementById('progress-track');
  const tooltip   = document.getElementById('time-tooltip');
  const volSlider = document.getElementById('vol-slider');
  const playBtn   = document.getElementById('play-btn');

  audio.volume = 0.8;
  let tooltipTimer = null;
  let dragging = false;

  function fmt(s) {{
    if (!isFinite(s) || isNaN(s) || s < 0) return '';
    const m = Math.floor(s / 60);
    const sec = String(Math.floor(s % 60)).padStart(2, '0');
    return m + ':' + sec;
  }}

  function showTooltip(pct, t) {{
    const label = fmt(t);
    if (!label) return;
    tooltip.textContent = label;
    const clamped = Math.max(5, Math.min(95, pct * 100));
    tooltip.style.left = clamped + '%';
    tooltip.style.opacity = '1';
    clearTimeout(tooltipTimer);
    tooltipTimer = setTimeout(() => tooltip.style.opacity = '0', 1500);
  }}

  function updateBar(pct) {{
    fill.style.width    = (pct * 100) + '%';
    scrubber.style.left = (pct * 100) + '%';
  }}

  // Play / pause
  playBtn.addEventListener('click', () => {{
    if (audio.paused) audio.play().catch(() => {{}});
    else audio.pause();
  }});

  audio.addEventListener('play',  () => {{ iconPlay.style.display='none';  iconPause.style.display='block'; }});
  audio.addEventListener('pause', () => {{ iconPlay.style.display='block'; iconPause.style.display='none';  }});
  audio.addEventListener('ended', () => {{
    iconPlay.style.display='block'; iconPause.style.display='none';
    updateBar(0);
  }});
  audio.addEventListener('timeupdate', () => {{
    if (audio.duration) updateBar(audio.currentTime / audio.duration);
  }});

  // Progress bar — touch-action:none on the element lets us capture smoothly
  function pctFromEvent(e) {{
    const rect = trackEl.getBoundingClientRect();
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    return Math.max(0, Math.min(1, (clientX - rect.left) / rect.width));
  }}

  function doSeek(e) {{
    const pct = pctFromEvent(e);
    updateBar(pct);
    if (audio.duration) {{
      audio.currentTime = pct * audio.duration;
      showTooltip(pct, audio.currentTime);
    }}
  }}

  trackEl.addEventListener('mousedown',  e => {{ dragging = true; doSeek(e); e.preventDefault(); }});
  trackEl.addEventListener('touchstart', e => {{ dragging = true; doSeek(e); }}, {{passive:true}});
  window.addEventListener('mousemove',   e => {{ if (dragging) doSeek(e); }});
  window.addEventListener('touchmove',   e => {{ if (dragging) doSeek(e); }}, {{passive:true}});
  window.addEventListener('mouseup',     () => dragging = false);
  window.addEventListener('touchend',    () => dragging = false);

  // Volume — native range handles touch natively, just read value
  volSlider.addEventListener('input', () => {{
    audio.volume = parseFloat(volSlider.value);
  }});

  // Stretch iframe
  try {{
    window.parent.document.querySelectorAll('iframe').forEach(f => {{
      f.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:' + window.screen.height + 'px;border:none;z-index:99999;';
    }});
  }} catch(e) {{}}
</script>
</body>
</html>
""", height=900, scrolling=False)
