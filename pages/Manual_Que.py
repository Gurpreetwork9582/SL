import streamlit as st
import pandas as pd


st.title("Create Quiz Question")

# User inputs
question_text = st.text_input("Enter Question")
option_a = st.text_input("Option A")
option_b = st.text_input("Option B")
option_c = st.text_input("Option C")
option_d = st.text_input("Option D")

answer = st.selectbox(
    "Correct Answer",
    ["A", "B", "C", "D"]
)

if st.button("Save Question"):
    question = pd.DataFrame([{
        "question": question_text,
        "option A": option_a,
        "option B": option_b,
        "option C": option_c,
        "option D": option_d,
        "answer": answer }])
    st.success("Question saved!")
    st.write(question)
    