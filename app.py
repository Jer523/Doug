import streamlit as st

st.set_page_config(
    page_title="CHAPTER 48",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

audio_url = "https://raw.githubusercontent.com/Jer523/Douglas/main/assets/brahms_op118_no2.mp3"

st.markdown(f"""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap');

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

  @keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(14px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
  }}

  #chapter-page .title {{
    font-size: 50px;
    font-weight: 500;
    letter-spacing: 0.05em;
    color: #2E2E2E;
    line-height: 1.1;
    margin-bottom: 1rem;
    animation: fadeUp 1.6s ease-out 0.5s both;
  }}

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

  #chapter-page .player-block {{
    width: 100%;
    max-width: 420px;
    animation: fadeUp 1.4s ease-out 2.5s both;
  }}

  /* ── DIVIDER ── 改 width 调长度 */
  #chapter-page .divider {{
    width: 80px;
    height: 1px;
    background-color: #C8BFB0;
    margin: 0 auto 2rem auto;
  }}

  /* ── TRACK INFO ── 改 font-size 调字号 */
  #chapter-page .track {{
    font-size: 11px;
    color: #9B9083;
    letter-spacing: 0.08em;
    margin-bottom: 1.4rem;
    line-height: 1.6;
    font-family: 'Playfair Display', Georgia, serif;
  }}

  /* ── CUSTOM AUDIO PLAYER ── */
  .player-wrap {{
    width: 100%;
    max-width: 380px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    gap: 14px;
  }}

  /* Play/pause button */
  #play-btn {{
    flex-shrink: 0;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    border: 1px solid #C8BFB0;
    background: transparent;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: border-color 0.3s, opacity 0.3s;
    padding: 0;
  }}
  #play-btn:hover {{ border-color: #9B8B75; opacity: 0.8; }}
  #play-btn svg {{ width: 14px; height: 14px; fill: #7A6E65; }}

  /* Progress bar track */
  .progress-track {{
    flex: 1;
    height: 1px;
    background: #DDD6CE;
    position: relative;
    cursor: pointer;
    border-radius: 1px;
  }}

  /* Progress bar fill */
  #progress-fill {{
    height: 100%;
    width: 0%;
    background: #9B8B75;
    border-radius: 1px;
    transition: width 0.1s linear;
    pointer-events: none;
  }}

  /* Scrubber dot */
  #scrubber {{
    position: absolute;
    top: 50%;
    left: 0%;
    transform: translate(-50%, -50%);
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #9B8B75;
    pointer-events: none;
    transition: left 0.1s linear;
  }}

  /* Time display */
  #time-display {{
    flex-shrink: 0;
    font-size: 9px;
    font-family: 'Playfair Display', Georgia, serif;
    color: #B8B0A5;
    letter-spacing: 0.05em;
    min-width: 70px;
    text-align: right;
  }}

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

<div id="chapter-page">
  <p class="title">Chapter 48</p>
  <p class="subtitle">An intermezzo before the pages ahead</p>
  <div class="player-block">
    <div class="divider"></div>
    <p class="track">Brahms: Intermezzo Op. 118, No. 2 (1893)</p>

    <!-- Hidden native audio element -->
    <audio id="audio-el" preload="none">
      <source src="{audio_url}" type="audio/mpeg">
    </audio>

    <!-- Custom player UI -->
    <div class="player-wrap">

      <!-- Play / Pause button -->
      <button id="play-btn" onclick="togglePlay()">
        <svg id="icon-play" viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>
        <svg id="icon-pause" viewBox="0 0 24 24" style="display:none">
          <rect x="5" y="3" width="4" height="18"/>
          <rect x="15" y="3" width="4" height="18"/>
        </svg>
      </button>

      <!-- Progress track -->
      <div class="progress-track" id="progress-track" onclick="seek(event)">
        <div id="progress-fill"></div>
        <div id="scrubber"></div>
      </div>

      <!-- Time -->
      <span id="time-display">0:00 / —:——</span>

    </div>
  </div>
</div>

<p id="chapter-footnote">Douglas</p>

<script>
  const audio = document.getElementById('audio-el');
  const playBtn = document.getElementById('play-btn');
  const iconPlay = document.getElementById('icon-play');
  const iconPause = document.getElementById('icon-pause');
  const fill = document.getElementById('progress-fill');
  const scrubber = document.getElementById('scrubber');
  const timeDisplay = document.getElementById('time-display');

  function fmt(s) {{
    if (isNaN(s)) return '—:——';
    const m = Math.floor(s / 60);
    const sec = Math.floor(s % 60).toString().padStart(2, '0');
    return m + ':' + sec;
  }}

  function togglePlay() {{
    if (audio.paused) {{
      audio.play();
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
    const track = document.getElementById('progress-track');
    const rect = track.getBoundingClientRect();
    const pct = (e.clientX - rect.left) / rect.width;
    audio.currentTime = pct * audio.duration;
  }}
</script>
""", unsafe_allow_html=True)
