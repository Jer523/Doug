import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CHAPTER 48",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 全局背景样式
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
/* 脚注样式：延迟淡入、居中、可调大小字间距 */
.footnote-streamlit {
    position: fixed;
    bottom: 0rem;
    left: calc(50% + 8px);
    transform: translateX(-50%);
    font-size: 7.5px !important;
    color: #C0B8B0 !important;
    letter-spacing: 2.5em !important; /* 可自己调间距，同样加 !important */
    text-transform: uppercase;
    z-index: 10000;
    pointer-events: none;
    white-space: nowrap;
    opacity: 0;
    animation: footnoteFadeIn 1.2s ease-out 3.0s forwards;
}

@keyframes footnoteFadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
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
    animation:fadeUp 1.6s ease-out 2s both;
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
    max-width:240px;
    margin:0 auto 10px auto;
  }
  #viz-canvas {
    display:block;
    width:100%;
    height:28px;
  }

  .player-container {
    width:100%;
    max-width:250px;
    margin:0 auto;
    display:flex;
    align-items:center;
    gap:14px;
    padding-right:5px;
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
    position:relative;
  }
  #play-btn svg { width:13px; height:13px; fill:#7A6E65; }
  #play-btn .spinner {
    position:absolute;
    width:20px; height:20px;
    border:2px solid #DDD6CE;
    border-top:2px solid #9B8B75;
    border-radius:50%;
    animation: spin 0.8s linear infinite;
    display:none;
  }
  @keyframes spin { to { transform: rotate(360deg); } }

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
    transition: width 0.15s ease-out;
  }
  #scrubber {
    position:absolute;
    top:50%; left:0%;
    transform:translate(-50%,-50%);
    width:9px; height:9px;
    border-radius:50%;
    background:#9B8B75;
    transition: left 0.15s ease-out;
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
</style>
</head>
<body>

<div class="page">
  <p class="title">Chapter 48</p>
  <p class="subtitle">An intermezzo before the pages ahead</p>
  <div class="player-block">
    <div class="divider"></div>
    <p class="track">Brahms: Intermezzo Op. 118, No. 2 (1893)</p>

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
        <div class="spinner" id="loading-spinner"></div>
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

<!-- 纸屑 canvas (保留) -->
<canvas id="confetti-canvas" style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999;"></canvas>

