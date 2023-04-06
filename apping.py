import json
import requests
headers = {
    "Authorization":"Bearer ya29.a0Ael9sCN_7-I9V7YB5N5sKrGQVkE7tihsa5THbm9xsq80ayIFq468AHhAg_t7BmwddQ8JvGbf3DacPf9IBqp4m9cLp0Z3glj5hUa_1WCRnsPqb9DyAvuP_I-1wv7lbrG8oylEmVQjMehfHiy9MFgtzH-60eiNaCgYKARESARESFQF4udJhTx79fMFYmFnSb5pe3zY9ig0163"
}

para = {
    "name":"harrykane.jpg",
    "parents":["1DwDhFvYU5_bEsTEH7zTA3e5LnpHUJmgc"]
}

files = {
    'data':('metadata',json.dumps(para),'application/json;charset=UTF-8'),
    'file':open('/home/pritammandal/Documents/MongoDB-SoftwareEngineeringProject/uploads/1.png','rb')
}

r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)