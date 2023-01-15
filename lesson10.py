print("#1 - in base of number return name of month")
calendar_list = {
    1: 'January',
    2: 'February',
    3: 'Mart',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


def show_month(num):
    result = int(num)
    try:
        print(num, "is", calendar_list[num])
    except KeyError as exp:
        print("KeyError: your inserted number is: ", exp, ". Number should be between 1 and 12")


try:
    show_month(int(input("Insert number of month to see its name ")))
except ValueError:
    print("ValueError: inserted value should have a numerical type not a word ")

print('--------------------------------------------------------------------------')
print()
print("#2 - doubles in the list")
def check_unique_numbers(my_list):
    # adjusted list
    list_adjusted = []

    # list with non number elements
    l3 = []

    try:
        for item in l:
            list_adjusted.append(float(item))
    except ValueError as ve:
        print()
        print(ve)
        print(
            "!ERROR: in list, loaded by user, at least one element is not a number or its type isn`t correct - ask to review the list")
    except Exception as e:
        print(e)
    finally:
        for item in l:
            if type(item) != float and type(item) != int:
                l3.append(item)
            else:
                if type(item) == float or type(item) == int:
                    list_adjusted.append(float(item))

    unique_numbers = []
    not_unique_numbers = []

    for item in list_adjusted:
        if item not in unique_numbers:
            unique_numbers.append(item)
        else:
            not_unique_numbers.append(item)

    if len(not_unique_numbers) > 0:
        print("not unique numbers from adjusted user list are: ", not_unique_numbers)
    else:
        print("all numbers are unique")

    # print("list of elements should be adjusted : ",  l3)


l = ["six", 3, 3.5, 5, 7, "8", "fifth", 3, -3, 7]

check_unique_numbers(l)

print('--------------------------------------------------------------------------')
print()
print("#3 - own exception through 'raise'")
class IncomeLowerThanMinimumError(Exception):
    def __init__(self,income, message):
        self.declared_income = income
        self.message = message

    def __str__(self):
        print('Error: declared income {} is lower than minimum in the country (6700)'.format(self.declared_income))
        return 'IncomeLowerThanMinimumError has been raised'

declared_income = float(input("Declare your income: "))
try:
    if declared_income < 6700.00:
        raise IncomeLowerThanMinimumError(declared_income, "smth is wrong with inserted income value")
    else:
        print("Income has passed its first check")
except IncomeLowerThanMinimumError as error:
    print(error)
