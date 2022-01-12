import xml.etree.ElementTree as ET

data = '''
<person>
    <name> Chuck </name>
    <phone type = 'intl'>
        +1 734 303 44 56
    </phone>
    <email hide = 'yes'/>
</person>
'''

tree = ET.fromstring(data)

print('Name: ', tree.find('name').text)
print('Email: ', tree.find('email').get('hide'))