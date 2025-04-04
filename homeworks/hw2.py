
def divide7():
    inp=int(input("Enter a number: "))
    if inp % 2 ==0:
        if inp%7==3:
            return f"Yes {inp}"
        else:
            return "No"
    else:
        return "No"

# print(divide7())


def the_middle():
    inputs=[]
    for i in range(3):
        inpVal=int(input("Enter a number: "))
        inputs.append(inpVal)
    inputs.sort()
    print(inputs)
    return inputs[1]

# print(the_middle())


def ascii():
    inputs=[]
    for i in range(2):
        inpVal=input("Enter a number: ")
        inputs.append(inpVal)

    if ord(inputs[0])<ord(inputs[1]):
        return "Yes"
    else:
        return  "No"

# print(ascii())

def interval():
    inputs=[]
    for i in range(3): # A B C
        inpVal=input("Enter a number: ")
        inputs.append(inpVal)

    if inputs[0]>=inputs[1] and inputs[0]<inputs[2]:
        return "Yes"
    else:
        return  "No"

# print(interval())


def isGrowing():
    inputs=[]
    for i in range(4): 
        inpVal=int(input(f"Enter the {i}th number: "))
        inputs.append(inpVal)
        if i==0:
            continue
        elif inpVal<inputs[i-1]:
            return "No"
        
    return "Yes"

# print(isGrowing())

from functools import reduce

def unusualProblem():
    inputs=[]
    for i in range(4): #abcd
        inpVal=int(input(f"Enter the {i}th number: "))
        inputs.append(inpVal)

    if inputs[0] > inputs[2]:
        return (inputs[0]*inputs[3]) / (inputs[1]+inputs[2])
    elif inputs[0] == inputs[2]:
        # I don't want to write simple method (sum) :)
        return  reduce(lambda acc, curr: acc + curr, inputs)
    else:
        return (inputs[1]+inputs[3]) * (inputs[0])
    

# print(unusualProblem())

def unusualProblem():
    inputs=[]
    for i in range(4): #abcd
        inpVal=int(input(f"Enter the {i}th number: "))
        inputs.append(inpVal)

    if inputs[0] == -inputs[3] and inputs[1] != -inputs[2]:
        return "Yes"
    else:
        return "No"
    
# print(unusualProblem())


