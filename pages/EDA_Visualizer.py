import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Exploraa", layout="wide",page_icon="images\Exploraatory-analysis.png")

# --- Sidebar Upload ---
st.sidebar.title("📂 Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel file", type=['csv', 'xlsx'])

@st.cache_data
def load_data(file):
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        return pd.read_excel(file)

if uploaded_file:
    df = load_data(uploaded_file)
    st.sidebar.success("✅ Data loaded successfully!")

    # --- Tab Layout ---
    tab1, tab2, tab3 = st.tabs(["📄 Overview", "📊 Visual Analysis", "🧪 Advanced"])

    # ----------------------------
    # 📄 Tab 1: Overview
    # ----------------------------
    with tab1:
        st.header("🔍 Dataset Overview")

        st.subheader("First 5 Rows")
        st.dataframe(df.head())

        st.subheader("Data Info")
        buffer = df.info(buf=None)
        st.text(str(df.info(verbose=True)))

        st.subheader("Descriptive Statistics")
        st.dataframe(df.describe(include='all').T)

        st.subheader("Column Summaries")
        for col in df.columns:
            st.markdown(f"**🧠 {col}**")
            col_data = df[col]
            st.write("Type:", col_data.dtype)
            st.write("Nulls:", col_data.isnull().sum())
            st.write("Unique:", col_data.nunique())
            if col_data.dtype == 'object' or col_data.nunique() < 20:
                st.write("Top values:", col_data.value_counts().head())
            st.markdown("---")
# ----------------------------
# 📊 Tab 2: Visual Analysis
# ----------------------------
    with tab2:
        st.header("📊 Visual Analysis")
        default_num = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        default_cat = df.select_dtypes(include=['object', 'category']).columns.tolist()

        numeric_cols = st.sidebar.multiselect("Numerical Columns", df.columns, default=default_num)
        cat_cols = st.sidebar.multiselect("Categorical Columns", df.columns, default=default_cat)

        analysis_type = st.selectbox("Select Analysis Type", ["Univariate", "Bivariate", "Multivariate"])

        if analysis_type == "Univariate":
            col = st.selectbox("Select a column", df.columns)

            if col in numeric_cols:
                chart_type = st.selectbox("Chart Type", ["Histogram", "KDE Plot", "Boxplot"])
                st.info("✅ This is a numerical column. Use Histogram, KDE Plot, or Boxplot.")

                if chart_type == "Histogram":
                    fig = px.histogram(df, x=col)
                elif chart_type == "KDE Plot":
                    fig = px.density_contour(df, x=col)
                elif chart_type == "Boxplot":
                    fig = px.box(df, y=col)

                st.subheader(f"{chart_type} of {col}")
                st.plotly_chart(fig, use_container_width=True)

            elif col in cat_cols:
                chart_type = st.selectbox("Chart Type", ["Barplot", "Pie Chart"])
                st.info("✅ This is a categorical column. Use Barplot or Pie Chart.")

                if chart_type == "Barplot":
                    value_counts_df = df[col].value_counts().reset_index()
                    value_counts_df.columns = [col, 'count']
                    fig = px.bar(value_counts_df, x=col, y='count')

                elif chart_type == "Pie Chart":
                    fig = px.pie(df, names=col)

                st.subheader(f"{chart_type} of {col}")
                st.plotly_chart(fig, use_container_width=True)

            else:
                st.warning("❌ Please select a valid numerical or categorical column.")

        elif analysis_type == "Bivariate":
            chart_type = st.selectbox("Graph type", ["Scatter", "Boxplot", "Lineplot", "BarPlot"])

            if chart_type == "Scatter" or chart_type == "Lineplot":
                x = st.selectbox("X-axis", numeric_cols, key='x_num')
                y = st.selectbox("Y-axis", [col for col in numeric_cols if col != x], key='y_num')

                if x and y:
                    st.info("✅ Both columns are numerical. Scatter and Line plots are suitable.")

                    st.subheader(f"{chart_type} Plot: {x} vs {y}")
                    if chart_type == "Scatter":
                        fig = px.scatter(df, x=x, y=y)
                    else:
                        fig = px.line(df, x=x, y=y)
                    st.plotly_chart(fig)

                else:
                    st.warning("❌ Please select two numerical columns.")

            elif chart_type == "Boxplot":
                x = st.selectbox("Categorical (X-axis)", cat_cols, key='x_cat')
                y = st.selectbox("Numerical (Y-axis)", numeric_cols, key='y_cat')

                if x and y:
                    st.info("✅ Categorical vs Numerical. Boxplot is appropriate.")
                    st.subheader(f"Boxplot of {y} by {x}")
                    fig = px.box(df, x=x, y=y)
                    st.plotly_chart(fig)
                else:
                    st.warning("❌ Please select a categorical column and a numerical column.")

            elif chart_type == "BarPlot":
                x = st.selectbox("X-axis (Categorical)", cat_cols, key='x_bar')
                y = st.selectbox("Y-axis (Numerical)", [col for col in numeric_cols if col != x], key='y_bar')

                if x and y:
                    st.info("✅ Bar plots are good for categorical vs numerical.")
                    st.subheader(f"Bar Plot: {x} vs {y}")
                    fig = px.bar(df, x=x, y=y)
                    st.plotly_chart(fig)
                else:
                    st.warning("❌ Please select a categorical and a numerical column.")

        elif analysis_type == "Multivariate":
            st.subheader("📌 Correlation Heatmap (Numerical Features Only)")

            if numeric_cols and len(numeric_cols) >= 2:
                st.info("✅ Correlation heatmap shows relationships between numerical features.")
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
                st.pyplot(fig)
            else:
                st.warning("❌ Please select at least two numerical columns for correlation heatmap.")


        # ----------------------------
        # 🧪 Tab 3: Advanced
        # ----------------------------
        with tab3:
            st.header("🧪 Advanced Features")
            st.write("🚧 Features like profiling, export, ML will be added here soon...")

else:
    st.title("📊 Exploratory Data Analysis")
    st.markdown("Upload your dataset from the sidebar to begin your data Exploration.")
    st.info("Accepted formats: CSV or Excel")
    st.image('images\download.gif',use_container_width=True)

