import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np


def _get_chart_layout(title: str, is_dark: bool) -> dict:
    """Base layout config for all charts."""
    text_color = "#94a3b8" if is_dark else "#475569"
    grid_color = "rgba(148, 163, 184, 0.1)" if is_dark else "rgba(15, 23, 42, 0.08)"
    bg_color = "rgba(0,0,0,0)"

    return dict(
        title=dict(
            text=title,
            font=dict(size=16, color=text_color, family="Inter"),
            x=0.5,
            xanchor="center",
        ),
        font=dict(family="Inter", color=text_color),
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        margin=dict(l=40, r=40, t=60, b=40),
        xaxis=dict(gridcolor=grid_color, zerolinecolor=grid_color),
        yaxis=dict(gridcolor=grid_color, zerolinecolor=grid_color),
    )


def render_prediction_distribution(metrics: dict, is_dark: bool):
    """Chart 1: Prediction Distribution — Pie Chart."""

    attack_pct = metrics["attack_count"]
    normal_pct = metrics["normal_count"]

    colors = ["#ef4444", "#10b981"] if is_dark else ["#dc2626", "#059669"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Attack", "Normal"],
                values=[attack_pct, normal_pct],
                hole=0.55,
                marker=dict(
                    colors=colors,
                    line=dict(color="rgba(0,0,0,0.1)", width=2),
                ),
                textinfo="label+percent",
                textfont=dict(size=14, family="Inter", color="white"),
                hovertemplate="<b>%{label}</b><br>"
                + "Count: %{value}<br>"
                + "Percentage: %{percent}<extra></extra>",
                pull=[0.03, 0],
            )
        ]
    )

    layout = _get_chart_layout("Prediction Distribution", is_dark)
    layout["showlegend"] = True
    layout["legend"] = dict(
        orientation="h",
        yanchor="bottom",
        y=-0.15,
        xanchor="center",
        x=0.5,
        font=dict(size=12),
    )

    # Add center annotation
    fig.add_annotation(
        text=f"<b>{metrics['total_samples']}</b><br><span style='font-size:11px'>Samples</span>",
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(
            size=18,
            color="#6366f1" if is_dark else "#4f46e5",
            family="Inter",
        ),
    )

    fig.update_layout(**layout, height=380)
    st.plotly_chart(fig, use_container_width=True, key="chart_pie")


def render_confusion_matrix(metrics: dict, is_dark: bool):
    """Chart 2: Confusion Matrix — Heatmap."""

    z = [[metrics["tn"], metrics["fp"]], [metrics["fn"], metrics["tp"]]]

    labels_x = ["Predicted Normal", "Predicted Attack"]
    labels_y = ["Actual Normal", "Actual Attack"]

    # Annotation text
    text = [
        [f"TN<br><b>{metrics['tn']}</b>", f"FP<br><b>{metrics['fp']}</b>"],
        [f"FN<br><b>{metrics['fn']}</b>", f"TP<br><b>{metrics['tp']}</b>"],
    ]

    colorscale = [
        [0, "#1e1b4b" if is_dark else "#e0e7ff"],
        [0.5, "#4338ca" if is_dark else "#818cf8"],
        [1, "#6366f1" if is_dark else "#4f46e5"],
    ]

    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            x=labels_x,
            y=labels_y,
            colorscale=colorscale,
            showscale=True,
            colorbar=dict(
                title=dict(text="Count", font=dict(size=12)),
                tickfont=dict(size=10),
            ),
            hovertemplate="<b>%{y}</b> → %{x}<br>Count: %{z}<extra></extra>",
        )
    )

    # Add text annotations
    text_color = "white" if is_dark else "#1e1b4b"
    for i in range(2):
        for j in range(2):
            fig.add_annotation(
                x=labels_x[j],
                y=labels_y[i],
                text=text[i][j],
                showarrow=False,
                font=dict(size=14, color=text_color, family="Inter"),
            )

    layout = _get_chart_layout("Confusion Matrix", is_dark)
    fig.update_layout(**layout, height=380)
    fig.update_xaxes(side="bottom")
    st.plotly_chart(fig, use_container_width=True, key="chart_cm")


