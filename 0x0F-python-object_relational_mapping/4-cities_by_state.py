#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
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
    query = """SELECT c.id, c.name, s.name FROM states s JOIN
    cities c ON s.id=c.state_id ORDER BY c.id"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print("(%d, '%s', '%s')" % (row[0], row[1], row[2]))
    cur.close()
    dbconnect.close()
