import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    mysql_database = argv[3]
    state_name = argv[4]
    connect = MySQLdb.connect(host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database)
    cursor = connect.cursor()
    query = """SELECT cities.name FROM cities INNER JOIN states ON cities.states_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"""
    cursor.execute(query,(state_name,))
    rows = cursor.fetchall()
    cities = [row[0]for row in rows]
    print(", ".join(cities))
    cursor.close()
    connect.close()


