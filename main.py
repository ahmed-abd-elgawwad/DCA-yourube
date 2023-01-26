import streamlit as st
import pandas as pd
from dca_oop import  ARPS
# title
st.write("# DCA `ARP's model`")

# sidebar seciton
st.sidebar.write("# User Inputs")
file = st.sidebar.file_uploader("Upload file",type=["csv"])
if file:
    try:
        df = pd.read_csv(file)
        cols = list(df.columns)
        production_col = st.sidebar.selectbox("production column",cols)
        date_col = st.sidebar.selectbox("date column",cols)
        freq = st.sidebar.selectbox("date frequency",[ "Daily" , "Monthly" , "Yearly" ])

        # smoothing the data
        arps = ARPS(df,production_col,date_col)
        st.write("#### Smooting the data `Moving Average` ")
        window_size = st.slider("Window size in MA",min_value=10,max_value=500,step=10)
        arps.smooth(window_size,3,True)
        d = arps.prepocess_date_col(freq)
        st.line_chart(d[[production_col,production_col+"_rol_Av"]])

        # fitting the data
        st.write("### Fitting data `All ARP's models`")
        params, data  = arps.fit_all_models()
        st.line_chart(data)
        st.write(params)
    except:
        st.error("make sure you entered the data right")




