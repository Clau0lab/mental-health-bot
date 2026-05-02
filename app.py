import streamlit as st
from huggingface_hub import InferenceClient
# 1. SETUP - Replace
HF_TOKEN = "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"
client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=HF_TOKEN)
st.title("Iris: My Mental Health ChatBot") 
st.write("Hello! I am Iris and I am here to listen.")

# 2. Create the input box for the user 
prompt = st.chat_input("How are you feeling today?")
if prompt:
    # Display the user's message
    with st.chat_message("user"): st.markdown(prompt)
# 3. IRIS BRAIN (Hugging Face)
with st.chat_message("assistant"):
    # We give the AI a "system message" to tell it hown to behave
    system_instructions = "You are Iris, a kind and empathetic mental health companion. Listen carefully and offer supportive, non-medical advice."
    #This sends your message to Hugging Face
    response = client.chat_completion(messages=[{"role": "system", "content": system_instructions},{"role": "user", "content": prompt}], max_tokens=500, stream=False)
iris_text = response.choices[0].message.content
st.markdown(iris_text)