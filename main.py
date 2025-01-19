import streamlit as st

name = st.text_input("Enter your name: ")
fname = st.text_input("Enter your father name: ")
adr = st.text_area("Enter your address: ")
classdata = st.selectbox("Enter your class: ",(1,2,3,4,5))

button = st.button("Done")
if button:
    st.markdown(f"""
        Name: {name}
        Father Name : {fname}
        address : {adr}
        class : {classdata}
    """)