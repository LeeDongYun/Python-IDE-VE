import sqlite3
con = sqlite3.connect("c:/work/company.db")
cur = con.cursor()

cur.execute("CREATE TABLE emp(empid text, name text, phonenum text, depid text);")
cur.execute("CREATE TABLE dep(depid text, name text, phonenum text);")



cur.execute("INSERT INTO "emp" VALUES("1000","김철수","010-1111-1111","100"),
    ("1001","김안나","010-2222-2222","200"), ("1002","박호두","010-3333-3333","300"),
    ("1003","김지수","010-4444-4444","400");")

cur.execute("INSERT INTO dep VALUES("400","다니엘","010-1234-5678"),("300","조나단","010-");")

#list =(("1000","김철수","010-1111-1111","100"),("1001","김안나","010-2222-2222","200"), ("1002","박호두","010-3333-3333","300"),("1003","김지수","010-4444-4444","400"))
#cur.executemany("insert into PhoneBook values(?,?);",list)
#cur.execute("update PhoneBook set PhoneNum='010-1234-1235' where Name='BB';")
#cur.execute("delete from PhoneBook where Name ='CC;'")
con.commit

cur.execute("select * from PhoneBook")
for row in cur:
    print(row)

for l in con.iterdump():
    print(l)