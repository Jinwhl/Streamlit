import streamlit as st
from Y_Plus_Calculator import y_plus_calculator_page

def main():
    st.title("Welcome to JUNJIN LAB")

    page_options = ["Home", "Y+ Calculator"]
    selected_page = st.sidebar.selectbox("Select Page", page_options)

    if selected_page == "Home":
        st.write("Welcome to the Home Page!")
    elif selected_page == "Y+ Calculator":
        y_plus_calculator_page()

if __name__ == "__main__":
    main()
