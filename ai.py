import streamlit as st
from streamlit_chat import message
from bardapi import Bard
from bardapi import BardCookies
import json

cookie_dict = {
    "__Secure-1PSID": "cQhCZ0Hnt_kQSweU5ZiHbZkfYBLc9dmghM0_agUF3R_Ea05FqNSC3aRYOXBLMysJkF43IQ.",
    "__Secure-1PSIDTS": "sidts-CjEB3e41hX2F-K_S1Rq_5mRkJ1g6PEcraBVELC4jxMNcbMTqwBRVnS8zDbzpK-oMkG8dEAA",
    # Any cookie values you want to pass session object.
}

bard = BardCookies(cookie_dict=cookie_dict)

st.title("AI-COMPANION")

changes='''
    <style>
    [data-testid="stAppViewContainer"]
    {
    background-color:rgba(255,255,255,0.05);
    background-size:fit;
    }
    .st-bx {
    background-color: rgba(255, 255, 255, 0.05);
    }

    /* .css-1hynsf2 .esravye2 */

    html {
    background: transparent;
    }
    div.esravye2 > iframe {
        background-color: transparent;
    }
    </style>
    '''
    
st.markdown(changes,unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def generate_response(prompt):
    response = bard.get_answer(prompt)['content']
    return response

if prompt := st.text_input( "hey wassup?", key="input"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = generate_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):

        st.markdown(response)


    