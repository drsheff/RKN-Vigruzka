import os

path = "C:\\Programs\\zapros\\"

curdir = os.getcwd()
os.chdir(path)
out = os.system(r'c:\\CSP\\csptest.exe -sfsign -sign -detached -add -in "zapros.xml" -out "zapros.xml.sign" -my 007733670249')

if out == 0:
    print("Sign succsessfully!")
else:
    print("Sign ERROR!Check Certificate or Owner Subscriber")