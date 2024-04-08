import requests  # Importing the requests module to make HTTP requests

# Function to get weather forecast by coordinates
def get_forecast_by_coordinates(latitude, longitude):
    # API endpoint and parameters
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": f"{latitude},{longitude}", "days": "3"}
    headers = {
        "X-RapidAPI-Key": "YOUR API KEY",  # Replace 'YOUR API KEY' with your actual API key
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    # Make the request
    response = requests.get(url, headers=headers, params=querystring)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        response_dict = response.json()

        # Define the keys you want to extract
        keys_to_extract = ['location', 'current']
        
        # Extract key-value pairs
        extracted_data = {}
        for key in keys_to_extract:
            if key in response_dict:
                extracted_data[key] = response_dict[key]

        # Print the extracted information
        location_info = extracted_data.get('location', {})
        current_info = extracted_data.get('current', {})
        dntime = "Night" if current_info.get('is_day') == 0 else "Day"
        Time = location_info.get('localtime' , {})  

        print(
            "\n", "-"*50, "Weather Report", "-"*50, "\n \n"
            f"  Location information:    {location_info.get('name')} , {location_info.get('region')} , {location_info.get('country')}\n \n"
            f"  Date: {str(Time).split(' ')[0]} , Time : {str(Time).split(' ')[1]} {dntime} \n \n"
            f"  Current Temperature:     {current_info.get('temp_c')}°C\n \n"
            f"  Weather Condition:       {current_info.get('condition', {}).get('text')}\n \n"
            f"  Wind speed:              {current_info.get('wind_kph')} kph\n \n"
        )

    else:
        print("Error:", response.status_code)

# Function to get weather forecast by location
def get_forecast_by_location(city):
    # API endpoint and parameters
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    querystring = {"q": city, "days": "3"}
    headers = {
        "X-RapidAPI-Key": "YOUR API KEY",  # Replace 'YOUR API KEY' with your actual API key
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    # Make the request
    response = requests.get(url, headers=headers, params=querystring)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        response_dict = response.json()

        # Define the keys you want to extract
        keys_to_extract = ['location', 'current']
        
        # Extract key-value pairs
        extracted_data = {}
        for key in keys_to_extract:
            if key in response_dict:
                extracted_data[key] = response_dict[key]

        # Print the extracted information
        location_info = extracted_data.get('location', {})
        current_info = extracted_data.get('current', {})
        dntime = "Night" if current_info.get('is_day') == 0 else "Day"
        Time = location_info.get('localtime' , {})  

        print(
            "\n", "-"*50, "Weather Report", "-"*50, "\n \n"
            f"  Location information:    {location_info.get('name')} , {location_info.get('region')} , {location_info.get('country')}\n \n"
            f"  Date: {str(Time).split(' ')[0]} , Time : {str(Time).split(' ')[1]} {dntime} \n \n"
            f"  Current Temperature:     {current_info.get('temp_c')}°C\n \n"
            f"  Weather Condition:       {current_info.get('condition', {}).get('text')}\n \n"
            f"  Wind speed:              {current_info.get('wind_kph')} kph\n \n"
        )

    else:
        print("Error:", response.status_code)
