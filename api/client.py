import requests
import streamlit as st

def get_essay_response(topic):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {"topic": topic}}
    )
    return response.json()["output"]

def get_poem_response(topic):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input": {"topic": topic}}
    )
    return response.json()["output"]

# Streamlit UI
st.title("LangChain Demo with LLaMA2 (Ollama)")

essay_topic = st.text_input("Write an essay on")
poem_topic = st.text_input("Write a poem on")

if essay_topic:
    st.subheader("Essay Output")
    st.write(get_essay_response(essay_topic))

if poem_topic:
    st.subheader("Poem Output")
    st.write(get_poem_response(poem_topic))
