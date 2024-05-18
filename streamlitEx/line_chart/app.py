import streamlit as st
import pandas as pd
import numpy as np
# 타 이 틀 설 정
st.title('My first Streamlit app')
# 데 이 터 생 성
data = pd.DataFrame(
np.random.randn(50, 3),
columns=['a', 'b', 'c'])
# 데 이 터 표 시
st.write("Here's our first attempt at using data to create a table:")
st.write(data)
# 차 트 그 리 기
st.line_chart(data)