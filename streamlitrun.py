# pip install streamlit
# pip freeze -> requirements.txt
# pip install -r requirements.txt

import streamlit as st
from helpers.view import View

if __name__ == "__main__":
    st.image(r"C:\Users\USER\Dropbox\BOOTCAMP\workspace\1st_project\data\K-car_image.webp")
    view = View(":car: 중고차 매물 검색 및 FAQ :car:")

    
