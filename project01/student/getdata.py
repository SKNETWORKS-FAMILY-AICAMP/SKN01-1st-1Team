from urllib import request
import json

def jsonplaceholder():
    target = "https://jsonplaceholder.typicode.com/users"
    result = request.urlopen(target)
    
    return json.load(result) # binary json화 