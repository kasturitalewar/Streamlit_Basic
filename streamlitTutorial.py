import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello GPT")
name=st.text_input("Ask your questions:")
st.write("This is your first Streamlit app")
st.text("lets get started")
name=st.text_input("Enter your name:")
if st.button("Greet"):
    st.success(f"Hello {name}")

#How to upload any csv file:
upload_file = st.file_uploader("upload a csv",type='csv')
if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)

st.header("This is header")
st.subheader("This is a subheader")
st.markdown("[Link](https://streamlit.io/)")
st.text_area("write your message")
st.number_input("pick a number", min_value=0, max_value=10)
st.slider("choose a range",0,100)
st.selectbox("select a fruit",["apple","mango","banana",])
st.multiselect("select language",["java","python","c","c++"])
st.radio("pick one",["Option A","Option B"])
st.checkbox("I agree with terms and conditions")

if st.checkbox("show details"):
    st.info("here are more details")

# form tag
with st.form("login form"):
    username=st.text_input("enter username")
    password=st.text_input("password",type="password")
    submitted=st.form_submit_button("Login")

    if submitted:
        st.success(f"Welcome {username}")

df=pd.DataFrame(np.random.rand(20,3),columns=["A","B","C"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
st.video("https://youtu.be/cevGjmYyI3w?si=Zg65Nz9IuPKbEZSc")
st.image("https://kommodo.ai/i/fFEv2VYevtyqIMGOnq8n",caption="sample image")



