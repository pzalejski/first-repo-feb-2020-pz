# Prework Question 1
def display_name(name):
    print(name)

# display_name("Peter")


# Prework Question 2 - print 100 odd numbers
def print_odd():
    for num in range (0, 100):
        if num % 2 != 0:
            print(num)

# print_odd()

# Prework Question 3 - Find max in a list
def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max

my_list = [1, 2, 3, 6, 8, 12]

# max_num_in_list[

#Prework Question 4 - Fucntion returns leap year
def is_leap(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        print('True')
    else:
        print('False')


#Question 5

def is_consecutive(a_list):
    total = 2
    while total > 1:
        test = a_list.pop(0)
        if test == a_list[0] - 1:
            total = len(a_list)
        else:
            return False
    return True

is_consecutive([1,2,3,4,5,7,6])

def isconsec(a_list):
    for i in range(1, len(a_list)):
        if a_list[i] - 1 != a_list[i:-1]
            return False
    return True