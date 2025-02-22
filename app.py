import streamlit as st
import requests
import json
from datetime import datetime

st.title("Sport Questionnaire")

# Adding introduction text
st.write("Welcome to our short questionnaire. Please answer the following questions.")

# Creating the form
with st.form("questionnaire"):
    # Question 1 - text input
    name = st.text_input("1. What is your name?")
    
    # Question 2 - selection box
    age_group = st.selectbox(
        "2. Which age group do you belong to?",
        ["18-25", "26-35", "36-45", "46-55", "56 and above"]
    )
    
    # Question 3 - radio buttons
    exercise = st.radio(
        "3. How often do you exercise?",
        ["Every day", "Several times a week", "Several times a month", "Never"]
    )
    
    # Question 4 - slider
    satisfaction = st.slider(
        "4. How satisfied are you with your life? (1 = least, 10 = most)",
        min_value=1,
        max_value=10,
        value=5
    )
    
    # Question 5 - text area
    feedback = st.text_area(
        "5. Do you have any additional comments or feedback?"
    )
    
    # Submit button
    submit = st.form_submit_button("Submit answers")

# Display responses after submission
if submit:
    st.success("Thank you for completing the questionnaire!")
    
    # Prepare webhook data
    webhook_url = "https://stream-in.europe-west3.gcp.keboola.com/stream/978/nord-stream-3/VPtWx8XMoL77pEAQmbtOenoyJJyrHcXtT5Xg2eH7AX9UkwhE"
    
    payload = {
        "id": f"form-submission-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        "time": datetime.now().isoformat(),
        "data": {
            "name": name,
            "age_group": age_group,
            "exercise": exercise,
            "satisfaction": satisfaction,
            "feedback": feedback
        }
    }

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            st.success("Data sent successfully!")
        else:
            st.error(f"Error sending data: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

    # Display answers
    st.write("Your answers:")
    st.write(f"Name: {name}")
    st.write(f"Age group: {age_group}")
    st.write(f"Exercise frequency: {exercise}")
    st.write(f"Life satisfaction: {satisfaction}")
    st.write(f"Additional comments: {feedback}") 