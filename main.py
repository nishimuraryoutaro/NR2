import streamlit as st
import time
st.title('NR1')

st.write('DataFrame')

st.write('プレグレスパーの表示')

bar = st.progress(0)

for i in range(100):
    bar.progress(i + 1)
    time.sleep(0.1)