import streamlit as st

st.text_input("이름:")
st.text_input("학년:")

st.selectbox("this is just a question",["English or Spanish"])
st.selectbox("What do you want to get?",["carrot or candy blossom"])
st.selectbox("What game do you like?",["roblox or mincraft"])
st.selectbox("Who do you want?", ["idiot", "prodigy"])
st.selectbox("What game do you like?", ["grow-a-garden", "rivals"])

st.text_input("What is ypur MBTI?")
st.text_input("What is ypur pc password?")

st.subheader(" -Level 1- ")
st.number_input(" 1 + 1 = ?")
st.number_input("3 + 4 = ?")
st.number_input(" 6 + 2 = ?")
st.number_input(" 3 + 3 = ?")

st.subheader(" -level 2-")
st.number_input("12 - 7 = ?")
st.number_input("78 - 52 = ?")
st.number_input("63 - 42 = ?")
st.number_input("81 - 9 = ?")

st.subheader(" -level 3-")
st.number_input("8 x 9 = ?")
st.number_input("6 x 7 = ?")
st.number_input("2 x 5 = ?")
st.number_input("9 x 4 = ?")

st.subheader(" -level 4-")
st.number_input("72 % 8 = ?")
st.number_input("81 % 9 = ?")
st.number_input("54 % 9 = ?")
st.number_input("45 % 5 = ?")

st.subheader(" -level 5-")
st.number_input("1/4 + 5/8 = ?")
st.number_input("5/6 - 9/13 = ?")
st.number_input("6/7 * 2/7 = ?")
st.number_input("4/7 % 10/11 = ?")

st.subheader(" -level 6-")
st.number_input("0.1 % 4 = ?")
st.number_input("0.8 % 5 = ?")
st.number_input("0.12 % 3 = ?")
st.number_input("0.13 % 65 = ?")

st.subheader(" -level 7- ")
st.number_input("y = 2 + 5y = 2x + 53 x y = 73x - y=7x + y = 12x + y = 124x 2y 4x = 2y")


st.subheader(" ... you came so far... now is the time to stop solving correctly... muahaha..? ")
st.number_input("∫ 0∞​  sin_x/x​ dx = ?... ")