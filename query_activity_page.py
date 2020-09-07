import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = 'https://mobile.yangkeduo.com/luxury_spike.html?_wv=41729&_wvx=10&id=143534&subject_id=&type=47&refer_share_id=7w3gqdrutsr1ns1g068xepflpmn6hilo&refer_share_uid=4935443353500&refer_share_uin=RNORJ7PISN75P3PEBVM4LI2SHY_GEXDA&refer_share_channel=copy_link'

response = requests.get(url, headers=headers)
f = open('activity_page.data', 'w')
f.write(response.content.decode())
print(response.content.decode()) 
f.close()

f = open('activity_page.data', 'r')
line = f.readlines()[35]
print(line[39:-62])
