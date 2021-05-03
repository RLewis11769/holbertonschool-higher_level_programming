"""
safe_print_list_integers - prints first x elements of a list if integer
my_list - list of elements of any type
x - number of elements to print
Returns: number of integers printed
"""
def safe_print_list_integers(my_list=[], x=0):
    if my_list:
        count = 0
        for val in range(x):
            try:
                if isinstance(val, int):
                    print("{:d}".format(my_list[val]), end="")
                    count += 1
            except (TypeError, ValueError):
                print("", end="")
        print()
        return count
