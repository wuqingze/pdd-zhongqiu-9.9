import requests
import threading

urls = {
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=168990652045',
    'https://mobile.yangkeduo.com/spike.html?_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=ffffff&__rp_name=spike_super_list&spike_channel=99cmldy',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170828195525',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170470818131',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=120910437168',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=171702158003',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=138674233704',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170939476364',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=171688354776',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146337333706',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=164637149471',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146181908747',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=153486220783',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=4826641614',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=61108215691',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=128353504925',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=167164925411',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=128345909982',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146200367667',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146141063973',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=159211885655',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=134639026879',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=142373478863',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=83065615344',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=129263460010',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=78321634578',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=154113690395',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=169779040354',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=145563917976',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=145315585024',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=98701470585',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=149996936167',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=145849112707',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=148163823632',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=120717296896',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=164673438700',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=163673065067',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146208470819',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=153667510784',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=171589031196',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=164594045546',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170174394280',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=147102355231',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=98292332021',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=159148492049',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=23469130',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146642889913',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=145843516788',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=147285681428',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146664945201',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=131156173412',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146213265713',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146138472493',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146113076405',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=147051494917',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=150443336712',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146100241691',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=101907687584',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=144695323457',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=154020962928',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=153502191621',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=153658595991',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=153623545297',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=132437812435',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170548083987',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=154926153410',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=153374259610',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=159421745700',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=155992970988',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=153665362742',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=158745658403',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=158752532550',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=159427059447',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=159447052103',
    'http://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170905303083',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=160576708354',
    'http://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170405776725',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=146168077215',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=161866688230',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=159127553801',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=156741938415',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=171618071506',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=164576813542',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=478987331',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=164562966057',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=165545349508',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=164335035074',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170524408107',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=111346968882',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=166222229523',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=150516856605',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=153613247900',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=165156253484',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170910947417',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170819652211',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170814896970',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=171503096987',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170812803870',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170881026689',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=171496295648',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170952643923',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=170089837075',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=171543855464',
    'https://mobile.yangkeduo.com/pincard_appointment_buy.html?type=39&_pdd_fs=1&_pdd_tc=ffffff&_pdd_sbs=1&_pdd_nc=1D0A42&subject_id=172483922811'
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def fix(n):
    if n<10:
        return '00'+str(n)

    if n<100:
        return '0'+str(n)

    return str(n)

cnt = 1
def process(url):
    global cnt
    print(url)
    response = requests.get(url, headers=headers)
    #path = './urls-response/'+str(cnt)
    path = './urls-response/'+fix(cnt)
    f = open(path, 'w')
    f.write(response.content.decode())
    f.close()
    print(cnt, response)
    cnt += 1

for url in urls:
    process(url)
#    t = threading.Thread(target=process, args=(url,))
#    t.start()

