import math

# ex. 1
def symbols_count(str):
    if len(str) > 20:
        return

    return len(list(str))

# print(symbols_count("aabbbbss"))

# ex. 2
def anagrama(str1,str2):
    if len(str1) > 20 or len(str2)>20:
        return
    
    def sortLetters(str):
        return "".join(sorted(str))
    return "Yes" if sortLetters(str1) == sortLetters(str2) else "No"
   
# print(anagrama("abcEcba", "aabcEcb"))

# ex. 3
def palindrom(str):
    # way 1
    return "Yes" if str == str[::-1] else "No"

    # way 2
    for i in range(len(str)//2):
        if str[i] != str[-1*(i+1)]:
            return "No"
    return "Yes"

# print(palindrom("abcEcba"))

#  ex. 4
def customSplit(str,letter):
    letterIndex=str.index(letter)
    return str[letterIndex+1:]

# print(customSplit("abcdefghlmnop", "f"))

# ex. 5
def subword(s1, s2):
    if len(s1)>20 or len(s2)>len(s1):
        return
    
    return "Yes" if s1.index(s2) else "No"

# print(subword("abcdefg", "efg"))

# ex. 6
def evenNumbersCount():
    n=input("Enter count of elements: ")
    elements=[int(input("Enter item: ")) for _ in range(int(n))]
    evenElems=list(filter(lambda x:x%2==0, elements))
    return len(evenElems)

# print(evenNumbersCount())

# ex. 7
def getDuplicatedElements():
    n=input("Enter count of elements: ")
    elements=[int(input("Enter item: ")) for _ in range(int(n))]
    duplicated=[]
    temp=[]
    for i in elements:
        if i in temp and i not in duplicated:
            duplicated.append(i)
        else:
            temp.append(i)
    return duplicated

# print(getDuplicatedElements())

# ex. 8
def longestSequence():
    n=input("Enter count of elements: ")
    elements=[int(input("Enter item: ")) for _ in range(int(n))]

    bestSolution=0
    currentSize=0
    for i in range(len(elements)):
        if i==0:
            continue
    
        if elements[i-1] < elements[i]:
            currentSize +=1
        else:
            bestSolution=max(bestSolution, currentSize) 
            currentSize=0

    return bestSolution+1

# print(longestSequence())


# ex. 9
def reapitedCount():
    n=input("Enter count of elements: ")
    elements=[int(input("Enter item: ")) for _ in range(int(n))]

    repeatedObj={}
    for i in elements:
        item=str(i)
        if item in repeatedObj:
            repeatedObj[item] += 1
        else:
            repeatedObj[item] = 1
    return list(repeatedObj.values())

# print(reapitedCount())

# ex. 10
def theClosestCoupletoZero():
    n=input("Enter count of elements: ")
    elements=[int(input("Enter item: ")) for _ in range(int(n))]

    bestSolution=math.inf
    items=[]
    for i in range(len(elements)):
        for j in range(len(elements)):
            if i==j: continue

            if abs(elements[i] + elements[j])<bestSolution:
                bestSolution=abs(elements[i] + elements[j])
                items=[elements[i], elements[j]]
    return f"the smallest value is {bestSolution}, and items are {items}"
      

# print(theClosestCoupletoZero())