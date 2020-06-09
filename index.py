import requests

req = requests.post("http://thwebsite/path/", headers={"content-type":"application/x-www-form-urlenc", "Auth":"084e0343a0486ff05530df6c705c8bb4"}, data={"flag":"true"})