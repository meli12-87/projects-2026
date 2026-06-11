import streamlit as st
import time

pronpet = st.chat_input('Enter your question')

if pronpet:
    st.write(pronpet)



message = st.chat_message('ai').write('How can I help you?')
message2 = st.chat_message('user').write('Give Me Correct Answer')

#with st.spinner('Wait For An Answer...'):
  #  time.sleep(6)

#st.write('Finish')

#count=0

#if st.button('ADD'):
  ## st.write(f'Count:{count}')

st.write(f'Session_state:{st.session_state}')
if 'counter' not in st.session_state:
    st.session_state['counter']=0

if st.button('ADD'):
    st.session_state['counter'] +=1
    st.write(f'counter: {st.session_state['counter']}')