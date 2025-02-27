# NEXT STEPS
# 1.  make model more accuret

import streamlit as st
import pandas as pd
import numpy as np
import requests as res
import json as js
from dbModels import Results
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from streamlit_drawable_canvas import st_canvas

if "img" not in st.session_state:
    st.session_state["img"] = []

if "num" not in st.session_state:
    st.session_state["num"] = ""
    
if "res" not in st.session_state:
    st.session_state["res"] = ""
    
if "responseCode" not in st.session_state: 
    st.session_state["responseCode"] = ""

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
    
def submitData():
    st.button("Predict Number",
      key="predict_number",
      on_click= sendRequst
      )
    
    st.write(f"Model output: {st.session_state.res}")     
            
def connectToDB():
    url = "postgresql://user:password@db:5432/user"
    engine = create_engine(url)
    return pd.read_sql("results", con=engine)

def sendRequst():
    
    payload = { "img": st.session_state.img, "num": st.session_state.num}  
    
    response = res.post("http://ai:8000/", json=payload)

    st.session_state["responseCode"] = response.status_code
    
    if st.session_state["responseCode"] == 200:
        
        resData = response.json()
        st.session_state["res"] = resData["output"]
        
        results_to_db(st.session_state.res, st.session_state.num)

def results_to_db(modleResult, userDefinedResult):
    engine = create_engine("postgresql://user:password@db/user")
    with Session(engine) as session:

        newRecord = Results(model_result=modleResult, use_defined_result=userDefinedResult)
        session.add_all([newRecord])
        session.commit()

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
    st.write(" ")
    st.write(" ")
    submitData()
    st.write(" ")
    st.write(" ")

st.write("Previous Model Results")
st.table(df.tail(5))
