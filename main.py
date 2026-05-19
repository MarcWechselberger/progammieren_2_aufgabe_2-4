import streamlit as st
import read_data

st.write("# EKG APP")

st.write("## Versuchsperson auswählen")

person_data = read_data.load_person_data()
person_list = read_data.get_person_list(person_data)

current_user = st.selectbox('Versuchsperson', options=person_list, key="sbVersuchsperson")

st.write(f"The selected user: {current_user}")
