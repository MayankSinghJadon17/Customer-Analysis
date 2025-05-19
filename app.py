import streamlit as st
from streamlit_option_menu import option_menu
from pages import page1, page2, page3

st.set_page_config(page_title="Customer Pesonality Analysis", layout="wide")

# for sidebar thing
with st.sidebar:
    selected = option_menu(
        menu_title="Get Info",
        options=["Home", "Analytics", "Clustering"],
        icons=["house", "bar-chart", "diagram-3"],
        menu_icon="cast",
        default_index=0
    )

# page navigations
if selected == "Home":
    page1.show()
elif selected == "Analytics":
    page2.show()
elif selected == "Clustering":
    page3.show()
