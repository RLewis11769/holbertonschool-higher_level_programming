#!/usr/bin/python3

""" Print all states starting with 'N' """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE ASCII(left(name, 1)) LIKE ASCII('N');"
    cursor.execute(sql)
    data = cursor.fetchall()

    for entry in data:
        print(entry)
