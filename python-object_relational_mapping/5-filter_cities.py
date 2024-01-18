# import MySQLdb
# from sys import argv

# if __name__ == "__main__":

#     if len(argv) != 4:
#         print("Usage: {} <username> <password> <database>".format(argv[0]))
#         exit(1)

#     username, password, database = argv[1], argv[2], argv[3]

#     # Connecting to the MySQL server
#     db = MySQLdb.connect(
#         host="localhost",
#         port=3306,
#         user=username,
#         passwd=password,
#         db=database
#     )

#     cursor = db.cursor()

#     query = """SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id """
#     cursor.execute(query)

#     rows = cursor.fetchall()

#     for i, state in enumerate(states):
#         print(state[0], end='')
#         if i < len(states)-1:
#             print(', ', end='')
#     print('')

#     cursor.close()
#     db.close()

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("page, phoenix")
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    # Connecting to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id"""
    cursor.execute(query)

    rows = cursor.fetchall()

    for i, row in enumerate(rows):
        print(f"{row[0]}: {row[1]}, {row[2]}", end='')
        if i < len(rows) - 1:
            print(', ', end='')

    print('')

    cursor.close()
    db.close()

