def vowelCount(str):
    vowel = ('a', 'e', 'i', 'o', 'u')
    vCount = 0
    for i in str.lower():
        if i in vowel:
            vCount = vCount + 1
    return vCount

def uniqueChar(str):
    list = []
    for i in str:
        if i not in list:
            list.append(i)

    return len(list)