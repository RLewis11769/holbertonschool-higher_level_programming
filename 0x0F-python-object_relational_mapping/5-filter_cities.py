#!/usr/bin/python3

""" Prints all cities where state matches argv[4] """

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    with db.cursor() as cursor:
        cursor.execute("""SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %(state)s""",
                       {'state': argv[4]})

        data = cursor.fetchall()

        for x in range(len(data)):
            if x != len(data) - 1:
                print("{}, ".format(data[x][0]), end="")
            else:
                print("{}".format(data[x][0]), end="")
        print()
