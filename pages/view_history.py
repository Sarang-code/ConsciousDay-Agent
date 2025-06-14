import streamlit as st  # imports streamlit library to create UI elements
from database.db import get_entries_by_date # get_entries_by_date() from database/db.py module

st.set_page_config(page_title="Past Reflections", page_icon="📅") # Set the browser tab title and icon

st.title("View Past Reflections") # Sets the main title of the page at the top

#  Creates a date picker input where the user selects a specific date.
selected_date = st.date_input("Select a date")
if st.button("Load Entry"): # Displays a button labeled “Load Entry”.
    entries = get_entries_by_date(str(selected_date)) # Calls database function to fetch all entries for the selected date
    if entries: #  If any entry/entries are found, continue to display them.
        for entry in entries: # Loop through all entries
            st.header(f"Reflections on {entry[1]}") # Displays a header with the entry date
            st.markdown(f"- **Journal:** {entry[2]}") # Display morning journal of user given on that day
            st.markdown(f"- **Intention:** {entry[3]}") # display intentions of user on that day
            st.markdown(f"- **Dream:** {entry[4]}") # Display dream of user on that day
            st.markdown(f"- **Priorities:** {entry[5]}") # Display priorities of user on that day
            st.subheader(f" **Reflection:**\n\n{entry[6]}") #  Displays the AI-generated Reflection
            st.subheader(f" **Strategy:**\n{entry[7]}") # displays the AI-generated strategy
    else:
        st.warning("No entries found for this date.") #  If no entries were found, shows a warning message