<script>
  // ========== 纸屑炮 ==========
  (function() {
    const cc     = document.getElementById('confetti-canvas');
    const cx     = cc.getContext('2d');
    const COLORS = ['#E8A0BF','#F4C842','#6EC6E6','#A8D8A8','#C4A0E8','#F4855A','#7EC8C8','#F4E04D'];
    const TOTAL  = 160;
    let particles = [];
    let startedAt = null;
    const DURATION = 4000;

    function resize() {
      cc.width  = window.innerWidth;
      cc.height = window.innerHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    function spawn() {
      particles = [];
      for (let i = 0; i < TOTAL; i++) {
        const fromLeft = i < TOTAL / 2;
        const x = fromLeft ? -10 : cc.width + 10;
        const angle = fromLeft
          ? (-75 + Math.random() * 65) * Math.PI / 180
          : (-170 + Math.random() * 65) * Math.PI / 180;
        const speed = 1.5 + Math.random() * 10;
        particles.push({
          x,
          y: cc.height * (0.25 + Math.random() * 0.15),
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed,
          color: COLORS[Math.floor(Math.random() * COLORS.length)],
          w: 6 + Math.random() * 6,
          h: 3 + Math.random() * 4,
          rot: Math.random() * Math.PI * 2,
          rotV: (Math.random() - 0.5) * 0.25,
          opacity: 1,
        });
      }
    }

    function tick(now) {
      if (!startedAt) startedAt = now;
      const elapsed = now - startedAt;
      if (elapsed > DURATION) {
        cx.clearRect(0, 0, cc.width, cc.height);
        return;
      }
      cx.clearRect(0, 0, cc.width, cc.height);
      const fade = Math.max(0, 1 - elapsed / DURATION);
      for (const p of particles) {
        p.x   += p.vx;
        p.y   += p.vy;
        p.vy  += 0.28;
        p.vx  *= 0.985;
        p.rot += p.rotV;
        cx.save();
        cx.globalAlpha = fade * p.opacity;
        cx.translate(p.x, p.y);
        cx.rotate(p.rot);
        cx.fillStyle = p.color;
        cx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
        cx.restore();
      }
      requestAnimationFrame(tick);
    }

    setTimeout(() => {
      spawn();
      requestAnimationFrame(tick);
    }, 500);
  })();
</script>

<script>
  // ========== DOM 元素 ==========
  const playBtn      = document.getElementById('play-btn');
  const iconPlay     = document.getElementById('icon-play');
  const iconPause    = document.getElementById('icon-pause');
  const spinner      = document.getElementById('loading-spinner');
  const fill         = document.getElementById('progress-fill');
  const scrubber     = document.getElementById('scrubber');
  const progressWrap = document.getElementById('progress-wrap');
  const tooltip      = document.getElementById('time-tooltip');

  // ========== 音频状态 ==========
  let audioCtx      = null;
  let audioBuffer   = null;
  let gainNode      = null;
  let analyser      = null;
  let dataArray     = null;

  let sourceNode    = null;
  let startTime     = 0;
  let startOffset   = 0;
  let pausedAt      = 0;
  let isPlaying     = false;
  let duration      = 0;

  let tooltipTimer        = null;
  let draggingProgress    = false;
  let lastDragPct         = null;
  let visualBufferActive  = false;
  let visualBufferTimeout = null;

  let animationFrame = null;
  let isLoadingAudio = false;

  // ========== 工具函数 ==========
  function fmt(s) {
    if (!isFinite(s) || isNaN(s) || s < 0) return '';
    return Math.floor(s/60) + ':' + String(Math.floor(s%60)).padStart(2,'0');
  }

  function showTooltip(pct, t) {
    const label = fmt(t);
    if (!label) return;
    tooltip.textContent = label + (duration ? ' / ' + fmt(duration) : '');
    tooltip.style.left = Math.max(5, Math.min(95, pct*100)) + '%';
    tooltip.style.opacity = '1';
    clearTimeout(tooltipTimer);
    tooltipTimer = setTimeout(() => tooltip.style.opacity='0', 1500);
  }

  function updateProgress(pct) {
    fill.style.width    = (pct*100) + '%';
    scrubber.style.left = (pct*100) + '%';
  }

  function showLoading(show) {
    if (show) {
      iconPlay.style.display  = 'none';
      iconPause.style.display = 'none';
      spinner.style.display   = 'block';
      playBtn.style.pointerEvents = 'none';
    } else {
      spinner.style.display = 'none';
      playBtn.style.pointerEvents = 'auto';
      if (isPlaying) {
        iconPlay.style.display  = 'none';
        iconPause.style.display = 'block';
      } else {
        iconPlay.style.display  = 'block';
        iconPause.style.display = 'none';
      }
    }
  }

  // ========== 下载并解码音频 ==========
  async function loadAudioBuffer() {
    if (audioBuffer) return;
    if (isLoadingAudio) return;
    isLoadingAudio = true;
    showLoading(true);
    console.log('开始下载音频...');
    try {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        analyser = audioCtx.createAnalyser();
        analyser.fftSize = 2048;
        analyser.smoothingTimeConstant = 0.75;
        gainNode = audioCtx.createGain();
        gainNode.gain.value = 0;
        analyser.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        dataArray = new Uint8Array(analyser.frequencyBinCount);
      }
      const response = await fetch("__AUDIO_URL__");
      if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
      const arrayBuffer = await response.arrayBuffer();
      console.log('下载完成，开始解码...');
      audioBuffer = await audioCtx.decodeAudioData(arrayBuffer);
      duration = audioBuffer.duration;
      console.log('解码成功，时长:', duration);
    } catch (err) {
      console.error('音频加载失败:', err);
      alert('音频加载失败，请检查网络或CORS。');
    } finally {
      isLoadingAudio = false;
      showLoading(false);
    }
  }

  // ========== 安全淡入/淡出 ==========
  function fadeOutQuick() {
    if (!gainNode) return;
    const now = audioCtx.currentTime;
    gainNode.gain.cancelScheduledValues(now);
    gainNode.gain.setValueAtTime(gainNode.gain.value, now);
    gainNode.gain.linearRampToValueAtTime(0, now + 0.005);
  }

  function fadeInSmooth() {
    if (!gainNode) return;
    const now = audioCtx.currentTime;
    gainNode.gain.cancelScheduledValues(now);
    gainNode.gain.setValueAtTime(0, now);
    gainNode.gain.linearRampToValueAtTime(1.0, now + 0.04);
  }

  function muteInstant() {
    if (!gainNode) return;
    const now = audioCtx.currentTime;
    gainNode.gain.cancelScheduledValues(now);
    gainNode.gain.setValueAtTime(0, now);
  }

  // ========== 播放核心 ==========
  function stopSource() {
    if (sourceNode) {
      try { sourceNode.stop(0); } catch(e) {}
      sourceNode.disconnect();
      sourceNode = null;
    }
  }

  function playFrom(offset) {
    fadeOutQuick();
    setTimeout(() => {
      stopSource();
      if (!audioBuffer || !gainNode) return;
      sourceNode = audioCtx.createBufferSource();
      sourceNode.buffer = audioBuffer;
      sourceNode.connect(analyser);
      startOffset = offset;
      startTime = audioCtx.currentTime;
      muteInstant();
      sourceNode.start(0, offset);
      setTimeout(fadeInSmooth, 10);
      isPlaying = true;
      iconPlay.style.display  = 'none';
      iconPause.style.display = 'block';
      sourceNode.onended = () => {
        if (isPlaying && sourceNode) {
          const elapsed = audioCtx.currentTime - startTime;
          const endPos = startOffset + elapsed;
          if (endPos >= duration - 0.1) {
            stopSource();
            isPlaying = false;
            pausedAt = duration;
            iconPlay.style.display  = 'block';
            iconPause.style.display = 'none';
            updateProgress(1);
          }
        }
      };
    }, 6);
  }

  function pause() {
    if (!isPlaying) return;
    const elapsed = audioCtx.currentTime - startTime;
    pausedAt = Math.min(startOffset + elapsed, duration);
    fadeOutQuick();
    setTimeout(() => {
      stopSource();
      isPlaying = false;
      iconPlay.style.display  = 'block';
      iconPause.style.display = 'none';
    }, 6);
  }

  // ========== 拖拽逻辑 ==========
  function progressPct(e) {
    const rect = progressWrap.getBoundingClientRect();
    const x = e.touches ? e.touches[0].clientX : e.clientX;
    return Math.max(0, Math.min(1, (x - rect.left) / rect.width));
  }

  function dragMove(e) {
    if (!draggingProgress) return;
    lastDragPct = progressPct(e);
    updateProgress(lastDragPct);
    showTooltip(lastDragPct, lastDragPct * (duration || 0));
  }

  function dragStart(e) {
    draggingProgress = true;
    lastDragPct = progressPct(e);
    updateProgress(lastDragPct);
    fill.style.transition    = 'none';
    scrubber.style.transition = 'none';
    visualBufferActive = true;
    clearTimeout(visualBufferTimeout);
    e.preventDefault();
  }

  function dragEnd() {
    if (!draggingProgress) return;
    draggingProgress = false;
    fill.style.transition    = 'width 0.15s ease-out';
    scrubber.style.transition = 'left 0.15s ease-out';
    if (lastDragPct !== null && duration) {
      const targetTime = lastDragPct * duration;
      pausedAt = targetTime;
      if (isPlaying) {
        playFrom(targetTime);
      } else {
        updateProgress(lastDragPct);
      }
    }
    visualBufferTimeout = setTimeout(() => {
      visualBufferActive = false;
      if (!draggingProgress && !isPlaying) {
        updateProgress(pausedAt / duration);
      }
    }, 150);
  }

  progressWrap.addEventListener('mousedown', dragStart);
  progressWrap.addEventListener('touchstart', dragStart, {passive: false});
  window.addEventListener('mousemove', dragMove);
  window.addEventListener('touchmove', dragMove, {passive: false});
  window.addEventListener('mouseup', dragEnd);
  window.addEventListener('touchend', dragEnd);

  // ========== 播放/暂停按钮 ==========
  playBtn.addEventListener('click', async () => {
    if (!audioBuffer) {
      await loadAudioBuffer();
      if (!audioBuffer) return;
    }
    if (audioCtx.state === 'suspended') {
      await audioCtx.resume();
    }
    if (isPlaying) {
      pause();
    } else {
      if (pausedAt >= duration) pausedAt = 0;
      playFrom(pausedAt);
    }
  });

  // ========== 进度条自动更新 ==========
  function updateTimeDisplay() {
    if (!draggingProgress && !visualBufferActive && isPlaying) {
      const elapsed = audioCtx.currentTime - startTime;
      const pos = startOffset + elapsed;
      if (pos <= duration) {
        updateProgress(pos / duration);
      }
    } else if (!isPlaying && !draggingProgress && !visualBufferActive) {
      if (duration) updateProgress(pausedAt / duration);
    }
    animationFrame = requestAnimationFrame(updateTimeDisplay);
  }
  updateTimeDisplay();

  // ========== 可视化 ==========
  const canvas = document.getElementById('viz-canvas');
  const ctx    = canvas.getContext('2d');
  const BAR_COUNT = 44;
  const BAR_GAP   = 2;
  const MAX_H     = 24;
  const MIN_H     = 2;
  let barBins = null;

  function buildBarBins() {
    const sampleRate = audioCtx.sampleRate;
    const totalBins  = analyser.frequencyBinCount;
    const hzPerBin   = sampleRate / analyser.fftSize;
    const freqMin = 60;
    const freqMax = 2600;
    barBins = new Array(BAR_COUNT);
    for (let i = 0; i < BAR_COUNT; i++) {
      const t = i / (BAR_COUNT - 1);
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
    canvas.height = 28 * dpr;
    ctx.scale(dpr, dpr);
  }
  resizeCanvas();
  window.addEventListener('resize', resizeCanvas);

  let tickCount = 0;
  function drawViz() {
    const dpr = window.devicePixelRatio || 1;
    const W = canvas.width / dpr;
    const H = canvas.height / dpr;
    ctx.clearRect(0, 0, W, H);
    const BAR_W = (W - (BAR_COUNT - 1) * BAR_GAP) / BAR_COUNT;
    const playing = isPlaying;

    if (playing && analyser && dataArray) {
      if (!barBins) buildBarBins();
      analyser.getByteFrequencyData(dataArray);
      for (let i = 0; i < BAR_COUNT; i++) {
        const raw = dataArray[barBins[i]] / 255;
        const t = i / (BAR_COUNT - 1);
        let eqGain;
        if (t < 0.07) { eqGain = 0.25; }
        else if (t < 0.65) { eqGain = 0.1 + Math.pow((t - 0.07) / 0.58, 0.8) * 1.4; }
        else { eqGain = 1.0 + Math.pow((t - 0.65) / 0.35, 1.0) * 5.0; }
        const boosted = Math.min(1, raw * eqGain);
        const barMax = t < 0.65 ? MAX_H : MAX_H - Math.pow((t - 0.65) / 0.35, 0.7) * 15;
        bars[i].target = MIN_H + boosted * (barMax - MIN_H);
      }
    } else {
      if (++tickCount >= 5) {
        tickCount = 0;
        for (let i = 0; i < BAR_COUNT; i++) {
          bars[i].target = playing ? MIN_H + Math.random() * (MAX_H - MIN_H) : MIN_H;
        }
      }
    }

    let x = 0;
    for (let i = 0; i < BAR_COUNT; i++) {
      bars[i].h += (bars[i].target - bars[i].h) * bars[i].speed;
      if (bars[i].h < MIN_H) bars[i].h = MIN_H;
      const barH = bars[i].h;
      const y = (H - barH) / 2;
      ctx.fillStyle = '#B8A898';
      ctx.beginPath();
      ctx.roundRect(x, y, BAR_W, barH, 1);
      ctx.fill();
      x += BAR_W + BAR_GAP;
    }
    requestAnimationFrame(drawViz);
  }
  drawViz();

  // 清理
  window.addEventListener('beforeunload', () => {
    stopSource();
    if (audioCtx) audioCtx.close();
  });
</script>
</body>
</html>
"""

# 渲染播放器组件
components.html(HTML.replace("__AUDIO_URL__", AUDIO_URL), height=900, scrolling=False)

# 脚注直接用 Streamlit 的 markdown 放在页面底部（固定定位）
st.markdown('<p class="footnote-streamlit">Douglas</p>', unsafe_allow_html=True)