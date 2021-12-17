import pymysql
import csv

#This code is just for a one-time-use code
#This code is to transfer csv data to mysql

conn = pymysql.connect(host='localhost', user='root', password='060600', db='elice_library', charset='utf8')
curs = conn.cursor()
sql = """insert into book (title, publisher, publication_date, page, isbn, description, link, copies_owned, present_owned) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
sql2 = """insert into author (author_name) values (%s)"""

# # run this code first and then comment these out again
# f = open('new_elice_book_info.csv', 'r', encoding='utf-8-sig')
# rd = csv.reader(f)
# for line in rd:
#     curs.execute(sql, (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]))
#     # print(line)
# conn.commit()
# conn.close()
# f.close()


# # run this code after the first one and then comment these out again
# f2 = open('new_elice_book_info_authors.csv', 'r', encoding='utf-8-sig')
# rd2 = csv.reader(f2)
# for line in rd2:
#     curs.execute(sql2, (line[1],))
# conn.commit()
# conn.close()
# f2.close()


'''
modify table
ALTER TABLE table_name MODIFY column_name DATE;   column의 datatType을 DATE로 바꾸기
ALTER TABLE table_name MODIFY column_name VARCHAR(200) NOT NULL DEFAULT default_value;
data 최솟값 조건 걸려면 check
ALTER TABLE table_name ADD CONSTRAINT any_given_name CHECK(조건);
ALTER TABLE table_name ADD CONSTRAINT any_given_name CHECK(relationship in (‘wife’, ‘husband’, ‘child’));

constraint 확인하는 방법
SELECT * FROM table_name.TABLE_CONSTRAINTS WHERE table_name = ‘department’
ALTER TABLE department DROP constraint_to_drop(i.g. FOREIGN KEY) the_given_name_when_u_apply_the_constraint


alter table book add constraint check_more_than_10_words check (length(isbn) = 10 or length(isbn) = 13); 이걸로 isbn 9자 초과할 때만 입력하게 함
'''