import requests
import json

# Get the feed
r = requests.get("https://api.themoviedb.org/3/movie/550?api_key=13ef1e7771b4887b9470d27d67577c2a")
i= 0
# Convert it to a Python dictionary
data = json.loads(r.text)
print data
# Loop through the result.
for item in data['production_companies']:

    print "Video Title: %s" % (item['name'])

    print "Video ID: %d" % (item['id'])

    i  = i + 1
