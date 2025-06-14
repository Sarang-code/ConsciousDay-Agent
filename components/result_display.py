import streamlit as st # imports streamlit library to create UI elements

def display_result(reflection, strategy): # This function is used to display results
    st.success("Reflection Complete") # Show success message at the top of the output.
    st.subheader("Reflection") # Adds a subheader "Reflection"
    st.write(reflection) # displays the reflection text
    st.subheader("Strategy") # Adds a subheader "Strategy"
    st.write(strategy) # displays the strategy text
