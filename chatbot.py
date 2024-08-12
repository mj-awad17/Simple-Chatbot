print("Chatbot working ...")
# Libraries
import streamlit as st
import google.generativeai as genai
import api

# Google API configure
genai.configure(api_key=api)
