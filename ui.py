# import streamlit as st
# import requests

# st.title("🧑‍🏫 English Communication Chatbot")

# user_input = st.text_input("Enter your message:")

# if st.button("Send"):
#     response = requests.post(
#         "http://127.0.0.1:8000/chat",
#         params={"msg": user_input}
#     )

#     result = response.json()
#     st.write("🤖 Bot:", result["response"])