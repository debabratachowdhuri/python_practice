import facebook
import Image
import urllib, cStringIO

token = "EAALY5GhzJvUBAPQHEhH6sY6Dkd5UaaZAE4jlwqvcOnPVAwwAtSw8f6ggG3ggljCYHHZBRyNSCFUz70r2Tmm7wYyMtZCnrNsonnL6NhNVMEHwiyozh3HGZBAdxVFnJy933w8PtUVRi9ZBnZAiSdcuBKxZCEykUU1OpECbcMWANPUmAZDZD"

graph = facebook.GraphAPI(token)
profile = graph.get_object('me')
args = {'fields' : 'id,name,email', }
profile = graph.get_object('me', **args)
print (profile['email']);
url = "http://graph.facebook.com/"+profile['id']+"/picture"
file = cStringIO.StringIO(urllib.urlopen(url).read())
image = Image.open(file)
image.show()