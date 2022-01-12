import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

api_key = False

api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key = False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while TRUE:
    address = input('Enter location: ')

    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address

    if api_key is not False:
        parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)
        print('Retrieving: ', url)
        uh = urllib.request.urlopen(url, context=ctx)

        data = uh.read()
        print('Retrieved: ', len(data), 'characters')
        print(data.decode())
        tree = ET.fromstring(data)

        results = tree.findall('result')

        lat = results[0].find('geometry').find('location').find('lat').text
        long= results[0].find('geometry').find('location').find('lng').text
    
    print('lat', lat, 'long', long)
    print(location)
