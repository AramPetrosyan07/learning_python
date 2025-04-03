# Թվաբանություն և ճյուղավորում 11-13, 25

# enter 2 number and check if there is equal return "Yes" if not so return "No
def is_equal():
    first_inp = input("")
    second_ing = input("")
    if first_inp == second_ing:
        return "Yes"
    else:
        return "No"

# print(is_equal())

# enter 2 number and return the biggest of them
def the_max():
    first_inp = input("")
    second_ing = input("")
    if first_inp > second_ing:
        return f"the biggest value is -> {first_inp} "
    elif first_inp < second_ing:
        return f"the biggest value is -> {second_ing} "
    else:
        return "equal"

# print(the_max())

# enter 3 number and return the smallest of them
def the_min():
    inputs=[]
    for i in range(3):
        inpVal=int(input("Enter a number: "))
        inputs.append(inpVal)
    inputs.sort()
    print(inputs)
    return inputs[0]

# print(the_min())

# enter x number and if it is - number, I must return that number but +
# way 1
def make_number_positive():
    inp=int(input("Enter a number: "))
    return abs(inp)


# way 2
def make_number_positive2():
    inp=int(input("Enter a number: "))
    if inp<0:
        return -inp
    else:
        return inp

# print(make_number_positive2())