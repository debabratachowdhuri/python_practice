import requests
import json
import key

# Get the feed
r = requests.get("https://api.themoviedb.org/3/movie/550?api_key="+key.Auth_token.MOVIE_API_KEY)

# Convert it to a Python dictionary
data = json.loads(r.text)
# print data
# Loop through the result.
for item in data['production_companies']:

    print "Video Title: %s" % (item['name'])

    print "Video ID: %d" % (item['id'])


data = json.loads(r.text)
