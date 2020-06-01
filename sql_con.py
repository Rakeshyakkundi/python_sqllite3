import sqlite3
conn = sqlite3.connect('python_pro.db')


i=0
while i != 999:
    num = int(input("\nEnter : 1]Add Student\t2]Delete Student\t 3]Search student\t 4]Print all Students\t 5]Exit\n"))
    if num ==1:
        name = input("Enter student name :")
        USN = int(input('Enter USN :'))
        m1 = int(input("Marks one :"))
        m2 = int(input("Enter Marks two :"))
        m3 = int(input("Enter marks three :"))
        conn.execute(f"INSERT INTO Students  \
            VALUES ('{name}',{USN}, {m1}, {m2}, {m3} )")
        conn.commit()
        print('Data Base is :\n')
        cursor = conn.execute(f"SELECT name,USN,m1,m2,m3 from Students")
        for data in cursor:
            for j in data:
                print(j)
    elif num==2:
        USN = int(input("Enter the USN of the student to delete it :"))
        conn.execute(f'DELETE from Students where USN={USN}')
        conn.commit()
        cursor = conn.execute(f"SELECT name,USN,m1,m2,m3 from Students")
        for data in cursor:
            for j in data:
                print(j)
    elif num ==3:
        USN = int(input("Enter the USN and see the Students detail :"))
        cursor = conn.execute(f"SELECT name,USN,m1,m2,m3 from Students  where USN={USN}")
        for data in cursor:
            print('Name is :',data[0])
            print('USN is :',data[1])
            l = data[2]
            p = data[3]
            k = data[4]
            kit = [l,p,k]
            kit.sort(reverse = False)
            kit.pop(0)
            print("Average Score of two number is :",(kit[0]+kit[1])/2)
    elif num==5:
        print('Bye')
        break
    elif num == 4:
        cursor = conn.execute(f"SELECT name,USN,m1,m2,m3 from Students ")
        for data in cursor:
            for j in data:
                print(j)
    else:
        print('Invalid number')
        break
conn.commit()
conn.close()