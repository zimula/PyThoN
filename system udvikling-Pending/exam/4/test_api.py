'''
- must import requests library in order to use apis.
Testing api
- reponse
- data
- https://todo.pixegami.io/
- 
'''
import requests

ENDPPOINT = "https://todo.pixegami.io/"
response = requests.get(ENDPPOINT)
print(response)