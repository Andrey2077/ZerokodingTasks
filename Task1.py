

#Сложность О в квадрате
def lists():
    a = [1,1,2,3,5,8,13,21,34,55,89]
    #seta = set(a)
    b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    result = []

    for i in a:
        for j in b:
            if i == j:
                if not i in result:
                    result.append(i)

    print(result)


#Сложность O(n+m)
def lists2():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    setA = set(a)
    result = [element for element in b if element in setA]
    print(result)
 
lists2()