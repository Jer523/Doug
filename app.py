import streamlit as st
import os
import base64

# ─────────────────────────────────────────────
#  Page config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Chapter 48",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  CSS INJECTION
# ─────────────────────────────────────────────
st.markdown("""
<style>

/* ── 1. HIDE DEFAULT STREAMLIT CHROME ─────── */
#MainMenu,
header[data-testid="stHeader"],
footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
}

/* ── 2. PAPER-TONE BACKGROUND ──────────────── */
html,
body,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
.main,
.block-container {
    background-color: #FDFBF7 !important;
    margin: 0;
    padding: 0;
}

/* ── 3. BLOCK CONTAINER — VERTICAL OFFSET ─── */
.block-container {
    max-width: 640px !important;
    padding-top: 18vh !important;
    padding-bottom: 12vh !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* ── 4. GOOGLE FONT IMPORT + GLOBAL TYPOGRAPHY */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap');

* {
    font-family: 'Playfair Display', Georgia, 'Times New Roman', serif !important;
    color: #4A4A4A;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}

/* ── 5. CENTRED TEXT ───────────────────────── */
p, h1, h2, h3, h4, h5, h6,
.stMarkdown, .stMarkdown p {
    text-align: center !important;
}

/* ── 6. AUDIO PLAYER ───────────────────────── */
audio {
    display: block !important;
    margin: 0 auto !important;
    width: 100% !important;
    max-width: 420px !important;
    accent-color: #9B8B75 !important;
    opacity: 0.85;
}

/* ── 7. FADE-IN KEYFRAMES ──────────────────── */
@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(6px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ── 8. STAGGERED ANIMATION DELAYS ─────────── */
.anim-title    { animation: fadeUp 1.6s ease-out 0.5s both; }
.anim-subtitle { animation: fadeUp 1.6s ease-out 2.0s both; }
.anim-player   { animation: fadeUp 1.4s ease-out 3.5s both; }
.anim-footnote { animation: fadeUp 1.2s ease-out 4.0s both; }

/* ── 9. COMPONENT TYPOGRAPHY ───────────────── */

/* Title — fixed px for reliability on mobile */
.title-text {
    font-size: 52px;
    font-weight: 500;
    letter-spacing: 0.06em;
    color: #333333;
    margin-bottom: 0.5rem;
    line-height: 1.15;
}

/* Subtitle */
.subtitle-text {
    font-size: 18px;
    font-style: italic;
    font-weight: 400;
    color: #6A6A6A;
    letter-spacing: 0.02em;
    margin-bottom: 2.8rem;
    line-height: 1.6;
}

/* Track / composer info — deliberately small and muted */
.track-text {
    font-size: 11px;
    font-weight: 400;
    color: #9B9083;
    letter-spacing: 0.08em;
    margin-bottom: 0.55rem;
    line-height: 1.5;
}

/* Thin decorative rule */
.divider {
    width: 36px;
    height: 1px;
    background-color: #C8BFB0;
    margin: 0 auto 2.4rem auto;
}

/* Footnote — fixed to bottom of viewport */
.footnote-text {
    font-size: 9px;
    color: #B8B0A5;
    letter-spacing: 0.55em;
    text-transform: uppercase;
    position: fixed;
    bottom: 1.8rem;
    left: 0;
    right: 0;
    text-align: center;
    margin: 0;
}

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  AUDIO
#  Put your mp3 at:  assets/brahms_op118_no2.mp3
# ─────────────────────────────────────────────
AUDIO_PATH = "assets/brahms_op118_no2.mp3"

audio_html = ""
if os.path.exists(AUDIO_PATH):
    with open(AUDIO_PATH, "rb") as f:
        audio_bytes = f.read()
    audio_b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
    <audio controls preload="metadata">
      <source src="data:audio/mpeg;base64,{audio_b64}" type="audio/mpeg">
    </audio>
    """


# ─────────────────────────────────────────────
#  PAGE CONTENT
# ─────────────────────────────────────────────
st.markdown(f"""

<!-- ① TITLE -->
<div class="anim-title">
    <p class="title-text">Chapter 48</p>
</div>

<!-- ② SUBTITLE -->
<div class="anim-subtitle">
    <p class="subtitle-text">An intermezzo before the pages ahead.</p>
</div>

<!-- ③ TRACK INFO + ④ AUDIO PLAYER -->
<div class="anim-player">
    <div class="divider"></div>
    <p class="track-text">Brahms: Intermezzo Op. 118, No. 2 (1893)</p>
    {audio_html}
</div>

<!-- ⑤ FOOTNOTE — fixed to bottom -->
<div class="anim-footnote">
    <p class="footnote-text">Douglas</p>
</div>

""", unsafe_allow_html=True)
