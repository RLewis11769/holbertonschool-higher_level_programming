"""
list_division - divides one list by another
my_list_1 - first list (to be divided)
my_list_2 - second list (to divide)
list_length - length of list
Return: new list including results of division
"""
def list_division(my_list_1, my_list_2, list_length):
        new_list = []
        for val in range(list_length):
                try:
                        div = (my_list_1[val] / my_list_2[val])
                except ZeroDivisionError:
                        print("division by 0")
                        div = 0
                except IndexError:
                        print("out of range")
                        div = 0
                except TypeError:
                        print("wrong type")
                        div = 0
                finally:
                        new_list.append(div)
        return new_list
