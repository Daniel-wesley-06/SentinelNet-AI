import streamlit as st


def render_header():
    """Render the main header section with title and subtitle."""

    st.markdown(
        """
        <div style="text-align: center; padding: 2rem 0 1rem 0;">
            <div style="display: inline-flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                <span style="font-size: 2.5rem;">🛡️</span>
                <h1 class="main-title" style="margin: 0;">SentinelNet AI</h1>
            </div>
            <p class="subtitle">Network Intrusion Detection System — Detection on Unseen Synthetic Traffic</p>
            <div style="
                width: 60px;
                height: 3px;
                background: linear-gradient(135deg, #6366f1, #8b5cf6);
                margin: 1rem auto 0 auto;
                border-radius: 2px;
            "></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
