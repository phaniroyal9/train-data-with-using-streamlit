import streamlit as st
import numpy as np
import pickle
from pickle import load
pickle_in =open('arsh.pkl', 'rb')
classifier = load(pickle_in)


# from sklearn.linear_model import LogisticRegression

st.markdown('<style>body{background-color: black;}</style>',unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'> OUTPUT OF TRAIN DATA</h1>", unsafe_allow_html=True)

# the data which the user inputs
def main():

    st.title('HEROKU DEPLOYMENT')
    col1 = st.number_input('enter a value')
    col2 = st.number_input('enter another value')
    prediction = classifier.predict([[col1,col2]])
    output = st.button('SUBMIT')
    if output:
        if prediction == 1:
            st.write('output : 01 :smile:')
        else:
            st.write('output : 00 :cry:')

if __name__ == '__main__':
    main()

# def prediction(col1,col2):
#     prediction = classifier.predict([[col1,col2]])
#     if prediction == 1:
#         pred = "Yes"
#     else:
#         pred = "No"
#     return pred
#
#
# def main():
#     st.title('HEROKU DEPLOYMENT')
#     col1 = st.number_input('enter a value')
#     col2 = st.number_input('enter another value')
#     if st.button('Predict'):
#         output=prediction(col1,col2)
#         st.info(output)
