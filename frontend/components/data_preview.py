import streamlit as st
import pandas as pd


def render_data_preview(df: pd.DataFrame):
    """Render the data preview section showing sampled rows."""

    st.markdown(
        '<div class="section-header">🔎 Data Preview — Sampled Rows</div>',
        unsafe_allow_html=True,
    )

    # Select key columns to display
    display_cols = [
        "duration", "protocol_type", "service", "flag",
        "src_bytes", "dst_bytes", "count", "srv_count",
        "true_label", "prediction_label",
    ]
    available_cols = [c for c in display_cols if c in df.columns]

    display_df = df[available_cols].copy()

    # Rename for readability
    rename_map = {
        "true_label": "Actual",
        "prediction_label": "Predicted",
        "src_bytes": "Src Bytes",
        "dst_bytes": "Dst Bytes",
        "protocol_type": "Protocol",
        "srv_count": "Srv Count",
    }
    display_df = display_df.rename(columns={k: v for k, v in rename_map.items() if k in display_df.columns})

    # Summary row
    total = len(df)
    attacks = (df["prediction"] == 1).sum()
    normals = (df["prediction"] == 0).sum()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption(f"📋 Showing {min(50, total)} of {total} sampled rows")
    with col2:
        st.caption(f"🔴 Attacks: {attacks}")
    with col3:
        st.caption(f"🟢 Normal: {normals}")

    # Color the dataframe
    def highlight_predictions(row):
        if "Predicted" in row.index:
            color = (
                "background-color: rgba(239, 68, 68, 0.15)"
                if row["Predicted"] == "Attack"
                else "background-color: rgba(16, 185, 129, 0.15)"
            )
            return [color] * len(row)
        return [""] * len(row)

    styled = display_df.head(50).style.apply(highlight_predictions, axis=1)
    st.dataframe(
        styled,
        use_container_width=True,
        height=400,
    )
