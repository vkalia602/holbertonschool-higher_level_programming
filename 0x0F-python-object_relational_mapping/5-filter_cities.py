#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of
 that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states
    ON cities.state_id = states.id WHERE states.name=%s""", (sys.argv[4], ))

    query_rows = cur.fetchall()
    cities_list = [row[0] for row in query_rows]
    print(', '.join(cities_list))
    cur.close()
    conn.close()
