#!/usr/bin/python3
"""
script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb as mysql
import sys
if __name__ == "__main__":
    dbconnect = mysql.connect(host="localhost",
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              port=3306)
    cur = dbconnect.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print("(%d, '%s')" % (row[0], row[1]))
    cur.close()
    dbconnect.close()
