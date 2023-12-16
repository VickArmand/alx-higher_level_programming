#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
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
    cur.execute("""SELECT * FROM states WHERE name = '%s'
                ORDER BY states.id""" % (name))
    rows = cur.fetchall()
    for row in rows:
        print("(%d, '%s')" % (row[0], row[1]))
    cur.close()
    dbconnect.close()
