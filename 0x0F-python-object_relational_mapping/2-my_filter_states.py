#!/usr/bin/python3

""" Prints all states matching argv[4] """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(argv[4]))

    data = cursor.fetchall()

    for entry in data:
        print(entry)
