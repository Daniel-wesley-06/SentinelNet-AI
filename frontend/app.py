import sys
from pathlib import Path

# Add parent directory to path so we can import data_loader
sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st

# Local imports
from styles.theme import inject_css, get_theme_colors
from data_loader import call_backend_api, check_backend_health
from components.header import render_header
from components.control_panel import render_control_panel
from components.metrics import render_metrics
from components.charts import render_all_charts


# ─── Page Config ───
st.set_page_config(
    page_title="SentinelNet AI — Intrusion Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Initialize Session State ───
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = True

if "results" not in st.session_state:
    st.session_state["results"] = None

if "metrics" not in st.session_state:
    st.session_state["metrics"] = None

# ─── Inject Theme CSS ───
is_dark = st.session_state.get("dark_mode", True)
inject_css(is_dark)

# ─── Header ───
render_header()

st.divider()

# ─── Backend Status Check ───
backend_online = check_backend_health()

# ─── Control Panel ───
detect_clicked, sample_size = render_control_panel()

if not backend_online:
    st.warning(
        "⚠️ Backend API is not running. Start it with: "
        "`python -m uvicorn backend.main:app --reload`",
        icon="🔌",
    )

st.divider()

# ─── Detection Pipeline ───
if detect_clicked:
    if not backend_online:
        st.error("❌ Cannot run detection — backend API is offline. Please start the backend first.")
    else:
        with st.spinner("🔄 Running ensemble detection (IF + SVM) on sampled data..."):
            try:
                results_df, metrics = call_backend_api(sample_size=sample_size)

                # Store in session state
                st.session_state["results"] = results_df
                st.session_state["metrics"] = metrics

            except Exception as e:
                st.error(f"❌ Backend error: {str(e)}")
                st.stop()

        st.success(
            f"✅ Detection complete! Analyzed **{metrics['total_samples']}** samples — "
            f"**{metrics['attack_count']}** attacks detected, "
            f"**{metrics['normal_count']}** normal traffic.",
            icon="🛡️",
        )

# ─── Results Section ───
if st.session_state["results"] is not None and st.session_state["metrics"] is not None:
    results_df = st.session_state["results"]
    metrics = st.session_state["metrics"]

    # Metrics Section
    render_metrics(metrics)

    st.divider()

    # Charts Section
    render_all_charts(metrics, results_df, is_dark)

else:
    # Empty state — prompt user to click detect
    st.markdown(
        """
        <div style="
            text-align: center;
            padding: 4rem 2rem;
            opacity: 0.6;
        ">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🛡️</div>
            <h3 style="color: inherit; font-weight: 600;">Ready to Analyze</h3>
            <p style="font-size: 1.1rem; max-width: 500px; margin: 0.5rem auto;">
                Click <strong>"🔍 Detect Attacks"</strong> to sample data and run the
                ensemble intrusion detection model.
            </p>
            <p style="font-size: 0.85rem; margin-top: 1rem; opacity: 0.7;">
                Ensemble: Isolation Forest (0.4) + One-Class SVM (0.6)
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─── Footer ───
st.markdown(
    """
    <div style="
        text-align: center;
        padding: 2rem 0 1rem 0;
        opacity: 0.4;
        font-size: 0.8rem;
    ">
        SentinelNet AI • Network Intrusion Detection System • Ensemble Model (IF + SVM)
    </div>
    """,
    unsafe_allow_html=True,
)
