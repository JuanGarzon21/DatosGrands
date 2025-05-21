import streamlit as st
import plotly.express as px

st.title("Mi segunda publicacion")
st.header("Introduccion")
st.write("Esta es la primera vez que me sale algo")

fig = px.bar(x=["A", "B", "C"], y=[4, 3, 8])
st.plotly_chart(fig)