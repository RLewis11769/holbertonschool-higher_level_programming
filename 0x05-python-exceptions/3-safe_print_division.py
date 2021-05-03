"""
safe_print_list_division - prints result of division
a - first integer (to be divided)
b - second integer (to divide)
Return: result of division
"""
def safe_print_division(a, b):
    try:
        div = a / b
        print("Inside result: {:.1f}".format(div))
        return div
    except ZeroDivisionError:
        print("Inside result: None")
        return None
