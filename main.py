import streamlit as st
from PIL import Image
import read_data

st.write("# EKG APP")

st.write("## Versuchsperson auswählen")

if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'


person_data = read_data.load_person_data()
person_list = read_data.get_person_list(person_data)

st.session_state.current_user = st.selectbox('Versuchsperson', options=person_list, key="sbVersuchsperson")

person_dict = read_data.find_person_data_by_name(person_data, st.session_state.current_user)
if person_dict is None:
    picture_path = 'data/pictures/none.jpg'
else:
    picture_path = person_dict["picture_path"]

st.write(f"The selected user: {st.session_state.current_user}")

# Laden eines Bilds
image = Image.open(picture_path)
# Anzeigen eines Bilds mit Caption
st.image(image, caption=st.session_state.current_user)

#Die Reihenfolge ist wichtig