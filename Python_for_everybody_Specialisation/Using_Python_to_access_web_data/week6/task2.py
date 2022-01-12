import json
import urllib.request, urllib.parse, urllib.error
import ssl

api_key = False

# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')

parms = dict()
parms['address'] = address

if api_key is not False:
    parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving: ', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
info = json.loads(data)
print('Retrieved: ', len(data), 'characters')
# print(data.decode())

for i in info['results']:
    print('PlaceID ', i['place_id']) 
