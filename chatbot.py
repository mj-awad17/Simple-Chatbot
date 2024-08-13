api = "AIzaSyAcPWXRJG1apK5N1RipwPVrs3wYACoztLI"

print("Chatbot working ...")
# Libraries
import streamlit as st
import google.generativeai as genai

# Google API configure
genai.configure(api_key=api)

# initalize generative ai model
model = genai.GenerativeModel('gemini-1.5-flash')

# function to get response from model
def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text

# streamlit interface
st.set_page_config(page_title="Simple ChatBot!", layout='centered')
st.title("ChatBot 🤖")
st.write("Create by Muhammad Jawad.")


# form
with st.form(key="chat-form", clear_on_submit=True):
    # promopt input text using streamlit
    st.write("Google API use. ")
    prompt = st.text_input("", max_chars=2000)
    # send button
    submit_button = st.form_submit_button("Send")
    # condition if text_input empty
    if submit_button:
        if prompt:
            response = get_response(prompt)
            # display response 
            # st.write(response)
            st.session_state.history.append((prompt, response))
        else:
            st.warning("Please enter a prompt.")
            
# chat-history
if "history" not in st.session_state:
    st.session_state["history"] = []

# display chat history
for user_mgs, bot_mgs in st.session_state.history:
    st.markdown(f"""
                <div style="
                    background-color: #d1d3e0;
                    border-radius: 15px;    
                    padding: 10px 15px;
                    margin: 5px 0;
                    max-width: 70%;
                    text-align: left;
                    display: inline-block;
                    color:black;
                ">
                <p style="margin:0; font-size: 16px; line-height: 1.5"><b>You: </b>{user_mgs}</p>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown(f"""
                <div style="
                    background-color: #e1ffc7;
                    border-radius: 15px;
                    padding: 10px 15px;
                    margin: 5px 0;
                    max-width: 70%;
                    text-align: left;
                    display: inline-block;
                    color: black;
                ">
                <p style="margin:0; font-size: 16px; line-height: 1.5"><b>Bot: </b>{bot_mgs}</p>
                </div>
                """, unsafe_allow_html=True)

