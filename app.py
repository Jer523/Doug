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

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap" rel="stylesheet">
<style>
  * {
    margin:0; padding:0; box-sizing:border-box;
    -webkit-user-select:none;
    user-select:none;
  }
  html, body {
    width:100%; height:100%;
    background:#FDFBF7;
    font-family:'Playfair Display', Georgia, serif;
    color:#4A4A4A;
    -webkit-font-smoothing:antialiased;
    overflow:hidden;
  }
  @keyframes fadeUp {
    from { opacity:0; transform:translateY(14px); }
    to   { opacity:1; transform:translateY(0); }
  }
  .page {
    display:flex;
    flex-direction:column;
    align-items:center;
    text-align:center;
    padding:26vh 2rem 0 2rem;
    max-width:560px;
    margin:0 auto;
  }
  .title {
    font-size:50px;
    font-weight:500;
    letter-spacing:0.05em;
    color:#2E2E2E;
    line-height:1.1;
    margin-bottom:1rem;
    animation:fadeUp 1.6s ease-out 0.5s both;
  }
  .subtitle {
    font-size:15.6px;
    font-style:italic;
    color:#6A6A6A;
    letter-spacing:0.02em;
    line-height:1.6;
    margin-bottom:3rem;
    animation:fadeUp 1.6s ease-out 1.5s both;
  }
  .player-block {
    width:100%;
    max-width:420px;
    animation:fadeUp 1.4s ease-out 2.5s both;
  }
  .divider {
    width:257px;
    height:1px;
    background:#C8BFB0;
    margin:0 auto 2rem auto;
  }
  .track {
    font-size:12px;
    color:#9B9083;
    letter-spacing:0.08em;
    margin-bottom:1.2rem;
    line-height:1.6;
  }

  .viz-container {
    width:100%;
    max-width:250px;
    margin:0 auto 10px auto;
  }
  #viz-canvas {
    display:block;
    width:100%;
    height:28px;
  }

  .player-container {
    width:100%;
    max-width:270px;
    margin:0 auto;
    display:flex;
    align-items:center;
    gap:14px;
  }

  #play-btn {
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
  }
  #play-btn svg { width:13px; height:13px; fill:#7A6E65; }

  .progress-wrap {
    flex:1;
    position:relative;
    height:44px;
    display:flex;
    align-items:center;
    cursor:pointer;
    touch-action:none;
  }
  .progress-track {
    width:100%;
    height:1px;
    background:#DDD6CE;
    position:relative;
    border-radius:1px;
    pointer-events:none;
  }
  #progress-fill {
    height:100%;
    width:0%;
    background:#9B8B75;
    border-radius:1px;
  }
  #scrubber {
    position:absolute;
    top:50%; left:0%;
    transform:translate(-50%,-50%);
    width:9px; height:9px;
    border-radius:50%;
    background:#9B8B75;
  }
  #time-tooltip {
    position:absolute;
    top:2px; left:0%;
    transform:translateX(-50%);
    font-size:9px;
    color:#9B9083;
    white-space:nowrap;
    opacity:0;
    transition:opacity 0.2s;
    pointer-events:none;
  }
  .footnote {
    position:fixed;
    bottom:1.6rem;
    left:0; right:0;
    text-align:center;
    font-size:9px;
    color:#C0B8B0;
    letter-spacing:2em;
    text-transform:uppercase;
    animation:fadeUp 1.2s ease-out 3.5s both;
  }
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
      <source src="__AUDIO_URL__" type="audio/mpeg">
    </audio>

    <div class="viz-container">
      <canvas id="viz-canvas"></canvas>
    </div>

    <div class="player-container">
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
  let isSeeking        = false;

  let audioCtx  = null;
  let analyser  = null;
  let dataArray = null;

  function initWebAudio() {
    if (audioCtx) return;
    try {
      audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      analyser = audioCtx.createAnalyser();
      analyser.fftSize = 2048;
      analyser.smoothingTimeConstant = 0.75;
      const source = audioCtx.createMediaElementSource(audio);
      source.connect(analyser);
      analyser.connect(audioCtx.destination);
      dataArray = new Uint8Array(analyser.frequencyBinCount);
    } catch(e) {
      console.warn('Web Audio unavailable:', e);
    }
  }

  function fmt(s) {
    if (!isFinite(s) || isNaN(s) || s < 0) return '';
    return Math.floor(s/60) + ':' + String(Math.floor(s%60)).padStart(2,'0');
  }
  function showTooltip(pct, t) {
    const label = fmt(t);
    if (!label) return;
    tooltip.textContent = label;
    tooltip.style.left = Math.max(5, Math.min(95, pct*100)) + '%';
    tooltip.style.opacity = '1';
    clearTimeout(tooltipTimer);
    tooltipTimer = setTimeout(() => tooltip.style.opacity='0', 1500);
  }
  function updateProgress(pct) {
    fill.style.width    = (pct*100) + '%';
    scrubber.style.left = (pct*100) + '%';
  }

  document.getElementById('play-btn').addEventListener('click', () => {
    initWebAudio();
    if (audioCtx && audioCtx.state === 'suspended') audioCtx.resume();
    audio.paused ? audio.play().catch(()=>{}) : audio.pause();
  });
  audio.addEventListener('play',  () => { iconPlay.style.display='none';  iconPause.style.display='block'; });
  audio.addEventListener('pause', () => { iconPlay.style.display='block'; iconPause.style.display='none';  });
  audio.addEventListener('ended', () => { iconPlay.style.display='block'; iconPause.style.display='none'; updateProgress(0); });
  audio.addEventListener('timeupdate', () => {
    if (!draggingProgress && !isSeeking && audio.duration)
      updateProgress(audio.currentTime / audio.duration);
  });

  let pendingPct = null;

  function progressPct(e) {
    const rect = progressWrap.getBoundingClientRect();
    const x = e.touches ? e.touches[0].clientX : e.clientX;
    return Math.max(0, Math.min(1, (x - rect.left) / rect.width));
  }
  function dragMove(e) {
    if (!draggingProgress) return;
    pendingPct = progressPct(e);
    updateProgress(pendingPct);
    showTooltip(pendingPct, pendingPct * (audio.duration || 0));
  }
  function dragEnd() {
    if (!draggingProgress) return;
    draggingProgress = false;
    if (pendingPct !== null && audio.duration) {
      audio.currentTime = pendingPct * audio.duration;
      isSeeking = true;
      setTimeout(() => { isSeeking = false; }, 300);
      pendingPct = null;
    }
  }
  progressWrap.addEventListener('mousedown',  e => { draggingProgress=true; pendingPct=progressPct(e); updateProgress(pendingPct); e.preventDefault(); });
  progressWrap.addEventListener('touchstart', e => { draggingProgress=true; pendingPct=progressPct(e); updateProgress(pendingPct); }, {passive:true});
  window.addEventListener('mousemove',  dragMove);
  window.addEventListener('touchmove',  dragMove, {passive:true});
  window.addEventListener('mouseup',    dragEnd);
  window.addEventListener('touchend',   dragEnd);

  // ── Visualizer ──
  const canvas = document.getElementById('viz-canvas');
  const ctx    = canvas.getContext('2d');

  const BAR_COUNT = 44;
  const BAR_GAP   = 2;
  const MAX_H     = 24;
  const MIN_H     = 2;

  let barBins = null;

  // ── CHANGE 1 & 2: 单向左→右，log映射 60Hz~5000Hz 铺满全部44根柱子 ──
  function buildBarBins() {
    const sampleRate = audioCtx.sampleRate;
    const totalBins  = analyser.frequencyBinCount;
    const hzPerBin   = sampleRate / analyser.fftSize;

    const freqMin = 60;
    const freqMax = 3500;

    barBins = new Array(BAR_COUNT);
    for (let i = 0; i < BAR_COUNT; i++) {
      // i=0 → freqMin, i=BAR_COUNT-1 → freqMax, log scale
      const t    = i / (BAR_COUNT - 1);
      const freq = freqMin * Math.pow(freqMax / freqMin, t);
      barBins[i] = Math.min(Math.round(freq / hzPerBin), totalBins - 1);
    }
  }

  const bars = Array.from({length: BAR_COUNT}, () => ({
    h: MIN_H,
    target: MIN_H,
    speed: 0.18 + Math.random() * 0.08
  }));

  if (!CanvasRenderingContext2D.prototype.roundRect) {
    CanvasRenderingContext2D.prototype.roundRect = function(x,y,w,h,r) {
      this.rect(x,y,w,h);
    };
  }

  function resizeCanvas() {
    const dpr  = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width  = rect.width * dpr;
    canvas.height = 28         * dpr;
    ctx.scale(dpr, dpr);
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  let tickCount = 0;

  function drawViz() {
    const dpr = window.devicePixelRatio || 1;
    const W   = canvas.width  / dpr;
    const H   = canvas.height / dpr;
    ctx.clearRect(0, 0, W, H);

    const BAR_W   = (W - (BAR_COUNT - 1) * BAR_GAP) / BAR_COUNT;
    const playing = !audio.paused && !audio.ended;

    if (playing) {
      if (analyser && dataArray) {
        if (!barBins) buildBarBins();
        analyser.getByteFrequencyData(dataArray);

        for (let i = 0; i < BAR_COUNT; i++) {
          const raw = dataArray[barBins[i]] / 255;

          // ── CHANGE 3: 基于柱子位置的EQ动态权重 ──
          // t=0 → 最左低频, t=1 → 最右高频
          // 低频: 1.5, 中频: 1.0, 高频: 2.5+ (三段平滑插值)
          const t = i / (BAR_COUNT - 1);
          let eqGain;
          if (t < 0.07) {
                // 最左 ~3 格：极度压缩，raw=0.8 × 0.1 = 0.08 → 约8%
                eqGain = 0.1;
            } else if (t < 0.65) {
                // 低中频 → 中频：从 0.1 平滑爬升到 1.0，中间最高
                eqGain = 0.1 + Math.pow((t - 0.07) / 0.58, 0.8) * 1.4;
            } else {
                // 高频：大力拉升补偿弱信号，raw=0.03 × 6 = 0.18 → 约18%可见
                eqGain = 1.0 + Math.pow((t - 0.65) / 0.35, 1.0) * 5.0;
            }

          const boosted  = Math.min(1, raw * eqGain);
          bars[i].target = MIN_H + boosted * (MAX_H - MIN_H);
        }
      } else {
        tickCount++;
        if (tickCount >= 5) {
          tickCount = 0;
          for (let i = 0; i < BAR_COUNT; i++) {
            bars[i].target = MIN_H + Math.random() * (MAX_H - MIN_H);
          }
        }
      }
    } else {
      for (let i = 0; i < BAR_COUNT; i++) bars[i].target = MIN_H;
    }

    let x = 0;
    for (let i = 0; i < BAR_COUNT; i++) {
      bars[i].h += (bars[i].target - bars[i].h) * bars[i].speed;
      if (bars[i].h < MIN_H) bars[i].h = MIN_H;
      const barH = bars[i].h;
      const y    = (H - barH) / 2;
      ctx.fillStyle = '#B8A898';
      ctx.beginPath();
      ctx.roundRect(x, y, BAR_W, barH, 1);
      ctx.fill();
      x += BAR_W + BAR_GAP;
    }

    requestAnimationFrame(drawViz);
  }

  drawViz();

  try {
    window.parent.document.querySelectorAll('iframe').forEach(f => {
      f.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:'+window.screen.height+'px;border:none;z-index:99999;';
    });
  } catch(e) {}
</script>
</body>
</html>
"""

components.html(HTML.replace("__AUDIO_URL__", AUDIO_URL), height=900, scrolling=False)
