# pip install streamlit
# pip freeze -> requirements.txt
# pip install -r requirements.txt

import streamlit as st
from helpers.view import View
import os

if __name__ == "__main__":
    st.image(
        os.getcwd()+"\\data\\K-car_image.webp"
    )
    view = View(":car: K-car 중고차 :car:")
