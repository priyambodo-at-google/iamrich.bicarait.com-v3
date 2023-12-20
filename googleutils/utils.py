import streamlit as st

def reset_session() -> None:
    st.session_state['temperature'] = 0.2
    st.session_state['token_limit'] = 1024
    st.session_state['top_k'] = 40
    st.session_state['top_p'] = 0.8
    st.session_state['debug_mode'] = False
    st.session_state['prompt'] = []
    st.session_state['response'] = []

def hard_reset_session() -> None:
    st.session_state = {states : [] for states in st.session_state}

def create_session_state():
    if 'temperature' not in st.session_state:
        st.session_state['temperature'] = 0.2
    if 'token_limit' not in st.session_state:
        st.session_state['token_limit'] = 1024
    if 'top_k' not in st.session_state:
        st.session_state['top_k'] = 40
    if 'top_p' not in st.session_state:
        st.session_state['top_p'] = 0.8
    if 'debug_mode' not in st.session_state:
        st.session_state['debug_mode'] = False
    if 'prompt' not in st.session_state:
        st.session_state['prompt'] = []
    if 'response' not in st.session_state:
        st.session_state['response'] = []

##### NEW PARAMETER
# parameters = {
#     "temperature": 0.2,  # Temperature controls the degree of randomness in token selection.
#     "max_output_tokens": 1024,  # Token limit determines the maximum amount of text output.
#     "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
#     "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.                  
#     }

##### OLD PARAMETER
# parameters = {
#     "temperature": 0.0,  # Temperature controls the degree of randomness in token selection.
#     "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
#     "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
#     "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.                  
#     }