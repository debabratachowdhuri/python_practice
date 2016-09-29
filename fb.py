import facebook
import Image
import urllib, cStringIO

token = "<<token>>"

graph = facebook.GraphAPI(token)
profile = graph.get_object('me')
args = {'fields' : 'id,name,email', }
profile = graph.get_object('me', **args)
print (profile['email']);
url = "http://graph.facebook.com/"+profile['id']+"/picture"
file = cStringIO.StringIO(urllib.urlopen(url).read())
image = Image.open(file)
image.show()