#!/usr/bin/python3
"""
write a script that takes in arguments and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import MySQLdb as mysql
import sys
if __name__ == "__main__":
    name = sys.argv[4]
    dbconnect = mysql.connect(host="localhost",
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              port=3306)
    cur = dbconnect.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (name,))
    rows = cur.fetchall()
    for row in rows:
        print("(%d, '%s')" % (row[0], row[1]))
    cur.close()
    dbconnect.close()
