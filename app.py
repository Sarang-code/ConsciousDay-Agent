import streamlit as st # imports streamlit library to create UI elements
from datetime import date # to get the current date
from database.db import create_db, save_entry 
from agent.prompt_engine import generate_insight
from components.journal_form import journal_input_form
from components.result_display import display_result

st.set_page_config(page_title="ConsciousDay Agent", page_icon="🧘") # Set the browser tab title and icon

create_db() # Initializes the database and creates the entries table if it doesn't already exist

st.title("ConsciousDay Agent") # sets the main page tittle

# call a function to show UI elements and capture what it return.
journal, dream, intention, priorities, submitted = journal_input_form()

if submitted: # Executes the reflection logic only after the user clicks the "Reflect" button
    if not all([journal.strip(), intention.strip(), dream.strip(), priorities.strip()]): # If any of the 4 fields are empty or only contain spaces, shows an error and skips processing
        st.error("All fields are required.")
    else:
        with st.spinner("Reflecting..."): # Shows a spinner, gives the user feedback while waiting for the AI response.
            result = generate_insight(journal, intention, dream, priorities) # Sends all 4 inputs to the AI model and store response in result variable

            # Separate reflection and strategy from AI output/response
            parts = result.split("Suggested Day Strategy")

            reflection = parts[0].strip().removesuffix("4.") # removes '4. ' at the end.

            # if split is successfull and the length of parts is greater than 1
            # then add "Suggested Day Strategy " at the starting of text
            # else keeo it empty to avoid errors   
            strategy = "Suggested Day Strategy " + parts[1].strip() if len(parts) > 1 else ""

            # Saves the full entry (user inputs + AI results) into the SQLite database using save_entry() function
            save_entry({
                "date": str(date.today()),
                "journal": journal,
                "intention": intention,
                "dream": dream,
                "priorities": priorities,
                "reflection": reflection,
                "strategy": strategy
            })

            # Displays the reflection and strategy to the user in a clean format using result_display.py component.
            display_result(reflection, strategy)