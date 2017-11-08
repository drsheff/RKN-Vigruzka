import os
import sys
import base64
#os.system('python generate_xml.py')
#os.system('python sign request.py')

with open('c:\\Programs\\zapros\\zapros.xml', 'rb') as zaprosxml:
    readzapros = zaprosxml.read()

with open('c:\\Programs\\zapros\\zapros.xml.sign', 'rb') as sign:
    contentsign = sign.read()

import zeep
# Send Request to rkn
#wsdl = 'http://vigruzki.rkn.gov.ru/services/OperatorRequest/?wsdl'
wsdl = 'http://vigruzki.rkn.gov.ru/services/OperatorRequestTest/?wsdl'
client = zeep.Client(wsdl=wsdl)
soap = client.service.sendRequest(readzapros, contentsign, '2.2')
code = soap['code']
print(soap)

# Get result from rkn
result = client.service.getResult(code)
zip = result['registerZipArchive']

with open('rkn.zip', "wb") as zipfile:
    zipfile.write(zip)