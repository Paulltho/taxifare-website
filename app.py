import streamlit as st
import requests
from streamlit_folium import st_folium
import folium
from PIL import Image
import toml

# Load the .toml file
config = toml.load(".secrets.toml")

# Extract Mapbox details
MAPBOX_ACCESS_TOKEN = config["mapbox"]["MAPBOX_ACCESS_TOKEN"]
GEOCODING_API_URL = config["mapbox"]["GEOCODING_API_URL"]
DIRECTIONS_API_URL = config["mapbox"]["DIRECTIONS_API_URL"]
MODEL_API_URL = config["model"]["MODEL_API_URL"]


st.title("NYC taxi Fare Calculator")

image = Image.open("path/to/image.png")  # Replace with your image path
st.image(image, caption="Sample Image", use_column_width=True)

### HEADER 1: FILL IN FORM###
st.header("Your trip details")

### SUBHEADER 1.1: DETAIL FILL IN ###
st.markdown("_Please fill in your trip details._")

timestamp = st.text_input("Date and Time")
pickup_location = st.text_input("Pickup Location")
dropoff_location = st.text_input("Dropoff Location")
passenger_count = st.selectbox("Passenger Count", [1,2,3,4,5,6,7,8])


'''





## Here we would like to add some controllers in order to ask the user to select the parameters of the ride


1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

### SUBHEADER 1.2: MAP ###

pickup_longitude = st.text_input("Pickup Longitude")
pickup_latitude = st.text_input("Pickup Latitude")
dropoff_longitude = st.text_input("Dropoff Longitude")
dropoff_latitude = st.text_input("Dropoff Latitude")

st.header("Our prediction")


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not
even need to know anything about Data Science in order to retrieve a
prediction...

🤔 How could we call our API ? Off course... The `requests` package💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the
API...

## Finally, we can display the prediction to the user
'''
