import streamlit as st # imports streamlit library to create UI elements

# function to ddisplay UI form to user
def journal_input_form():
    with st.form("journal_form"): # creates a form block to contains all inputs and submit together
        journal = st.text_area("Morning Journal") # create a multi line text box for user to input morning journal
        dream = st.text_area("Dream") # create a multi line text box for user to input dream
        intention = st.text_area("Intention of the Day") # create a multi line text box for user to input intentions
        priorities = st.text_area("Top 3 Priorities (comma-separated)") # create a multi line text box for user to input priorities
        submitted = st.form_submit_button("Reflect") # A button to submit form data
    return journal, dream, intention, priorities, submitted # return all form inputs
