import geocoder

def get_current_location():
    g = geocoder.ip('me')
    return g.latlng  # Returns a tuple with latitude and longitude


# local_location = get_local_location()
# print("Latitude:", local_location[0])
# print("Longitude:", local_location[1])
