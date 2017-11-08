import sys
import time, datetime
from lxml import etree
request = etree.Element("request")
requestTime = etree.SubElement(request, "requestTime")
requestTime.text = time.strftime("%Y"+'-'+"%m"+'-'+"%d"+'T'+"%H"+'-'+"%M"+'-'+"%S%z")
operatorName = etree.SubElement(request, "operatorName")
operatorName.text = "OOO TELLAN"
inn = etree.SubElement(request, "inn")
inn.text = "007733670249"
ogrn = etree.SubElement(request, "ogrn")
ogrn.text = "5087746161553"
email = etree.SubElement(request, "email")
email.text = "sergey.silich@runexis.ru"

zapros = etree.tostring(request, encoding="windows-1251")
zapros_str = zapros.decode("windows-1251")
convert = zapros_str.replace("'", "\"")
xmltree = etree.tostring(request, encoding="windows-1251")

try:
    file = open('C:\\Programs\\zapros\zapros.xml', 'w', encoding="windows-1251")
    file.write(convert)
except IOError:
    print("Can't open")
else:
    file.close()
    print("Generate file is successfully")
