import pymysql


try:
    dbcon=pymysql.connect(host='127.0.0.1',user='root',password='',database='topsdb')
    print("Database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

#Table Create
create_tbl="create table studinfo(id integer primary key auto_increment,name text,sub varchar(20))"
try:
    cr.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('mitesh','php'),('ashok','java'),('hitesh','html'),('prasiddh','c++')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

"""n=int(input("Enter number of student's data:"))

for i in range(n):
    nm=input("Enter your name:")
    sub=input("Enter your Subject:")
    insert_data=f"insert into studinfo(name,sub)values('{nm}','{sub}')"

    try:
        cr.execute(insert_data)
        dbcon.commit()
        print("Record Inserted!")
    except Exception as e:
        print(e)"""


# Update Data
"""update_data="update studinfo set name='amit',sub='angular' where id=11"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""


# Delete Data
"""delete_data="delete from studinfo where id=14"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


# Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(4)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i)
except Exception as e:
    print(e)













