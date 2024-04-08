# Importing the necessary modules
import argparse               # Module for parsing command-line arguments
import weatherandtimeutils    # Custom module for weather and time-related utilities
import locationutils          # Custom module for location-related utilities

# Creating an ArgumentParser object to handle command-line arguments
parser = argparse.ArgumentParser()

# Adding positional argument 'weather' which is mandatory and will be the main command keyword
parser.add_argument('weather', help="Main command keyword")

# Adding optional argument for version which triggers the output of application version
parser.add_argument('-v', '--version', action='store_true', help="Outputs the Version of the Application")

# Adding argument for mode: 'location' to get weather by coordinates or 'current' to get weather for current location
parser.add_argument('mode', nargs='?', choices=['location', 'current'], help="Specify mode: 'location' to get weather by coordinates or 'current' to get weather for current location")

# Adding argument for location if 'mode' is 'location'
parser.add_argument('locationarg', nargs='?', help="Argument if location is Entered")

# Parsing the command-line arguments
args = parser.parse_args()

# If version argument is provided, print the version of the application
if args.version:
    print("Weather Utility ver 1.2")

# If mode is 'location', check if location argument is provided, and call the respective function accordingly
elif args.mode == 'location':
    if args.locationarg:
        weatherandtimeutils.get_forecast_by_location(args.locationarg)
    else:
        print("Location Not Provided")
        
# If mode is 'current', get current coordinates and call the function to get weather forecast by coordinates
elif args.mode == 'current':
    coordinates = locationutils.get_coordinates()
    weatherandtimeutils.get_forecast_by_coordinates(coordinates.split(',')[0], coordinates.split(',')[1])
