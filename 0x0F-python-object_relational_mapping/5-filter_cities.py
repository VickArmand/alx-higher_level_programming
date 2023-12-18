#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
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
    state_name = sys.argv[4]
    query = """SELECT c.name FROM states s JOIN cities c ON
    s.id=c.state_id WHERE s.name=%s ORDER BY c.id"""
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    if (len(rows) == 0):
        print()
    for row in rows:
        if rows.index(row) == (len(rows) - 1):
            print("%s" % (row[0]))
        else:
            print("%s," % (row[0]), end=" ")
    cur.close()
    dbconnect.close()
