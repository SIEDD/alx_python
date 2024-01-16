import MySQLdb
from sys import argv

if __name__ == "__main__":
    
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE id = 3"
    cursor.execute(query)

    row = cursor.fetchone()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
