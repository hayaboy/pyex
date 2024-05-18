import streamlit as st
import pandas as pd
import altair as alt

# 데이터 설정
years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
registrations = [2012, 2099, 2180, 2253, 2320, 2368, 2437, 2491, 2550, 2595]

# 데이터프레임 생성
data = pd.DataFrame({
    'Year': years,
    'Registrations': registrations
})

# Streamlit 앱 제목
st.title('자동차 등록 대수 시각화')

# 세로막대그래프 생성
bar_chart = alt.Chart(data).mark_bar().encode(
    x='Year',
    y='Registrations'
).properties(
    title='연도별 자동차 등록 대수 (세로막대그래프)'
)

# 꺾은선형 그래프 생성
line_chart = alt.Chart(data).mark_line(point=True).encode(
    x='Year',
    y='Registrations'
).properties(
    title='연도별 자동차 등록 대수 (꺾은선형 그래프)'
)

# 그래프 표시
st.altair_chart(bar_chart, use_container_width=True)
st.altair_chart(line_chart, use_container_width=True)