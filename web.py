import streamlit as st
from main import summarize_text


st.title("Summarize and Quiz Your Text")
st.write("This app allows you to summarize a text and then quiz yourself on the summary.")

user_text = st.text_input("Enter your text here:", key="text_input")

if user_text:
    summary = summarize_text(user_text)  
    st.write("### Summary")
    st.write(summary[0]['summary_text'])

st.write("### Quiz Section")
if st.button("Create Quiz"):
    num_questions = st.number_input("How many questions do you want to create?", min_value=1, max_value=10, value=3, step=1)
    
    for i in range(num_questions):
        question = st.text_input(f"Enter question {i+1}:", key=f"question_{i}")
        answer = st.text_input(f"Enter the answer for question {i+1}:", key=f"answer_{i}")
        if question and answer:
            questions[question] = answer
    
    st.write("\nQuiz Created Successfully!\n")
    start = st.button("Start Quiz") 
    if start:
        score = 0
        for question, answer in questions.items():
            user_answer = st.text_input(f"{question} ", key=f"quiz_{question}")
            if user_answer.strip().lower() == answer.strip().lower():
                st.write("Correct!")
                score += 1
            else:
                st.write(f"Wrong! The correct answer is: {answer}")
        
        st.write(f"\nYour final score is: {score}/{num_questions}")
