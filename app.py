import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
import base64


# OpenWeatherMap API Key
WEATHER_API_KEY = '6a1a2dd2ef74b03e7b05079ac5ca3f6e'

# Unsplash API Key
UNSPLASH_API_KEY = 'T-BSzKk4KkGBYzpwMLzkbnTPyZH9LAWMAtr_2wyrRRc'


# Function to get current weather data
def get_weather(city):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric'
    response = requests.get(base_url)
    return response.json()

# Function to get 5-day weather forecast data
def get_forecast(city):
    base_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={WEATHER_API_KEY}&units=metric'
    response = requests.get(base_url)
    return response.json()

# Function to get weather icon
def get_weather_icon(icon_code):
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    icon_data = response.content
    return Image.open(BytesIO(icon_data))

# Function to get a background image from Unsplash
def get_background_image(city):
    base_url = f"https://api.unsplash.com/search/photos?query={city}&client_id={UNSPLASH_API_KEY}&orientation=landscape"
    response = requests.get(base_url)
    data = response.json()
    if data['results']:
        image_url = data['results'][0]['urls']['regular']  # Get the first image's URL
        image_response = requests.get(image_url)
        return Image.open(BytesIO(image_response.content))
    else:
        return None

# Function to encode image to base64
def encode_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# Streamlit App Layout
st.title("Enhanced Weather App with LangChain")

city = st.text_input("Enter city name below.")

if city:
    # Get and display background image
    background_image = get_background_image(city)
    if background_image:
       # Encode image to base64
        background_image_base64 = encode_image_to_base64(background_image)
        
        # Set background using custom HTML/CSS with reduced opacity and brightness
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), 
                            url(data:image/jpeg;base64,{background_image_base64});
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                z-index: 1; /* Set the background */
            }}
            .stApp > div > div {{
                position: relative;
                z-index: 2;
                color: #000000; /* Adjust text color for readability */
                font-size: 20px; /* Increase font size */
                font-weight: bold; /* Make headers bold */
            }}
            .stApp h1, .stApp h2, .stApp h3 {{
                color: #000; /* Adjust header color */
                font-size: 28px; /* Increase header size */
                font-weight: bold; /* Make headers bold */
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    weather_data = get_weather(city)
    
    if weather_data['cod'] == 200:
        st.header(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}")
        st.write(f"Temperature: {weather_data['main']['temp']}°C")
        st.write(f"Feels Like: {weather_data['main']['feels_like']}°C")
        st.write(f"Humidity: {weather_data['main']['humidity']}%")
        st.write(f"Pressure: {weather_data['main']['pressure']} hPa")
        st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        st.write(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
        
        # Display Weather Icon
        icon = get_weather_icon(weather_data['weather'][0]['icon'])
        st.image(icon, width=100)

        # 5-Day Weather Forecast Side by Side
        st.subheader("5-Day Forecast")
        forecast_data = get_forecast(city)
        if forecast_data['cod'] == '200':
            # Creating columns for side-by-side display
            cols = st.columns(5)
            for i, forecast in enumerate(forecast_data['list'][::8]):  # Take one forecast per day (8 * 3-hour intervals)
                with cols[i]:
                    # Extracting date and day
                    date_str = forecast['dt_txt']
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                    day = date_obj.strftime('%A')
                    date = date_obj.strftime('%d %B')
                    
                    # Displaying Date, Day, and Weather Info
                    st.write(f"**{day}**")
                    st.write(date)
                    temp = forecast['main']['temp']
                    description = forecast['weather'][0]['description'].capitalize()
                    icon_code = forecast['weather'][0]['icon']
                    icon = get_weather_icon(icon_code)
                    
                    st.write(f"Temp: {temp}°C")
                    st.write(description)
                    st.image(icon, width=80)
        else:
            st.error("Could not retrieve forecast data.")
    else:
        st.error("City not found. Please enter a valid city name.")
