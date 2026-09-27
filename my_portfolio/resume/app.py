from __future__ import annotations

import base64
import mimetypes
from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
CSS_PATH = APP_DIR / "style.css"
PROFILE_IMAGE = next(
    (
        path
        for path in (APP_DIR / "dp.jpg", APP_DIR / "dp.jpeg", APP_DIR / "dp.png")
        if path.is_file() and path.stat().st_size > 0
    ),
    None,
)

st.set_page_config(
    page_title="Durga Manohar Bachu | AI & ML Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def profile_image_markup() -> str:
    if PROFILE_IMAGE is not None:
        encoded = base64.b64encode(PROFILE_IMAGE.read_bytes()).decode("ascii")
        media_type = mimetypes.guess_type(PROFILE_IMAGE.name)[0] or "image/png"
        return (
            '<img class="profile-image" '
            f'src="data:{media_type};base64,{encoded}" '
            'alt="Portrait of Durga Manohar Bachu">'
        )
    return '<div class="profile-image profile-fallback" aria-label="DM">DM</div>'


portfolio = f"""
<nav class="topbar">
  <a class="brand" href="#home">Durga Manohar Bachu<span class="brand-dot">.</span></a>
  <div class="nav-links">
    <a href="#home">Home</a><a href="#projects">Projects</a>
    <a href="#education">Education</a><a href="#skills">Skills</a>
    <a href="#social">Social Media</a>
  </div>
</nav>
<main class="page-wrap">
  <section class="hero" id="home">
    <div class="eyebrow"><span class="eyebrow-mark"></span> AI &amp; MACHINE LEARNING</div>
    {profile_image_markup()}
    <h1>Durga Manohar Bachu</h1>
    <p class="hero-role">Artificial Intelligence &amp; Machine Learning Student</p>
    <p class="hero-school">Sandip University <span>·</span> B.Tech</p>
    <div class="hero-actions">
      <a class="primary-link" href="#projects">Explore my work <span>↘</span></a>
      <a class="text-link" href="mailto:manumanohar7195@gmail.com">Get in touch</a>
    </div>
  </section>

  <section class="content-section" id="summary">
    <div class="section-heading"><span class="section-index">01</span><div><p class="section-kicker">A LITTLE ABOUT ME</p><h2>Profile summary</h2></div></div>
    <div class="summary-card">
      <p>I’m a B.Tech student in Artificial Intelligence &amp; Machine Learning, interested in building useful applications with modern AI. My work and learning focus on LLM fundamentals, agentic workflows, retrieval augmented generation, and voice interfaces.</p>
      <div class="summary-tags"><span>LLM applications</span><span>AI agents</span><span>RAG</span><span>Python</span></div>
    </div>
  </section>

  <section class="content-section" id="projects">
    <div class="section-heading"><span class="section-index">02</span><div><p class="section-kicker">SELECTED WORK</p><h2>Projects</h2></div></div>
    <div class="project-grid">
      <article class="project-card featured-project">
        <div class="project-topline"><span class="project-type">ENTERPRISE PROJECT</span><span class="project-year">2026</span></div>
        <h3>Enterprise Multi-Agent AI Workflow</h3>
        <p>A task-oriented AI workflow with specialized agents and a retrieval layer for relevant document context.</p>
        <ul>
          <li>Built agent routing with LangGraph for task-specific execution.</li>
          <li>Integrated Qdrant and RAG for document retrieval and context.</li>
          <li>Handled document loading, chunking, embeddings, similarity search, and relevance handling.</li>
          <li>Explored SQL and database integration alongside the knowledge layer.</li>
        </ul>
        <div class="tech-list"><span>LangGraph</span><span>Qdrant</span><span>RAG</span><span>SQL</span></div>
      </article>
      <article class="project-card">
        <div class="project-topline"><span class="project-type">AI APPLICATION</span><span class="project-year">2026</span></div>
        <h3>AI Voice Assistant</h3>
        <p>A voice-first assistant that processes spoken requests and returns AI-generated responses.</p>
        <ul>
          <li>Implemented voice-based interaction and command handling.</li>
          <li>Integrated an online Q&amp;A model to process requests and generate responses.</li>
        </ul>
        <div class="tech-list"><span>Python</span><span>AI assistant</span><span>Voice interaction</span></div>
      </article>
    </div>
  </section>

  <section class="content-section" id="education">
    <div class="section-heading"><span class="section-index">03</span><div><p class="section-kicker">LEARNING JOURNEY</p><h2>Education &amp; certification</h2></div></div>
    <div class="timeline">
      <article class="timeline-item"><span class="timeline-dot"></span><div class="timeline-title-row"><div><h3>B.Tech, Artificial Intelligence &amp; Machine Learning</h3><p class="timeline-place">Sandip University</p></div><span class="timeline-date">2026 – Present</span></div><p class="timeline-detail">4th Year <span>·</span> 8.0 CGPA</p></article>
      <article class="timeline-item"><span class="timeline-dot"></span><div class="timeline-title-row"><div><h3>Intermediate (12th)</h3><p class="timeline-place">947 / 1000 marks</p></div><span class="timeline-date">94.7%</span></div></article>
      <article class="timeline-item"><span class="timeline-dot"></span><div class="timeline-title-row"><div><h3>10th Class</h3><p class="timeline-place">10 / 10 CGPA</p></div></div></article>
    </div>
    <article class="cert-card"><div class="cert-icon">✦</div><div><p class="section-kicker">CERTIFICATION · 2026</p><h3>Agentic AI Certification</h3><p>KIET Institution · Training covering agentic AI concepts, agents, workflows, practical implementation, and an AI assistant project.</p></div></article>
  </section>

  <section class="content-section" id="skills">
    <div class="section-heading"><span class="section-index">04</span><div><p class="section-kicker">TOOLS &amp; KNOWLEDGE</p><h2>Skills</h2></div></div>
    <div class="skills-panel">
      <div class="skill-row"><h3>Programming</h3><div class="skill-chips"><span>Python</span></div></div>
      <div class="skill-row"><h3>APIs</h3><div class="skill-chips"><span>FastAPI</span><span>API integration</span><span>API keys</span></div></div>
      <div class="skill-row"><h3>LLM &amp; agents</h3><div class="skill-chips"><span>LLM fundamentals</span><span>Multi-agent systems</span><span>Tool calling</span><span>Deep agents</span><span>ReAct</span><span>MCPs</span></div></div>
      <div class="skill-row"><h3>Frameworks</h3><div class="skill-chips"><span>LangChain</span><span>LangGraph</span></div></div>
      <div class="skill-row"><h3>Retrieval</h3><div class="skill-chips"><span>RAG</span><span>Multimodal RAG</span><span>Vectorless RAG</span></div></div>
      <div class="skill-row"><h3>AI reliability</h3><div class="skill-chips"><span>Guardrails</span><span>LLM evaluation frameworks</span></div></div>
      <div class="skill-row"><h3>Languages</h3><div class="skill-chips"><span>English</span><span>Hindi</span><span>Telugu</span></div></div>
    </div>
  </section>

  <section class="content-section social-section" id="social">
    <div class="section-heading"><span class="section-index">05</span><div><p class="section-kicker">FIND ME ONLINE</p><h2>Social media</h2></div></div>
    <div class="social-card">
      <a class="social-link" href="https://www.linkedin.com/in/manoharbatchu/" target="_blank" rel="noopener noreferrer"><span class="social-icon">in</span><span><strong>LinkedIn</strong><small>Connect with me professionally</small></span><span class="social-arrow">↗</span></a>
      <a class="social-link" href="https://github.com/" target="_blank" rel="noopener noreferrer"><span class="social-icon github-mark">GH</span><span><strong>GitHub</strong><small>Explore code and projects</small></span><span class="social-arrow">↗</span></a>
      <a class="social-link" href="mailto:manumanohar7195@gmail.com"><span class="social-icon mail-mark">@</span><span><strong>Email</strong><small>manumanohar7195@gmail.com</small></span><span class="social-arrow">↗</span></a>
      <a class="social-link" href="tel:9095984467"><span class="social-icon mail-mark">☎</span><span><strong>Phone</strong><small>9095984467</small></span><span class="social-arrow">↗</span></a>
    </div>
  </section>
  <footer class="footer"><a class="brand footer-brand" href="#home">Durga Manohar Bachu<span class="brand-dot">.</span></a><span>AI &amp; Machine Learning · 2026</span><a href="#home">Back to top ↑</a></footer>
</main>
"""

styles = CSS_PATH.read_text(encoding="utf-8") if CSS_PATH.is_file() else ""
st.html(f"<style>{styles}</style>{portfolio}", width="stretch")
