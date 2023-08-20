#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    where name matches the argument.
    """
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT * FROM statesWHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC""", {
            'name': argv[4]
        })

        result = cur.fetchall()

        for row in result:
            print(row)
