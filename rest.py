import requests
import json

# Get the feed
r = requests.get("https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key=AIzaSyB5jNDWFwXL38zBTH70nz7BChg6kBFWwmg&part=snippet,contentDetails,statistics,status")
r.text

# Convert it to a Python dictionary
data = json.loads(r.text)
print data
# Loop through the result.
# for item in data['data']['items']:
#
#     print "Video Title: %s" % (item['title'])
#
#     print "Video Category: %s" % (item['category'])
#
#     print "Video ID: %s" % (item['id'])
#
#     print "Video Rating: %f" % (item['rating'])
#
#     print "Embed URL: %s" % (item['player']['default'])
