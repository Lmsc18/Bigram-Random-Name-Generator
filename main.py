from bigram import generate
import streamlit as st

st.title("Random Name Generator")

if st.button("Generate"):
    name=generate()
    st.text_area("Name Generated",name)