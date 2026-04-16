import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from utils import load_data, summary_table, top_regions, run_anova, daily_average

# ── Page configuration ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="Solar Farm Analysis | MoonLight Energy",
    page_icon="☀️",
    layout="wide",
)

# ── Title ────────────────────────────────────────────────────────────────────
st.title("☀️ Solar Farm Potential Dashboard")
st.markdown(
    "**MoonLight Energy Solutions** — Cross-country solar data explorer "
    "for Benin, Sierra Leone, and Togo."
)
st.divider()

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("🔧 Controls")

    selected_countries = st.multiselect(
        "Select Countries",
        options=["Benin", "Sierra Leone", "Togo"],
        default=["Benin", "Sierra Leone", "Togo"],
    )

    selected_metric = st.selectbox(
        "Solar Metric",
        options=["GHI", "DNI", "DHI"],
        index=0,
    )

    sample_size = st.slider(
        "Scatter sample size",
        min_value=500,
        max_value=5000,
        value=1500,
        step=500,
    )

    st.info("Data files are read locally from the `data/` folder.")

# ── Guard: require at least one country ──────────────────────────────────────
if not selected_countries:
    st.warning("Please select at least one country from the sidebar.")
    st.stop()

# ── Load data ────────────────────────────────────────────────────────────────
with st.spinner("Loading data…"):
    df = load_data(selected_countries)

st.success(f"Loaded **{len(df):,}** records from {len(selected_countries)} country(ies).")
st.divider()

# ── Tab layout ───────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(
    ["📊 Summary", "📦 Boxplot", "📈 Time Series", "🏆 Rankings"]
)

# ── Tab 1: Summary Table ─────────────────────────────────────────────────────
with tab1:
    st.subheader("Summary Statistics — Mean / Median / Std")
    metrics = ["GHI", "DNI", "DHI"]
    table = summary_table(df, metrics)
    st.dataframe(table, use_container_width=True)

    st.divider()
    st.subheader(f"ANOVA Test on {selected_metric}")
    anova = run_anova(df, selected_metric)
    col1, col2 = st.columns(2)
    col1.metric("F-Statistic", anova["f_stat"])
    col2.metric("p-value", f"{anova['p_value']:.6f}")
    if anova["p_value"] < 0.05:
        st.success(
            "✅ Differences are **statistically significant** (p < 0.05). "
            "Country choice matters for solar investment."
        )
    else:
        st.info("ℹ️ Differences are **not statistically significant** at p < 0.05.")

# ── Tab 2: Boxplot ───────────────────────────────────────────────────────────
with tab2:
    st.subheader(f"Distribution of {selected_metric} by Country")

    colors = {"Benin": "#1f77b4", "Sierra Leone": "#ff7f0e", "Togo": "#2ca02c"}
    palette = {c: colors[c] for c in selected_countries if c in colors}

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(
        data=df,
        x="Country",
        y=selected_metric,
        hue="Country",
        palette=palette,
        legend=False,
        width=0.5,
        ax=ax,
    )
    ax.set_title(f"{selected_metric} Distribution by Country", fontsize=14)
    ax.set_ylabel(f"{selected_metric} (W/m²)")
    ax.set_xlabel("")
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)
    plt.close(fig)

# ── Tab 3: Time Series ───────────────────────────────────────────────────────
with tab3:
    st.subheader(f"Daily Average {selected_metric} Over Time")

    daily = daily_average(df, selected_metric)
    
    # Pivot the data so countries are columns for st.line_chart
    chart_data = daily.pivot(index="Timestamp", columns="Country", values=selected_metric)
    
    st.line_chart(chart_data)
    st.info("💡 Pro Tip: Hover over the chart to see values, or use the legend to toggle countries.")

# ── Tab 4: Rankings ──────────────────────────────────────────────────────────
with tab4:
    st.subheader(f"Countries Ranked by Average {selected_metric}")

    ranking = top_regions(df, metric=selected_metric, top_n=len(selected_countries))
    st.dataframe(ranking, use_container_width=True)

    # Bar chart
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        ranking["Country"],
        ranking[f"Average {selected_metric} (W/m²)"],
        color=[colors.get(c, "grey") for c in ranking["Country"]],
        edgecolor="black",
        width=0.5,
    )
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{bar.get_height():.1f}",
            ha="center",
            va="bottom",
            fontsize=12,
        )
    ax.set_title(f"Countries Ranked by Average {selected_metric}")
    ax.set_ylabel(f"Average {selected_metric} (W/m²)")
    ax.grid(True, alpha=0.3, axis="y")
    st.pyplot(fig)
    plt.close(fig)

# ── Footer ───────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built with Streamlit · MoonLight Energy Solutions · 10 Academy Week 0")
