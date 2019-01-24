#Courier management system

"""A sample code which is used to modify the data in the database(.db)
using sqlite3 library in python."""

import sqlite3
import sys
#For connecting the database
try:
    cms=sqlite3.connect('CNSS.db')

except sqlite3.OperationalError as e:
    print("Operational Error has occoured while connecting! with a message:")
    print(e)
    sys.exit()
#Returns a Cursor object which uses this Connection
cur=cms.cursor()

while True:
    #Menu
    print("-------------------------")
    print("Courier Management System")
    print("1.Sender")
    print("2.Employee")
    print("3.Package")
    print("4.WareHouses")
    print("5.Courier Office")
    print("6.LogBook")
    print("7.Logout")
    print("-------------------------")
    n=int(input("Enter your choice:"))
    print("-------------------------")

    #Sender
    if n==1:
        print("1.Insert the sender details")
        print("2.Retrieve sender details")
        print("3.Retrieve details of all the senders")
        print("4.Delete the details of a particular sender")
        y=int(input("Enter your choice:"))

        # Used for deleting a record of particular user
        if y==4:
            u=int(input("Enter the sid of the sender"))
            sql10 = "DELETE from sender WHERE sid="+str(u)+";"
            cur.execute(sql10)
            cms.commit()
            print("Deleted the records of sid="+str(u))
        #Retrieve All
        if y==3:
            sql7 = "SELECT * FROM sender;"
            # Execute fun used to run the sql command internally
            cur.execute(sql7)
            while True:
                #Retrieves one result row for the query that was executed on that cursor
                se = cur.fetchone()
                if se == None:
                    break
                print(se)
        #Retrieve particular data
        if y==2:
            z = int(input("Enter the sender id :"))
            sql8 = "SELECT * FROM sender WHERE sid=" + str(z)
            cur.execute(sql8)
            while True:
                send = cur.fetchone()
                if send == None:
                    break
                print(send)
        #Insert the data
        if y==1:
            nam = input("Enter the name of sender :")
            sid = int(input("Give an id :"))
            phnum = int(input("Enter the phone no. :"))
            sadd = input("Enter the address of sender :")
            cur.execute("INSERT INTO sender (sname,sid,sph_no,sadd) VALUES (?,?,?,?);",
                        (nam, sid, phnum, sadd))
            #Used for modifying the data
            cms.commit()
            print("All the sender details were successfully inserted into the database")

    #Employee
    if n==2:
        print("1.Add an employee")
        print("2.Retrieve employee details:")
        print("3.Retrieve details of all the employees")
        k=int(input("Enter your choice:"))

        if k==3:
            sql4 = "SELECT * FROM emp;"
            cur.execute(sql4)
            while True:
                #retrieves one result row for the query that was executed on that cursor
                empl = cur.fetchone()
                if empl == None:
                    break
                print(empl)

        if k==2:
            i = int(input("Enter the employee id :"))
            sql5 = "SELECT * FROM emp WHERE eid=" + str(i)
            cur.execute(sql5)
            while True:
                em = cur.fetchone()
                if em == None:
                    break
                print(em)

        if k==1:
            name = input("Enter the name of employee: ")
            eid = int(input("Give an ID :"))
            cd = int(input("Enter the id of courier office"))
            empsal = int(input("Enter the salary :"))
            cur.execute("INSERT INTO emp (ename,eid,cid,emp_sal) VALUES (?,?,?,?);",
                        (name, eid, cd, empsal))
            cms.commit()
            print("All the employee details were successfully inserted into the database")

    #Package
    if n==3:
        print("1.Insert")
        print("2.Retrieve a package details")
        print("3.Retrieve details of all the packages")
        print("4.Delete the details of a particular package")
        j=int(input("Enter your choice:"))

        if j==4:
            h=int(input("Enter the package id(pid)"))
            sql11 = "DELETE FROM package WHERE pid="+str(h)
            cur.execute(sql11)
            cms.commit()

        if j==1:
            sid=int(input("Enter the sender id :"))
            cid=int(input("Enter the courier office id :"))
            pid=int(input("Enter the package id :"))
            add=input("Enter receiver's address : ")
            ph=input("Enter receiver's phone no. :")
            amt=int(input("Billing amount :"))
            status=input("Enter the billing status :")
            cur.execute("INSERT INTO package (sid,cid,pid,radd,rph,bill_amt,b_status) VALUES (?,?,?,?,?,?,?);",(sid,cid,pid,add,ph,amt,status))
            cms.commit()
            print("All the package details were successfully inserted into the database")

        if j==2:
            x=int(input("Please enter the sender ID:"))
            sql3 = "SELECT * FROM package WHERE sid="+str(x)
            cur.execute(sql3)
            while True:
                package = cur.fetchone()
                if package == None:
                    break
                print(package)

        if j==3:
            sql6 = "SELECT * FROM package;"
            cur.execute(sql6)
            while True:
                pk = cur.fetchone()
                if pk == None:
                    break
                print(pk)

    #Warehouse
    if n==4:
        sql2 = "SELECT * FROM cgodown;"
        cur.execute(sql2)
        print("------------------")
        while True:
            warehouse = cur.fetchone()
            if warehouse == None:
                break
            print(warehouse)

    #Courier Office
    if n==5:
        sql = "SELECT * FROM coffice;"
        #Execute fun used to run the sql command internally
        cur.execute(sql)
        while True:
            #Retrieves one result row for the query that was executed on that cursor
            office = cur.fetchone()
            if office == None:
                break
            print(office)

    #Logbook
    if n==6:
        a=int(input("Enter the sid of the sender"))
        sql9 = "SELECT * FROM logbook WHERE sid="+str(a)
        cur.execute(sql9)
        while True:
            log = cur.fetchone()
            if log == None:
                break
            print(log)

    #Logout
    if n==7:
        print("Hand it to us, we're good  :)")
        break
#End of the program