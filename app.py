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

  /* ── 播放器整体 ── */
  .player-wrap {{
    width:100%;
    max-width:380px;
    margin:0 auto;
    display:flex;
    align-items:center;
    gap:14px;
  }}

  /* ── 播放/暂停按钮 ── */
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
    transition:border-color 0.3s;
    padding:0;
  }}
  #play-btn:active {{ opacity:0.6; }}
  #play-btn svg {{ width:13px; height:13px; fill:#7A6E65; }}

  /* ── 进度条区域（包含tooltip） ── */
  .progress-wrap {{
    flex:1;
    position:relative;
    padding-top:18px; /* 为tooltip留空间 */
  }}

  .progress-track {{
    width:100%;
    height:1px;
    background:#DDD6CE;
    position:relative;
    cursor:pointer;
    border-radius:1px;
  }}

  /* 扩大点击热区 */
  .progress-track::before {{
    content:'';
    position:absolute;
    top:-10px; bottom:-10px;
    left:0; right:0;
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
    transition:left 0.05s linear;
  }}

  /* ── 悬浮时间提示 ── */
  #time-tooltip {{
    position:absolute;
    top:0;
    left:0%;
    transform:translateX(-50%);
    font-size:9px;
    color:#9B9083;
    letter-spacing:0.05em;
    white-space:nowrap;
    opacity:0;
    transition:opacity 0.2s;
    pointer-events:none;
  }}

  /* ── 音量控制区域 ── */
  .vol-wrap {{
    flex-shrink:0;
    display:flex;
    align-items:center;
    gap:6px;
    width:72px;
  }}

  /* 音量小图标 */
  .vol-icon svg {{
    width:11px; height:11px;
    fill:#B8B0A5;
    display:block;
  }}

  /* 音量滑块 */
  #vol-slider {{
    -webkit-appearance:none;
    appearance:none;
    width:100%;
    height:1px;
    background:#DDD6CE;
    outline:none;
    border:none;
    cursor:pointer;
  }}
  #vol-slider::-webkit-slider-thumb {{
    -webkit-appearance:none;
    width:7px; height:7px;
    border-radius:50%;
    background:#9B8B75;
    cursor:pointer;
  }}
  #vol-slider::-moz-range-thumb {{
    width:7px; height:7px;
    border-radius:50%;
    background:#9B8B75;
    border:none;
    cursor:pointer;
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

    <audio id="audio-el" preload="none" crossorigin="anonymous">
      <source src="{AUDIO_URL}" type="audio/mpeg">
    </audio>

    <div class="player-wrap">

      <!-- 播放/暂停 -->
      <button id="play-btn" onclick="togglePlay()">
        <svg id="icon-play" viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        <svg id="icon-pause" viewBox="0 0 24 24" style="display:none">
          <rect x="5" y="3" width="4" height="18"/>
          <rect x="15" y="3" width="4" height="18"/>
        </svg>
      </button>

      <!-- 进度条 + tooltip -->
      <div class="progress-wrap">
        <div id="time-tooltip">0:00</div>
        <div class="progress-track" id="progress-track">
          <div id="progress-fill"></div>
          <div id="scrubber"></div>
        </div>
      </div>

      <!-- 音量 -->
      <div class="vol-wrap">
        <span class="vol-icon">
          <svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02z"/></svg>
        </span>
        <input type="range" id="vol-slider" min="0" max="1" step="0.05" value="0.8">
      </div>

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
  const track = document.getElementById('progress-track');
  const tooltip = document.getElementById('time-tooltip');
  const volSlider = document.getElementById('vol-slider');

  // 默认音量
  audio.volume = 0.8;

  let tooltipTimer = null;

  function fmt(s) {{
    if (isNaN(s) || s === Infinity) return '—:——';
    const m = Math.floor(s / 60);
    const sec = String(Math.floor(s % 60)).padStart(2, '0');
    return m + ':' + sec;
  }}

  function showTooltip(pct, time) {{
    tooltip.textContent = fmt(time);
    tooltip.style.left = (pct * 100) + '%';
    tooltip.style.opacity = '1';
    clearTimeout(tooltipTimer);
    tooltipTimer = setTimeout(() => {{ tooltip.style.opacity = '0'; }}, 1200);
  }}

  function togglePlay() {{
    if (audio.paused) {{
      audio.play().catch(() => {{}});
    }} else {{
      audio.pause();
    }}
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
    const pct = audio.currentTime / audio.duration;
    fill.style.width = (pct * 100) + '%';
    scrubber.style.left = (pct * 100) + '%';
  }});

  audio.addEventListener('ended', () => {{
    iconPlay.style.display = 'block';
    iconPause.style.display = 'none';
    fill.style.width = '0%';
    scrubber.style.left = '0%';
  }});

  // 进度条点击 + 拖动
  let dragging = false;

  function getPct(e) {{
    const rect = track.getBoundingClientRect();
    const x = (e.touches ? e.touches[0].clientX : e.clientX);
    return Math.max(0, Math.min(1, (x - rect.left) / rect.width));
  }}

  function applySeek(pct) {{
    if (!audio.duration) return;
    audio.currentTime = pct * audio.duration;
    showTooltip(pct, audio.currentTime);
  }}

  track.addEventListener('mousedown', (e) => {{ dragging = true; applySeek(getPct(e)); }});
  track.addEventListener('touchstart', (e) => {{ dragging = true; applySeek(getPct(e)); }}, {{passive:true}});
  document.addEventListener('mousemove', (e) => {{ if (dragging) applySeek(getPct(e)); }});
  document.addEventListener('touchmove', (e) => {{ if (dragging) applySeek(getPct(e)); }}, {{passive:true}});
  document.addEventListener('mouseup', () => {{ dragging = false; }});
  document.addEventListener('touchend', () => {{ dragging = false; }});

  // 音量滑块
  volSlider.addEventListener('input', () => {{
    audio.volume = parseFloat(volSlider.value);
  }});

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
