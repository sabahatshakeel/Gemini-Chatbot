import streamlit as st
import google.generativeai as genai

# Configure the API key
GOOGLE_API_KEY = st.secrets['chatbot_api_key']

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the generative AI model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def get_chatbot_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit interface
st.set_page_config(page_title="Smart ChatBot", layout="centered")

# Custom CSS for chat bubbles with full width and emojis
st.markdown("""
    <style>
    .chat-container {
        display: flex;
        flex-direction: column;
        width: 100%;
    }
    .chat-bubble {
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        font-size: 18px;
        color: white;
        display: inline-block;
        line-height: 1.5;
    }
    .user-bubble {
        background: #6a82fb; /* Soft blue */
        align-self: flex-end;
        border-radius: 10px 10px 10px 10px;
    }
    .bot-bubble {
        background: #fc5c7d; /* Soft pink */
        align-self: flex-start;
        border-radius: 10px 10px 10px 10px;
    }
    .chat-header {
        # text-align: center;
        font-size: 35px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #3d3d3d;
    }
    .emoji {
        font-size: 22px;
        margin-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-header">Gemini Chatbot-Your AI Companion 💻</div>', unsafe_allow_html=True)
st.write("Powered by Google’s Gemini AI for smart, engaging conversations. 🤖")

if "history" not in st.session_state:
    st.session_state["history"] = []

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message here... ✍️", max_chars=2000, label_visibility="collapsed")
    submit_button = st.form_submit_button("Send 🚀")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please Enter A Prompt 😅")

if st.session_state["history"]:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for user_input, response in st.session_state["history"]:
        st.markdown(f'<div class="chat-bubble user-bubble"><span class="emoji">👤</span>You: {user_input}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-bubble bot-bubble"><span class="emoji">🤖</span>Bot: {response}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

