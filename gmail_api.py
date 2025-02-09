import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Streamlit UI
st.title("💬 Gmail Genie")
st.write("Hey dude!!Chat with your Gmail AI assistant!")

# Chat history initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chatbot response function
def get_chat_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Chat input
if prompt := st.chat_input("Ask me anything!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = get_chat_response(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            st.markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
