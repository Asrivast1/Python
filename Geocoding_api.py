import json, urllib.request, urllib.parse, urllib.error
# Accessing addresses using geocoding API
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
while True:
    address = input("Enter location:")
    if len(address)<1:break
    url = serviceurl+urllib.parse.urlencode({"address":address})
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")
    try: js = json.loads(data) # If reading the json file fails
    except : js = None
    if not js or "status" not in js or js["status"]!="OK":
        print("==== Failure to retrieve data ====")
        print(data)
        continue
    lat = js["results"][0]["geometry"]["location"]["lat"] #Printing the longitude as wel as the latitude of the location
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    location = js["results"][0]["formatted_adress"]
    print(location)
