import streamlit as st

with open("styles.css") as k:
    st.markdown(f"<style>{k.read()}</style>", unsafe_allow_html=True)

st.header("Power BI")


st.write("Raw sales data for a grocery selling company, which deals in several product categories and subcategories, spans the years 2015 to 2018 (four years). We have been tasked with creating a dashboard with all the essential information about their historical sales success.")

st.markdown('<iframe title="Grocery Sales" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiMGRlMGM1NWQtMWJmMC00YzJmLWFjNDEtZmRkMjUxNDkzY2FlIiwidCI6ImQwNjQ5MWQ4LTg5MjAtNDdmZS1iMmU4LTllMTY1ZTY3YzYxNCJ9" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)
