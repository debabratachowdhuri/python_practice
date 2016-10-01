import facebook
import Image
import urllib, cStringIO
import key
import fbAccesstoken

app_id = key.Auth_token.APP_ID
app_secret = key.Auth_token.APP_SECRET
fbToken = fbAccesstoken.FbToken();

token = fbToken.get_app_access_token(app_id, app_secret)

graph = facebook.GraphAPI(key.Auth_token.FB_AUTH_TOKEN)
# profile = graph.get_object('me')
args = {'fields' : 'id,name,email', }
profile = graph.get_object('me', **args)
print (profile['email']);
url = "http://graph.facebook.com/"+profile['id']+"/picture"
file = cStringIO.StringIO(urllib.urlopen(url).read())
image = Image.open(file)
image.show()