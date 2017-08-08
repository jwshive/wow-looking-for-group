import json
import ast
from base64 import b64encode, b64decode

# ENCODE JSON
ENCODING = 'utf-8'

# Convert JSON to base64
with open('group.json', 'r') as json_stuff:
    test_data = str(json.loads(json_stuff.read())).encode()


base64_bytes = b64encode(test_data)
print(base64_bytes)

base64_string = base64_bytes.decode(ENCODING)
print(base64_string)



# DECODING BASE64
json_data = json.loads(b64decode(base64_string).decode(ENCODING).replace('\'', '"'))

requesting_member_name = json_data['request']['requesting-member-name']
requesting_member_realm = json_data['request']['requesting-member-realm'] 

print(json_data)
