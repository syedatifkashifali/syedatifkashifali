import datetime
import streamlit as st

d = st.date_input("When's your birthday", datetime.date(2000, 7, 6))
st.write('Your birthday is:', d)
