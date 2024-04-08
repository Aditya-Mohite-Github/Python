import argparse
import weatherandtimeutils
import locationutils

parser = argparse.ArgumentParser()

# 'weather' as a positional argument (mandatory)
parser.add_argument('weather', help="Main command keyword")

# argument for version
parser.add_argument('-v', '--version', action='store_true' , help="Outputs the Version of the Application")

# argument for location for it's weather and current for exact location weather with help of co-ordinates using geocoder in locationutils.py
parser.add_argument('mode',nargs='?'  ,choices=['location', 'current'], help="Specify mode: 'location' to get weather by coordinates or 'current' to get weather for current location")
parser.add_argument('locationarg' , nargs='?', help="Argument if location is Entered")


args = parser.parse_args()

if args.version: print("Weather Utility ver 1.1")

if args.mode == 'location':
    if args.locationarg:
        weatherandtimeutils.get_forecast_by_location(args.locationarg)
    else: print("Location Not Provided")
elif args.mode == 'current':
    coordinates = locationutils.get_coordinates()
    weatherandtimeutils.get_forecast_by_coordinates(coordinates.split(',')[0] , coordinates.split(',')[1])


