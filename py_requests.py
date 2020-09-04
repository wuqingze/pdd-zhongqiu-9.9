import requests

url = 'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=171543855464'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
print(response.content)
