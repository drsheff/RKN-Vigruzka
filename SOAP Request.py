import os
import sys
import base64
import zeep
#os.system('python generate_xml.py')
#os.system('python sign request.py')
#openpath =
#writepath =

def zaprosxml():
    global readzapros
    try:
        with open('c:\\Programs\\zapros\\zapros.xml', 'rb') as zaprosxml:
            readzapros = zaprosxml.read()
    except IOError:
        print ("Error: File does not exist")
        sys.exit(1)
        return

def sign():
    global contentsign
    try:
        with open('c:\\Programs\\zapros\\zapros.xml.sign', 'rb') as sign:
            contentsign = sign.read()
    except IOError:
        print ("Error: File does not exist")
        sys.exit(1)
        return

zaprosxml()
sign()

# Send Request to rkn
#wsdl = 'http://vigruzki.rkn.gov.ru/services/OperatorRequest/?wsdl'
wsdl = 'http://vigruzki.rkn.gov.ru/services/OperatorRequestTest/?wsdl' # For Test
client = zeep.Client(wsdl=wsdl)
soap = client.service.sendRequest(readzapros, contentsign, '2.2')
code = soap['result']
if code == True:
    print(soap['resultComment'])
    # Get result from rkn
    result = client.service.getResult(code)
    zip = result['registerZipArchive']

    with open('rkn.zip', "wb") as zipfile:
        zipfile.write(zip)
else:
    print(soap['resultComment'])