import streamlit as st
from Y_Plus_Calculator import y_plus_calculator_page

def main():
    st.title("Welcome to JUNJIN LAB")

    # ==============     You can Delete       ============== #
    # 우리들의 서사...
    st.markdown(
        """
        <div style="text-align: center; font-size: 24px; font-weight: bold;">
            Introduction
        </div>
        """,
        unsafe_allow_html=True
    )
    file_path = "./story.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    st.write(content)
    # 아하...
    # ======================================================== #


    page_options = ["Home", "Y+ Calculator"]
    selected_page = st.sidebar.selectbox("Select Page", page_options)

    if selected_page == "Home":
        st.write("\n\n\nWelcome to the Home Page!")
        st.write("\n\n\nShout out to YJ Kim!!!😂😂😂😂😂")
    elif selected_page == "Y+ Calculator":
        y_plus_calculator_page()

if __name__ == "__main__":
    main()

