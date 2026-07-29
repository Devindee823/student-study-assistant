import streamlit as st

from agents.planner_agent import planner_agent
from agents.study_agent import study_agent
from agents.quiz_agent import quiz_agent


st.title("Student Study Assistant")

st.write("Welcome to my AI Study Assistant")


question = st.text_input("Ask your study question")


if question:
    st.write("You asked:", question)

    task = planner_agent(question)

    st.write("Task:", task)


    if task == "quiz":
        response = quiz_agent(question)

    else:
        response = study_agent(question)


    st.subheader("AI Response:")

    st.markdown(response)