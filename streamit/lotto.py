import streamlit as st
import random
import datetime

st.title("로또")

# 1~45, 6자리

def lotto():
    lot = set() # 로또는 중복이 없음
    while len(lot) < 6:
        numb = random.randint(1,46) # 1~45숫자
        lot.add(numb)
    lot = list(lot)
    lot.sort()
    return lot

button = st.button("번호생성")
if button:
    for i in range(0,6):
        st.subheader(f"{lotto()}") # 함수 자체를 넣을수 있다 ?
    st.write("당첨번호")

# confetti effect (종이조각)
from streamlit.components.v1 import html # 외부모듈 쓸거면 이렇게

# define your javascript
#
my_js = """
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/confetti@3.0.3/tsparticles.confetti.bundle.min.js"></script>
<script>
const defaults = {
  spread: 360,
  ticks: 100,
  gravity: 0,
  decay: 0.94,
  startVelocity: 30,
  shapes: ["heart"],
  colors: ["FFC0CB", "FF69B4", "FF1493", "C71585"],
};

confetti({
  ...defaults,
  particleCount: 50,
  scalar: 2,
});

confetti({
  ...defaults,
  particleCount: 25,
  scalar: 3,
});

confetti({
  ...defaults,
  particleCount: 10,
  scalar: 4,
});
</script>
""" # 알림창 뜸

# wrap the javascript as html code
my_html = f"{my_js}" # my_js 내용으로 script에 삽입

# excute your app
st.title("Javascript example")
html(my_html) # 해당사항 html에 적용!