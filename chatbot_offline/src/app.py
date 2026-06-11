import streamlit as st
import utils

model = 'qwen2.5-coder:7b'

st.title('OFFLINE CHATBOT PROJECT')
st.caption(':llama: you can ask your question offline')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role':'assistant',
                         'content':'How Can I Help U?'}]

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

prompt = st.chat_input('Enter Your question')
if prompt:

    st.chat_message('user').write(prompt)
    if 'password' in prompt:
        st.chat_message('ai').write('i can not answer to this question type')
    
    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role':'user',
                                        'content':prompt})
    with st.spinner('generate response...'):
        result = utils.call_ollama_model(model, prompt)
    
    st.chat_message('assistant').write(result)
    st.session_state['messages'].append({'role':'assistant', 'content':result})