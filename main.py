#Required liabries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of Availabe Time Zone
TIME_ZONE = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Create Aap Title
st.title("🕑 Time Zone App")

# Create a mutliselect widget for selected timezones
selected_timezone = st.multiselect("Select Timezones", TIME_ZONE, default=["UTC", "Asia/Karachi"])

#Display the timezones
st.subheader("Selected Timezones")

for tz in selected_timezone:

    #Get and format current time for each selected timezone with AM/PM
    now = datetime.now(ZoneInfo(tz))
    current_time = now.strftime("%Y-%m-%d %I:%M:%S %p")

    # Time-based Emoji Selection
    hour = now.hour
    if 6 <= hour < 12:
        emoji ="🌅" # Morning
    elif 12 <= hour < 18:
        emoji = "☀️" # Afternoon
    elif 18 <= hour < 21:
        emoji = "🌇" #Evening
    else:
        emoji = "🌙" # Night

    st.write(f"{emoji}  **{tz}**: {current_time}")

# Create a subeader for Converting time between timezones 
st.subheader("Convert Time Between Timezones")

#Create a time widget for the current time
current_time = st.time_input("Current Time", value=datetime.now().time())

#Create a selectbox for selecting the timezone to Convert from
from_tz = st.selectbox("From Timezone", TIME_ZONE, index=0)

#Create a selectbox for selecting the timezone to Convert to
to_tz = st.selectbox("To Timezoze", TIME_ZONE, index=1)

# Create a button to trigger the time coversion
if st.button("Convert Time"):

    # Combine the current time with the selected date.
    dt = datetime.combine(datetime.today(), current_time).replace(tzinfo=ZoneInfo(from_tz))

    # Convert the time to the selected timezone
    converted_time =dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")

    # Display the converted time
    st.success(f"Converted Time in {to_tz}: {converted_time}")

