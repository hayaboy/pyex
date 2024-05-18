
import openai
import streamlit as st

st.title('인공지능 시인')

content=st.text_input("당신이 원하는 시의 주제는 무엇입니까?")
# content = "봄비"

messages = [
    {"role": "system", "content": "노벨 문학상을 맏은 시인 AI입니다. 저와 대화합니다."},
    {"role": "user", "content": content+"에 대한 시를 써줘"},
]


# print(response["choices"][0]["message"]["content"])

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages,temperature=0)
        st.write(result["choices"][0]["message"]["content"])