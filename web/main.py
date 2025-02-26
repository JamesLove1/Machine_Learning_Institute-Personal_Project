import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import requests as res
import json as js

from streamlit_drawable_canvas import st_canvas

state = st.session_state
state.img = []
state.num = None

def drawNumber():
    st.write("Draw a number")
    canvas_result = st_canvas(
                              "canvas",
                              update_streamlit=True,
                              width=250,
                              height=250
                              )
    if canvas_result.image_data is not None:
        state.img = canvas_result.image_data.tolist()
    
def insertNumber():
        actualNumber = st.text_input("Actual Number", value="", key="predicted_number")  
        state.num = actualNumber
        

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
    
    payload = {"img": state.img, "num": state.num} # 
    
    res.post("http://ai:8000/", json=payload)

st.button("Predict Number",
          key="predict_number",
          help="Click to predict the number",
          on_click= sendRequst
          )

st.write("Model Results")
st.table(df.tail(5))
