"""
    Simple Streamlit webserver application for serving developed classification
	models.
    Author: Rogue byte Analytica.
    Note:
    ---------------------------------------------------------------------
    Plase follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------
	For further help with the Streamlit framework, see:
	https://docs.streamlit.io/en/latest/
"""

#import Dependencies
import streamlit as st
import datetime
import pandas as pd

def main():
    st.header('Hello Nemisa Hackathon')
    st.write("<h3 align='center'>This is Rogue Byte Analytica</h3>",unsafe_allow_html=True)


if __name__ == '__main__':
	main()