#!/usr/bin/python3

""" Print all data from states """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()

    sql = "SELECT * FROM states;"
    cursor.execute(sql)
    data = cursor.fetchall()

    for entry in data:
        print(entry)
