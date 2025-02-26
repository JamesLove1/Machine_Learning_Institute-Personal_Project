import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import requests as res
import json as js

from streamlit_drawable_canvas import st_canvas

if "img" not in st.session_state:
    st.session_state["img"] = []

if "num" not in st.session_state:
    st.session_state["num"] = None
    
if "res" not in st.session_state:
    st.session_state["res"] = None
    
if "responseCode" not in st.session_state: 
    st.session_state["responseCode"] = None

def drawNumber():
    st.write("Draw a number")
    canvas_result = st_canvas(
                              "canvas",
                              update_streamlit=True,
                              width=250,
                              height=250
                              )
    if canvas_result.image_data is not None:
        st.session_state["img"] = canvas_result.image_data.tolist()
    
def insertNumber():
        actualNumber = st.text_input("Actual Number", value="", key="predicted_number")  
        st.session_state["num"] = actualNumber
        

def connectToDB():
    url = "postgresql://user:password@db:5432/user"
    engine = create_engine(url)
    return pd.read_sql("results", con=engine)



# ========= page layout =========

df = connectToDB()

st.set_page_config(page_title="MNST Modle", page_icon="🧊", layout="centered")

st.title("MNST Modle")
st.write("use the canvas to draw a number, then insert the actual number and click predict")

img, submit = st.columns(2)

with img:
    drawNumber()

with submit:
    insertNumber()


def sendRequst():
    
    payload = { "img": st.session_state.img, "num": st.session_state.num}  
    
    response = res.post("http://ai:8000/", json=payload)

    st.session_state["responseCode"] = response.status_code
    
    if st.session_state["responseCode"] == 200:
        
        resData = response.json()
        st.session_state["res"] = resData["output"]
    
st.button("Predict Number",
          key="predict_number",
          on_click= sendRequst
          )

st.write(f"output: from model: {st.session_state.res}")

st.write("Model Results")
st.table(df.tail(5))
