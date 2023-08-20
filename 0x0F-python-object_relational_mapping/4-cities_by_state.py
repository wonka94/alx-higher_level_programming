#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get all cities.
    """
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC""", {
            'name': argv[4]
        })

        result = cur.fetchall()

    for row in result:
        print(row)
