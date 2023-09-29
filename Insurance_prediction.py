import pickle
import streamlit as st


model = pickle.load(open('Insurance_prediction.sav','rb'))


st.title('Insurance Prediction')

age = st.number_input('Input your age',0)
sex = st.selectbox(
    'Your gender?',
    ('Male', 'Female'))
if sex == 'Male':
    sex = 1
else:
    sex = 0
bmi = st.number_input('Input your bmi',0)
children = st.number_input('How many children',0)
smoker = st.selectbox(
    'Are you smoker?',
    ('Yes', 'No'))
if smoker == 'Yes':
    smoker = 0
else:
    smoker = 1


predict = ''

if st.button('Prediction'):
    predict = model.predict(
        [[age,sex,bmi,children,smoker]]
    )
    st.write('The insurance prediction is ', predict)