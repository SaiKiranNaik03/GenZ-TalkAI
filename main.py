import streamlit as st
import requests
import json
import time

# Apply custom CSS for futuristic, vibrant design
st.set_page_config(page_title="GenZ-TalkAI", layout="centered")

st.markdown("""
    <style>
        .main-container {
            background: linear-gradient(135deg, #1f1c2c, #928dab);
            font-family: 'Poppins', sans-serif;
            color: #fff;
        }
        .main .block-container {
            max-width: 850px;
            margin: auto;
            padding: 4rem 3rem;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 25px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.25);
        }
        h1 {
            color: #f7f7f7;
            text-align: center;
            font-size: 3rem;
            margin-bottom: 1.5rem;
        }
        .stChatMessage {
            border-radius: 30px;
            font-size: 1.3rem;
        }
        .user .stChatMessage {
            background-color: #00c6ff;
            color: white;
            text-align: left;
            font-size: 1.4rem;
        }
        .assistant .stChatMessage {
            background-color: rgba(255, 255, 255, 0.15);
            color: #f1f1f1;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.3);
            font-size: 1.4rem;
        }
        .stChatInput input {
            border-radius: 50px;
            padding: 18px;
            border: none;
            outline: none;
            background-color: rgba(255, 255, 255, 0.2);
            color: #fff;
            font-size: 1.2rem;
        }
        .stChatInput input::placeholder {
            color: #ccc;
        }
        .stButton>button {
            border-radius: 50px;
            background-color: #4caf50;
            color: white;
            font-size: 1.1rem;
            padding: 12px 30px;
        }
        .stApp {
            background-color: transparent;
        }
    </style>
    <div class="main-container"></div>
""", unsafe_allow_html=True)

# Function to generate response using API
def response_generator(user):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    api_key = "YOUR_API_KEY"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": user}]}]}

    response = requests.post(f"{url}?key={api_key}", headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        try:
            response_data = response.json()
            return response_data['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError, ValueError) as e:
            return f"Error parsing response: {str(e)}"
    else:
        return f"Error: {response.status_code} - {response.text}"

# App UI setup
st.title("GenZ-TalkAI ✨")

with st.chat_message("assistant", avatar="./chatbot.png"):
    st.write("👋 Hey Kiran! How can I help you today?")

if "message" not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    avatar = "./programmer.png" if message['role'] == "user" else "./chatbot.png"
    with st.chat_message(message['role'], avatar=avatar):
        st.write(message['content'])

# Chat input and response
if prompt := st.chat_input("💬 Ask me anything..."):
    with st.chat_message("user", avatar="./programmer.png"):
        st.write(prompt)
    st.session_state.message.append({"role": "user", "content": prompt})

    try:
        response = response_generator(prompt)
        assistant_reply = response

        with st.chat_message("assistant", avatar="./chatbot.png"):
            message_placeholder = st.empty()
            typed_msg = ""
            for char in response:
                typed_msg += char
                message_placeholder.markdown(typed_msg)
                time.sleep(0.01)

        st.session_state.message.append({"role": "assistant", "content": assistant_reply})

    except requests.exceptions.RequestException as e:
        st.error(f"❌ An error occurred: {e}")
    except KeyError:
        st.error("⚠️ Failed to parse the response. Please check the API response format.")



# Inital Trial Code

# import streamlit as st
# import requests
# import json
# import time
# def response_generator(user):
#     url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
#     api_key = "AIzaSyCgFKdRQNa8tZ3R3zxfA5BvZLF-WwMyLlI"
#     headers = {
#         "Content-Type": "application/json"
#     }
#     data = {
#         "contents": [
#             {
#                 "parts": [
#                     {
#                         "text": user
#                     }
#                 ]
#             }
#         ]
#     }

#     # Make the POST request
#     response = requests.post(f"{url}?key={api_key}", headers=headers, data=json.dumps(data))
#     if response.status_code == 200:
#         try:
#             response_data = response.json()  # Parse the JSON response
#             # Extract the text part
#             return response_data['candidates'][0]['content']['parts'][0]['text']
#         except (KeyError, IndexError, ValueError) as e:
#             return f"Error parsing response: {str(e)}"
#     else:
#         return f"Error: {response.status_code} - {response.text}"
# st.logo("./AI logo.webp")
# st.title("GenZ-TalkAI")
# with st.chat_message("assistant",avatar="./AI logo.webp"):
#     st.write("Hi Kiran, How may I help you today!!")
# if "message" not in st.session_state:
#     st.session_state.message = []

# for message in st.session_state.message:
#     with st.chat_message(message['role']):
#         st.write(message['content'])

# if prompt := st.chat_input("Ask anything..."):
#     with st.chat_message("user",avatar="./User logo.webp"):
#         st.write(prompt)
#     st.session_state.message.append({"role": "user", "content": prompt})

#     try:
#         response=response_generator(prompt)
#         assistant_reply = response

#         with st.chat_message("assistant",avatar="./AI logo.webp"):
#             message_placeholder = st.empty()
#             typed_msg=""
#             for char in response:
#                 typed_msg += char
#                 message_placeholder.markdown(typed_msg)
#                 time.sleep(0.01)

#         st.session_state.message.append({"role": "assistant", "content": assistant_reply})

#     except requests.exceptions.RequestException as e:
#         st.error(f"An error occurred: {e}")
#     except KeyError:
#         st.error("Failed to parse the response. Please check the API response format.")
        