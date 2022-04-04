import base64
import json                    

import requests

api = 'http://localhost:8000/detect/api/upload/'
image_file = 'cat-image.jpeg'

with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
  
payload = json.dumps({'label': 'test_label', 'image': im_b64, 'client_secret_key': '7cc25da8-6ace-43e2-80a8-15262d2b8058'})
response = requests.post(api, data=payload, headers=headers)


if response.status_code == 201:
    print('Image Uploaded Successfully')
else:
    print('Something went wrong..')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')

