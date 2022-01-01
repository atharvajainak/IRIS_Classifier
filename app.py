import streamlit as st
import joblib

st.title("Iris Classifier")

model = joblib.load('IRIS_Classifier')

sl = st.slider('Sepal Length', 1.0, 7.9, 6.4)
sw = st.slider('Sepal Width', 0.5, 4.4, 2.8)
pl = st.slider('Petal Length', 0.5, 6.9, 5.6)
pw = st.slider('Petal Width', 0.1,2.5, 2.1)

op = model.predict([[sl,sw,pl,pw]])
st.title(op[0])