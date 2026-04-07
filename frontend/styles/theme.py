import streamlit as st


def get_theme_colors(is_dark: bool) -> dict:
    """Return color palette based on current theme."""
    if is_dark:
        return {
            "bg_primary": "#0a0e1a",
            "bg_secondary": "#111827",
            "bg_card": "rgba(17, 24, 39, 0.8)",
            "bg_card_border": "rgba(99, 102, 241, 0.2)",
            "text_primary": "#f1f5f9",
            "text_secondary": "#94a3b8",
            "text_muted": "#64748b",
            "accent_primary": "#6366f1",
            "accent_secondary": "#8b5cf6",
            "accent_gradient": "linear-gradient(135deg, #6366f1, #8b5cf6, #a78bfa)",
            "success": "#10b981",
            "warning": "#f59e0b",
            "danger": "#ef4444",
            "chart_bg": "rgba(0,0,0,0)",
            "chart_grid": "rgba(148, 163, 184, 0.1)",
            "chart_text": "#94a3b8",
            "plotly_template": "plotly_dark",
            "metric_bg": "linear-gradient(135deg, rgba(99,102,241,0.15), rgba(139,92,246,0.1))",
            "shadow": "0 8px 32px rgba(0, 0, 0, 0.3)",
            "glass_bg": "rgba(17, 24, 39, 0.6)",
            "glass_border": "rgba(99, 102, 241, 0.15)",
        }
    else:
        return {
            "bg_primary": "#f8fafc",
            "bg_secondary": "#ffffff",
            "bg_card": "rgba(255, 255, 255, 0.9)",
            "bg_card_border": "rgba(99, 102, 241, 0.15)",
            "text_primary": "#0f172a",
            "text_secondary": "#475569",
            "text_muted": "#94a3b8",
            "accent_primary": "#6366f1",
            "accent_secondary": "#8b5cf6",
            "accent_gradient": "linear-gradient(135deg, #6366f1, #8b5cf6, #a78bfa)",
            "success": "#059669",
            "warning": "#d97706",
            "danger": "#dc2626",
            "chart_bg": "rgba(0,0,0,0)",
            "chart_grid": "rgba(15, 23, 42, 0.08)",
            "chart_text": "#475569",
            "plotly_template": "plotly_white",
            "metric_bg": "linear-gradient(135deg, rgba(99,102,241,0.08), rgba(139,92,246,0.05))",
            "shadow": "0 8px 32px rgba(15, 23, 42, 0.08)",
            "glass_bg": "rgba(255, 255, 255, 0.7)",
            "glass_border": "rgba(99, 102, 241, 0.1)",
        }


def inject_css(is_dark: bool):
    """Inject custom CSS based on current theme."""
    c = get_theme_colors(is_dark)

    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* ===== Global Reset ===== */
    .stApp {{
        background: {c["bg_primary"]};
        font-family: 'Inter', sans-serif;
        transition: background 0.4s ease;
    }}

    /* ===== Hide Streamlit default elements ===== */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* ===== Scrollbar ===== */
    ::-webkit-scrollbar {{
        width: 6px;
        height: 6px;
    }}
    ::-webkit-scrollbar-track {{
        background: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
        background: {c["accent_primary"]}40;
        border-radius: 10px;
    }}

    /* ===== Header Title ===== */
    .main-title {{
        font-size: 2.8rem;
        font-weight: 800;
        background: {c["accent_gradient"]};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0;
        letter-spacing: -0.5px;
        line-height: 1.2;
    }}

    .subtitle {{
        font-size: 1.15rem;
        color: {c["text_secondary"]};
        font-weight: 400;
        margin-top: 4px;
        letter-spacing: 0.3px;
    }}

    /* ===== Section Headers ===== */
    .section-header {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {c["text_primary"]};
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid {c["accent_primary"]}30;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}

    /* ===== Card Container ===== */
    .glass-card {{
        background: {c["glass_bg"]};
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid {c["glass_border"]};
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: {c["shadow"]};
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .glass-card:hover {{
        border-color: {c["accent_primary"]}40;
        box-shadow: {c["shadow"]}, 0 0 20px {c["accent_primary"]}10;
        transform: translateY(-2px);
    }}

    /* ===== Metric Cards ===== */
    div[data-testid="stMetric"] {{
        background: {c["metric_bg"]};
        border: 1px solid {c["bg_card_border"]};
        border-radius: 16px;
        padding: 1.2rem 1.5rem;
        box-shadow: {c["shadow"]};
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    div[data-testid="stMetric"]:hover {{
        transform: translateY(-4px);
        border-color: {c["accent_primary"]}50;
        box-shadow: 0 12px 40px {c["accent_primary"]}15;
    }}

    div[data-testid="stMetric"] label {{
        color: {c["text_secondary"]} !important;
        font-weight: 600;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {{
        font-size: 2rem;
        font-weight: 800;
        color: {c["text_primary"]} !important;
    }}

    div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {{
        font-weight: 600;
    }}

    /* ===== Buttons ===== */
    .stButton > button {{
        background: {c["accent_gradient"]} !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.7rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        letter-spacing: 0.3px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 15px {c["accent_primary"]}40 !important;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px {c["accent_primary"]}50 !important;
    }}

    .stButton > button:active {{
        transform: translateY(0) !important;
    }}

    /* ===== Theme Toggle Button ===== */
    .theme-toggle .stButton > button {{
        background: {c["glass_bg"]} !important;
        color: {c["text_primary"]} !important;
        border: 1px solid {c["glass_border"]} !important;
        box-shadow: none !important;
        padding: 0.4rem 1rem !important;
        font-size: 0.9rem !important;
    }}

    .theme-toggle .stButton > button:hover {{
        border-color: {c["accent_primary"]} !important;
        box-shadow: 0 4px 12px {c["accent_primary"]}20 !important;
    }}

    /* ===== Slider ===== */
    .stSlider > div > div > div > div {{
        background: {c["accent_gradient"]} !important;
    }}

    .stSlider p {{
        color: {c["text_secondary"]} !important;
        font-weight: 500;
    }}

    /* ===== DataFrame ===== */
    .stDataFrame {{
        border: 1px solid {c["glass_border"]};
        border-radius: 12px;
        overflow: hidden;
    }}

    /* ===== Divider ===== */
    hr {{
        border-color: {c["glass_border"]} !important;
        margin: 2rem 0 !important;
    }}

    /* ===== Spinner ===== */
    .stSpinner > div {{
        border-top-color: {c["accent_primary"]} !important;
    }}

    /* ===== Plotly chart container ===== */
    .js-plotly-plot {{
        border-radius: 12px;
        overflow: hidden;
    }}

    /* ===== Smooth Animations ===== */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    .animate-in {{
        animation: fadeInUp 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }}

    /* ===== Status indicator pulse ===== */
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.5; }}
    }}

    .pulse {{
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }}

    /* ===== Tab styling ===== */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
    }}

    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        border-radius: 8px;
        color: {c["text_secondary"]};
        font-weight: 500;
        padding: 8px 16px;
    }}

    .stTabs [aria-selected="true"] {{
        background: {c["accent_primary"]}20;
        color: {c["accent_primary"]};
    }}

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
