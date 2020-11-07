def createList(string):
    List = []

    for i in string:
        List.append(i)
    return List

def createString(List):
    return ''.join(List)

def no_dups(s):
    # Your code here
    hash = [0] * 512
    input_index = 0
    res_index = 0
    temp = ''
    mutatedString = createList(s)

    while input_index != len(mutatedString):
        temp = mutatedString[input_index]
        if hash[ord(temp)] == 0:
            hash[ord(temp)] = 1
            mutatedString[res_index] = mutatedString[input_index]
            res_index += 1
        input_index += 1

    return createString(mutatedString[0:res_index])
    """
    string = s.split()
    arr = []
    for word in string:
        if(s.count(word) > 1 and (word not in arr) or s.count(word) == 1):
            arr.append(word)

    return ' '.join(arr)
    """

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))