import streamlit as st


def render_control_panel() -> tuple[bool, int]:
    """
    Render the control panel with detect button, sample slider, and theme toggle.
    Returns (detect_clicked, sample_size).
    """

    st.markdown(
        '<div class="section-header">⚙️ Control Panel</div>',
        unsafe_allow_html=True,
    )

    col_controls, col_spacer, col_theme = st.columns([5, 3, 2])

    with col_controls:
        sub_col1, sub_col2 = st.columns([1, 2])

        with sub_col1:
            detect_clicked = st.button(
                "🔍 Detect Attacks",
                use_container_width=True,
                type="primary",
                key="detect_btn",
            )

        with sub_col2:
            sample_size = st.slider(
                "📊 Sample Size",
                min_value=100,
                max_value=5000,
                value=2000,
                step=100,
                key="sample_slider",
                help="Number of samples to randomly draw from the 20,000-row dataset",
            )

    with col_theme:
        # Theme toggle
        is_dark = st.session_state.get("dark_mode", True)
        toggle_label = "☀️ Light Mode" if is_dark else "🌙 Dark Mode"

        st.markdown('<div class="theme-toggle">', unsafe_allow_html=True)
        if st.button(toggle_label, key="theme_toggle", use_container_width=True):
            st.session_state["dark_mode"] = not is_dark
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    return detect_clicked, sample_size
