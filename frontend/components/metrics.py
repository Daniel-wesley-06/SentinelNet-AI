import streamlit as st


def render_metrics(metrics: dict):
    """
    Render the KPI metric cards in a row:
    Accuracy, Attack Recall, Normal Recall.
    """

    st.markdown(
        '<div class="section-header">📈 Ensemble Model Performance</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="🎯 Accuracy",
            value=f"{metrics['accuracy']}%",
            delta=f"{metrics['total_samples']} samples",
            delta_color="off",
        )

    with col2:
        st.metric(
            label="🔴 Attack Recall",
            value=f"{metrics['attack_recall']}%",
            delta=f"{metrics['attack_count']} attacks detected",
            delta_color="off",
        )

    with col3:
        st.metric(
            label="🟢 Normal Recall",
            value=f"{metrics['normal_recall']}%",
            delta=f"{metrics['normal_count']} normal classified",
            delta_color="off",
        )

    with col4:
        precision = (
            metrics["tp"] / (metrics["tp"] + metrics["fp"]) * 100
            if (metrics["tp"] + metrics["fp"]) > 0
            else 0
        )
        st.metric(
            label="⚡ Precision",
            value=f"{precision:.1f}%",
            delta=f"TP: {metrics['tp']} | FP: {metrics['fp']}",
            delta_color="off",
        )
