import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

from streamlit_drawable_canvas import st_canvas

def drawNumber(payload):
    st.write("Draw a number")
    canvas_result = st_canvas(
                              "canvas",
                              update_streamlit=True,
                              width=250,
                              height=250
                              )
    payload["img"] = canvas_result.json_data

def insertNumber(payload):
        actualNumber = st.text_input("Actual Number", value="", key="predicted_number")
        payload["actualNumberb"] = actualNumber

def connectToDB():
    url = "postgresql://user:password@db:5432/user"
    engine = create_engine(url)
    return pd.read_sql("results", con=engine)



# ========= page layout =========

payload = {}

df = connectToDB()

st.set_page_config(page_title="MNST Modle", page_icon="🧊", layout="centered")

st.title("MNST Modle")
st.write("use the canvas to draw a number, then insert the actual number and click predict")

img, submit = st.columns(2)

with img:
    drawNumber(payload)

with submit:
    insertNumber(payload)

st.button("Predict Number", key="predict_number", help="Click to predict the number")

st.write("Modle Results")

st.table(df.tail(10))
