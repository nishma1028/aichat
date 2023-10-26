import streamlit as st
from streamlit_chat import message
from bardapi import Bard
from bardapi import BardCookies
import json

cookie_dict = {
    "__Secure-1PSID": "cQjL-Anx5XP7qFBtrZiigBV28PnXb9ZWGMWU6I9ZgpTDbVwieZc2DE3ESRInI2P1Z5oYfQ.",
    "__Secure-1PSIDTS": "sidts-CjIBNiGH7u33XkjzTqB7Dd-ihSLkBdUaEqBAwKauXhXxbDDUN68qQ5uDvmhF74AvVVz_xRAA",
    "__Secure-1PSIDCC": "ACA-OxOIDYRRX2w80V8ZPYuCTGBI_LGwk-CTXPylzuACkeHQWdS-6jQTSqnK4Bt7zLZXdULXbA",
    "__Secure-3PSIDCC":"ACA-OxNoAoaobh0OBga34KXAhKmHt1CDp-MPDTm3HfiIo3zfsl0ArQjWL6CAznv4U9W1LqiiBw",
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


    
