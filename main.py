import streamlit as st
st.title('나의 첫 스트림릿 프로젝트!!')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 동물을 선택해주세요:', ['강아지','고양이'])
if st.button('인사말 생성') : 
  st.write(name+'님! 당신이 좋아하는 동물은 '+menu+'이군요?! 저도 좋아요!!')
