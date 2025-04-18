import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st




# Set page config
st.set_page_config(
    page_title="Exploraa",
    layout="centered"
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Header
st.markdown("<h1 style='text-align: center;'>EDA Visualizer App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Learn Exploratory Data Analysis Visually</h3>", unsafe_allow_html=True)

st.markdown("---")



# Introduction
st.markdown("""
### 👋 Welcome!

This app helps you visually analyze your clean dataset using different types of exploratory data analysis (EDA) tools.

Whether you're a student or a data science enthusiast, this app will help you:
- ✅ Understand the **types of columns**: numerical vs categorical
- 📊 Choose the **right kind of charts** for each column
- 🧠 Learn which plots work best for **univariate**, **bivariate**, and **multivariate** analysis

---
### 🚀 How to Get Started:
1. Go to the **Visual Analysis** page from the sidebar
2. Select your numerical and categorical columns
3. Choose the analysis type (Univariate, Bivariate, Multivariate)
4. Pick the chart and start exploring!

---
### 📚 Key Features:
- Only shows valid chart types for your selected columns
- Helpful feedback when selection is invalid
- Powered by **Streamlit + Plotly + Seaborn**
""")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Built with ❤️ for learners & data explorers</p>", unsafe_allow_html=True)

import streamlit as st

# Author description with a LinkedIn link
author_description = """
### Author: Shivam Kajale

This project was created by **Shivam Kajale**. You can connect with me on [LinkedIn](https://www.linkedin.com/in/shivamkajale/).

Feel free to reach out for collaboration or any questions related to this project.
"""

# Display the author description
st.markdown(author_description)