def render_class_recall(metrics: dict, is_dark: bool):
    """Chart 3: Class-wise Recall — Bar Chart."""

    categories = ["Attack Recall", "Normal Recall"]
    values = [metrics["attack_recall"], metrics["normal_recall"]]
    colors = ["#ef4444" if is_dark else "#dc2626", "#10b981" if is_dark else "#059669"]

    fig = go.Figure(
        data=[
            go.Bar(
                x=categories,
                y=values,
                marker=dict(
                    color=colors,
                    line=dict(width=0),
                ),
                text=[f"{v}%" for v in values],
                textposition="outside",
                textfont=dict(size=14, family="Inter"),
                hovertemplate="<b>%{x}</b><br>Recall: %{y}%<extra></extra>",
                width=0.5,
            )
        ]
    )

    layout = _get_chart_layout("Class-wise Recall", is_dark)
    layout["yaxis"] = dict(
        range=[0, 110],
        gridcolor="rgba(148, 163, 184, 0.1)" if is_dark else "rgba(15, 23, 42, 0.08)",
        zerolinecolor="rgba(148, 163, 184, 0.1)" if is_dark else "rgba(15, 23, 42, 0.08)",
        title="Recall (%)",
    )
    layout["xaxis"] = dict(title="")

    fig.update_layout(**layout, height=380, bargap=0.3)
    st.plotly_chart(fig, use_container_width=True, key="chart_recall")


def render_feature_importance(df, is_dark: bool):
    """Chart 4: Top Feature Statistics — Horizontal Bar Chart."""

    # Show standard deviation of key numeric features as a proxy for "importance"
    numeric_cols = [
        "duration", "src_bytes", "dst_bytes", "count", "srv_count",
        "dst_host_count", "dst_host_srv_count", "hot", "num_compromised", "num_root"
    ]
    available = [c for c in numeric_cols if c in df.columns]
    if not available:
        st.info("No numeric features available for analysis.")
        return

    # Compute mean absolute difference between attack and normal samples
    stats = {}
    for col in available:
        attack_mean = df[df["label"] == 1][col].mean()
        normal_mean = df[df["label"] == 0][col].mean()
        stats[col] = abs(attack_mean - normal_mean)

    sorted_features = sorted(stats.items(), key=lambda x: x[1], reverse=True)[:8]
    features = [f[0] for f in sorted_features]
    diffs = [round(f[1], 2) for f in sorted_features]

    fig = go.Figure(
        data=[
            go.Bar(
                y=features,
                x=diffs,
                orientation="h",
                marker=dict(
                    color=diffs,
                    colorscale=[[0, "#6366f1"], [0.5, "#8b5cf6"], [1, "#a78bfa"]],
                    line=dict(width=0),
                ),
                text=[f"{d:.1f}" for d in diffs],
                textposition="outside",
                textfont=dict(size=11, family="Inter"),
                hovertemplate="<b>%{y}</b><br>Mean Diff: %{x:.2f}<extra></extra>",
            )
        ]
    )

    layout = _get_chart_layout("Feature Discrimination (Attack vs Normal)", is_dark)
    layout["yaxis"]["autorange"] = "reversed"
    layout["xaxis"]["title"] = "Mean Absolute Difference"
    fig.update_layout(**layout, height=380)
    st.plotly_chart(fig, use_container_width=True, key="chart_features")


def render_all_charts(metrics: dict, df, is_dark: bool):
    """Render all charts in a clean layout."""

    st.markdown(
        '<div class="section-header">📊 Analysis & Visualization</div>',
        unsafe_allow_html=True,
    )

    # Row 1: Prediction Distribution (full width)
    render_prediction_distribution(metrics, is_dark)

    # Row 2: Class-wise Recall + Feature Importance
    col1, col2 = st.columns(2)
    with col1:
        render_class_recall(metrics, is_dark)
    with col2:
        render_feature_importance(df, is_dark)
