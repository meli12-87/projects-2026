import streamlit as st
import utilshw

default_model = 'qwen2.5-coder:7b'
st.title(':llama: RUN AI OFFLINE MODELS')


if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("Ollama Offline ChatBot")

if st.button("Reset Memory"):
    st.session_state.messages = []
    st.rerun()

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

user_input = st.chat_input("Ask your question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    
    if user_input.lower() == "goodbye":
        st.chat_message("assistant").write("Goodbye")
        st.stop()
    
    fixed_response = None
    if "politics" in user_input.lower() or "political" in user_input.lower():
        fixed_response = "Fixed political response: I have no political opinion."
    elif "religion" in user_input.lower() or "religious" in user_input.lower():
        fixed_response = "Fixed religious response: Please ask another question."
    elif "war" in user_input.lower() or "conflict" in user_input.lower():
        fixed_response = "Fixed war response: I am against war."
    
    if fixed_response:
        st.session_state.messages.append({"role": "assistant", "content": fixed_response})
        st.chat_message("assistant").write(fixed_response)
    else:
        with st.spinner("Thinking..."):
            response = utilshw.call_ollama_model('qwen2.5-coder:7b', user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
    
    st.rerun()