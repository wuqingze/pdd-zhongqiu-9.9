s = open('02_data').read()
import json
list = json.loads(s)['props']['store']['list']
for obj in list:
    if obj['store'].get('imgData', None):
        imgData = obj['store'].get('imgData')[0]
        print(imgData['imgUrl'],imgData['url'],imgData['name']) 
