import streamlit as st

try:
  import snowflake.connector
  st.success("Success!")
  st.snow()
except:
  st.error("Oh no!")
 
