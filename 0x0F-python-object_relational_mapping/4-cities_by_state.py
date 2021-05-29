#!/usr/bin/python3

""" Prints all states matching argv[4] """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    with db.cursor() as cursor:
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id")
        data = cursor.fetchall()

        for entry in data:
            print(entry)
