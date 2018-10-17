import json
import requests, base64
import os                             # Allows for the clearing of the Terminal Window
import time, datetime
import glob
import getpass
# -*- coding: utf-8 -*-


italyListusers =   [] 

###  Define the API Arguments, and choose if you need a folder or not

import sys
if (3,0) <= sys.version_info < (4,0):
    import http.client as httplib
elif (2,6) <= sys.version_info < (3,0):
    import httplib

headers = {
    "Authorization": "Bearer TOKENHERE",
    "Content-Type": "application/json"
}
for i in range(len(italyListusers)):
    params = {
        "shared_folder_id": "123456",
        "member": {".tag":"email","email":italyListusers[i]},
        "access_level": {".tag":"viewer"}
    }
    c = httplib.HTTPSConnection("api.dropboxapi.com")
    c.request("POST", "/2/sharing/update_folder_member", json.dumps(params), headers)
    r = c.getresponse()
    print(str(r.status) + " " + r.read() + "for email: " + italyListusers[i])
###  API responses, first if an error occurs for reporting and second to show the new doc URL


###  API responses, first if an error occurs for reporting and second to show the new doc URL

    
    