import streamlit as st
import pandas as pd
import numpy as np

from streamlit_drawable_canvas import st_canvas

payload= {}

img, submit = st.columns(2)

with img:
    st.write("Draw a number")
    canvas_result = st_canvas(
                              update_streamlit=True,
                              width=250,
                              height=250
                              )
    payload["img"] = canvas_result.json_data

with submit:
    st.write("Submit the number")
    actualNumber = st.text_input("Actual Number", value="None", key="predicted_number")
    payload["actualNumberb"] = actualNumber


st.button("Predict Number", key="predict_number", help="Click to predict the number")


st.write("Modle Results")
st.table(pd.DataFrame())