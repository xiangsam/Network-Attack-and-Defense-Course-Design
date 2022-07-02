from os import write


sql_format = 'INSERT INTO movies(movie_id,movie_name,movie_rank,movie_score,movie_picture,movie_year) VALUES ({0[0]},{0[1]},{0[2]},{0[3]},{0[4]},{0[5]});'
director_insert = 'INSERT INTO directors VALUES({0[0]},{0[1]});'
writer_insert = 'INSERT INTO writers VALUES({0[0]},{0[1]});'
actor_insert = 'INSERT INTO actors VALUES({0[0]},{0[1]});'
type_insert = 'INSERT INTO types VALUES({0[0]},{0[1]});'
area_insert = 'INSERT INTO areas VALUES({0[0]},{0[1]});'
movie_director_insert = 'INSERT INTO movie_director VALUE({0[0]},{0[1]});'
movie_writer_insert = 'INSERT INTO movie_writer VALUE({0[0]},{0[1]});'
movie_actor_insert = 'INSERT INTO movie_actor VALUE({0[0]},{0[1]});'
movie_type_insert = 'INSERT INTO movie_type VALUE({0[0]},{0[1]});'
movie_area_insert = 'INSERT INTO movie_area VALUE({0[0]},{0[1]});'

movie_id = []
director_lst = []
writer_lst = []
actor_lst = []
area_lst = []
type_lst = []

def change_to_moviesql(rank,line):
    lst = line.split(' ')
    lst[-1] = str(rank+1)
    name = ' '.join(lst[2:-3])
    lst = [lst[1][2:],'\"'+name+'\"',lst[-1],lst[-2],'\"'+lst[0]+'\"',lst[-3]]
    movie_id.append(lst[0])
    fout.write(sql_format.format(lst)+'\n')

def process_str(s, lst):
    for e in s.split('/'):
        if not e in lst:
            lst.append(e)

def process_csv(line):
    lst = line.split(',')
    director_str = lst[0]
    writer_str = lst[1]
    actor_str = lst[2]
    type_str = lst[3]
    area_str = lst[4]
    process_str(director_str, director_lst)
    process_str(writer_str,writer_lst)
    process_str(actor_str, actor_lst)
    process_str(type_str, type_lst)
    process_str(area_str, area_lst)

def process_lst():
    for i, e in enumerate(director_lst):
        fout.write(director_insert.format([i+1, '\"'+e+'\"'])+'\n')
    for i, e in enumerate(writer_lst):
        fout.write(writer_insert.format([i+1, '\"'+e+'\"'])+'\n')
    for i, e in enumerate(actor_lst):
        fout.write(actor_insert.format([i+1, '\"'+e+'\"'])+'\n')
    for i, e in enumerate(area_lst):
        fout.write(area_insert.format([i+1, '\"'+e+'\"'])+'\n')
    for i, e in enumerate(type_lst):
        fout.write(type_insert.format([i+1, '\"'+e+'\"'])+'\n')

def change_to_sql(index, line):
    lst = line.split(',')
    director_l = list(set(lst[0].split('/')))
    writer_l = list(set(lst[1].split('/')))
    actor_l = list(set(lst[2].split('/')))
    type_l = list(set(lst[3].split('/')))
    area_l = list(set(lst[4].split('/')))
    for e in director_l:
        fout.write(movie_director_insert.format([movie_id[index], director_lst.index(e)+1])+'\n')
    for e in writer_l:
        fout.write(movie_writer_insert.format([movie_id[index], writer_lst.index(e)+1])+'\n')
    for e in actor_l:
        fout.write(movie_actor_insert.format([movie_id[index], actor_lst.index(e)+1])+'\n')
    for e in type_l:
        fout.write(movie_type_insert.format([movie_id[index], type_lst.index(e)+1])+'\n')
    for e in area_l:
        fout.write(movie_area_insert.format([movie_id[index], area_lst.index(e)+1])+'\n')
    


if __name__ == '__main__':
    fout = open('movie_inset.sql','w',encoding='utf-8')
    with open('data.txt','r',encoding='utf-8') as f:
        for index, line in enumerate(f):
            change_to_moviesql(index,line[:-1])
        f.close()
    fout.write('\n\n\n')
    with open('detail.csv','r',encoding='utf-8') as f:
        for line in f:
            if line == '\n':
                continue
            process_csv(line[:-1])
        f.close()
    process_lst()
    fout.write('\n\n')
    with open('detail.csv','r',encoding='utf-8') as f:
        i = 0
        for line in f:
            if line == '\n':
                continue
            change_to_sql(i, line[:-1])
            i+=1
        f.close()
    fout.close()
