import streamlit as st

# ─────────────────────────────────────────────
#  Page config — must be the very first Streamlit call
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Chapter 48",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  CSS INJECTION
#  Everything between the <style> tags is pure CSS.
#  Sections are clearly commented for easy editing.
# ─────────────────────────────────────────────
st.markdown("""
<style>

/* ── 1. HIDE DEFAULT STREAMLIT CHROME ─────────────────────────────────────
   Removes the top header bar, the footer "Made with Streamlit" bar,
   the hamburger/kebab menu button, and the deploy button.
   These selectors target Streamlit's internal DOM structure and may need
   updating if Streamlit releases a major version change.
   ────────────────────────────────────────────────────────────────────── */
#MainMenu,
header[data-testid="stHeader"],
footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
    visibility: hidden !important;
}

/* ── 2. GLOBAL RESET & PAPER-TONE BACKGROUND ──────────────────────────────
   Sets the warm ivory/paper background across every surface Streamlit
   creates: the root, the app view container, and the main block wrapper.
   ────────────────────────────────────────────────────────────────────── */
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

/* ── 3. BLOCK CONTAINER — VERTICAL OFFSET ─────────────────────────────────
   The content sits roughly 25–30 % from the top (via padding-top),
   rather than being vertically centred, so the lower half breathes.
   max-width keeps the column narrow for a book-page feeling.
   ────────────────────────────────────────────────────────────────────── */
.block-container {
    max-width: 640px !important;
    padding-top: 18vh !important;
    padding-bottom: 12vh !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* ── 4. GLOBAL TYPOGRAPHY ─────────────────────────────────────────────────
   Force an elegant serif stack everywhere. Georgia is universally
   available; Playfair Display would require a Google Fonts import (added
   below) and falls back gracefully.
   ────────────────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&display=swap');

* {
    font-family: 'Playfair Display', Georgia, 'Times New Roman', serif !important;
    color: #4A4A4A;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}

/* ── 5. ALL TEXT ELEMENTS — CENTRED ───────────────────────────────────────
   Every paragraph, heading, and custom element aligns to the centre.
   ────────────────────────────────────────────────────────────────────── */
p, h1, h2, h3, h4, h5, h6,
.stMarkdown, .stMarkdown p {
    text-align: center !important;
}

/* ── 6. AUDIO PLAYER — MINIMAL & CENTRED ─────────────────────────────────
   The native <audio> element is display-blocked and centred.
   We strip aggressive browser chrome where possible via accent-color.
   ────────────────────────────────────────────────────────────────────── */
audio {
    display: block !important;
    margin: 0 auto !important;
    width: 100% !important;
    max-width: 420px !important;
    accent-color: #9B8B75 !important;   /* warm sepia tone for controls */
    opacity: 0.85;
}

/* ── 7. FADE-IN KEYFRAMES ─────────────────────────────────────────────────
   A single reusable keyframe: element starts invisible and 4px below
   its resting position, then floats up while fading in.
   The subtle translateY lift gives a "breath" or "emerging" quality.
   ────────────────────────────────────────────────────────────────────── */
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

/* ── 8. STAGGERED ANIMATION CLASSES ──────────────────────────────────────
   Each content tier has its own delay.
   animation-fill-mode: both   → element stays invisible before its delay
                                  and stays visible after the animation ends.
   ────────────────────────────────────────────────────────────────────── */

/* Title  — starts fading in at 0.5 s */
.anim-title {
    animation: fadeUp 1.6s ease-out 0.5s both;
}

/* Subtitle — starts at 2.0 s */
.anim-subtitle {
    animation: fadeUp 1.6s ease-out 2.0s both;
}

/* Track info + audio player — start at 3.5 s */
.anim-player {
    animation: fadeUp 1.4s ease-out 3.5s both;
}

/* Footnote — starts at 4.0 s */
.anim-footnote {
    animation: fadeUp 1.2s ease-out 4.0s both;
}

/* ── 9. COMPONENT-SPECIFIC TYPOGRAPHY ────────────────────────────────────
   Fine-tuned sizes, weights, and spacing for each element tier.
   ────────────────────────────────────────────────────────────────────── */

/* Title */
.title-text {
    font-size: clamp(3.2rem, 9vw, 4.5rem);
    font-weight: 500;
    letter-spacing: 0.06em;
    color: #333333;
    margin-bottom: 0.5rem;
    line-height: 1.15;
}

/* Subtitle */
.subtitle-text {
    font-size: clamp(1rem, 2.4vw, 1.25rem);
    font-style: italic;
    font-weight: 400;
    color: #6A6A6A;
    letter-spacing: 0.02em;
    margin-bottom: 2.8rem;
    line-height: 1.6;
}

/* Track / composer info */
.track-text {
    font-size: clamp(0.7rem, 1.6vw, 0.82rem);
    font-weight: 400;
    color: #9B9083;          /* noticeably muted — secondary hierarchy */
    letter-spacing: 0.08em;
    text-transform: none;
    margin-bottom: 0.55rem;
    line-height: 1.5;
}

/* Decorative thin rule between subtitle and player block */
.divider {
    width: 36px;
    height: 1px;
    background-color: #C8BFB0;
    margin: 0 auto 2.4rem auto;
}

/* Footnote */
.footnote-text {
    font-size: 0.62rem;
    color: #B8B0A5;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    margin-top: 3.8rem;
}

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  AUDIO FILE PATH
#
#  Place your .mp3 file at:   assets/brahms_op118_no2.mp3
#  (relative to where you run `streamlit run app.py`)
#
#  The folder structure should look like:
#
#    your-project/
#    ├── app.py
#    └── assets/
#        └── brahms_op118_no2.mp3   ← put the mp3 here
#
#  If the file is absent, the audio element is simply hidden
#  so the page still renders cleanly during development.
# ─────────────────────────────────────────────
AUDIO_PATH = "assets/brahms_op118_no2.mp3"

import os

audio_html = ""
if os.path.exists(AUDIO_PATH):
    with open(AUDIO_PATH, "rb") as f:
        audio_bytes = f.read()
    import base64
    audio_b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
    <audio controls preload="metadata">
      <source src="data:audio/mpeg;base64,{audio_b64}" type="audio/mpeg">
    </audio>
    """
else:
    # Placeholder: invisible block that reserves space gracefully
    audio_html = """
    <div style="
        width:100%;
        max-width:420px;
        margin:0 auto;
        height:40px;
        border-bottom: 1px solid #D9D2C7;
        opacity:0.4;
    "></div>
    """


# ─────────────────────────────────────────────
#  PAGE CONTENT  (HTML injected via st.markdown)
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

<!-- ③ TRACK INFO + ④ AUDIO PLAYER  (share the same animation tier) -->
<div class="anim-player">
    <div class="divider"></div>
    <p class="track-text">Brahms: Intermezzo Op. 118, No. 2 (1893)</p>
    {audio_html}
</div>

<!-- ⑤ FOOTNOTE -->
<div class="anim-footnote">
    <p class="footnote-text">Douglas</p>
</div>

""", unsafe_allow_html=True)
