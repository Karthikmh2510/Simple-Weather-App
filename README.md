# Simple-Weather-App
This is a simple weather app which is developed using Streamlit and Python
To create a comprehensive `README.md` file for your Enhanced Weather App with Streamlit, you need to provide a detailed description of the application, installation steps, usage instructions, and information about the APIs used. Here's a structured and detailed guide for your `README.md` file:

---

# Enhanced Weather App with Streamlit

This repository contains an **Enhanced Weather App** built using **Streamlit** that provides real-time weather information and a 5-day weather forecast for a city. The app uses **OpenWeatherMap API** for weather data and **Unsplash API** to fetch background images of the cities.

## Features

- **Current Weather Data**: Displays temperature, humidity, pressure, wind speed, and weather description with an icon for a given city.
- **5-Day Weather Forecast**: Provides a 5-day weather forecast displayed side-by-side with date, temperature, description, and icons.
- **Dynamic Background**: Fetches city-specific background images from Unsplash to enhance the user experience.
- **Responsive Design**: Uses Streamlit's responsive layout and custom HTML/CSS for a visually appealing interface.

## Installation Guide

Follow these steps to set up the Enhanced Weather App on your local machine:

### 1. Prerequisites

- Python 3.7 or later installed on your machine.
- A web browser for viewing the Streamlit app.

### 2. Clone the Repository

Clone the repository to your local machine using:

```bash
git clone https://github.com/karthikmh2510/simple-weather-app.git
cd simple-weather-app
```

### 3. Create and Activate a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment for Python projects:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS and Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Required Packages

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include:

```plaintext
streamlit==1.26.0
requests==2.31.0
Pillow==10.0.0
```

You can generate this file using the following command if you don't have it yet:

```bash
pip freeze > requirements.txt
```

### 5. Set Up API Keys

You need to set up API keys for the **OpenWeatherMap** and **Unsplash** services:

1. **OpenWeatherMap API Key**: Sign up at [OpenWeatherMap](https://openweathermap.org/api) and generate an API key.
2. **Unsplash API Key**: Sign up at [Unsplash Developers](https://unsplash.com/developers) and create an application to get an API key.

After obtaining the keys, replace the placeholders in the Python script:

```python
# OpenWeatherMap API Key
WEATHER_API_KEY = 'your_openweathermap_api_key'

# Unsplash API Key
UNSPLASH_API_KEY = 'your_unsplash_api_key'
```

### 6. Run the Application

Execute the following command in the terminal to run the Streamlit app:

```bash
streamlit run app.py
```

Replace `app.py` with the name of your Python file if it's different. The application should open in a new tab in your default web browser. If it doesn't, visit `http://localhost:8501` manually.

## Usage

1. **Enter a City Name**: Type the name of a city in the input box.
2. **View Current Weather**: The app displays current weather details like temperature, humidity, wind speed, and a descriptive icon.
3. **View 5-Day Forecast**: Check the 5-day weather forecast for the entered city. Forecasts are presented side-by-side with icons and descriptions.
4. **Dynamic Background**: Enjoy a dynamically changing background image related to the city.

## Explanation of Key Components

- **`get_weather(city)`**: Fetches current weather data for the city using the OpenWeatherMap API.
- **`get_forecast(city)`**: Fetches a 5-day weather forecast using the OpenWeatherMap API.
- **`get_weather_icon(icon_code)`**: Fetches the weather icon corresponding to the weather condition code.
- **`get_background_image(city)`**: Fetches a background image for the city using the Unsplash API.
- **`encode_image_to_base64(image)`**: Encodes the image to Base64 format to be used in HTML/CSS for custom backgrounds.
- **Custom HTML/CSS Styling**: Enhances the Streamlit app's appearance using custom styling to set backgrounds and adjust text visibility.

## APIs Used

1. **OpenWeatherMap API**: Provides current weather data and 5-day weather forecasts. [OpenWeatherMap Documentation](https://openweathermap.org/api)
2. **Unsplash API**: Provides high-quality images based on search queries. [Unsplash API Documentation](https://unsplash.com/developers)

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. Contributions are highly appreciated!

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/your-feature`).
3. Commit your Changes (`git commit -m 'Add some feature'`).
4. Push to the Branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Karthik Manjunath Hadagali - [karthik.m.hadagali2013@example.com](mailto:karthik.m.hadagali2013@example.com)

Project Link: [https://github.com/your-username/enhanced-weather-app](https://github.com/your-username/enhanced-weather-app)

---

Replace `your-username` with your GitHub username and `your-email@example.com` with your email address. Feel free to modify the content as needed for your project!
