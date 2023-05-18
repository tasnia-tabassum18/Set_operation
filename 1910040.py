def Union(s1):
    splitStr = s1.split(' ')
    first = splitStr[0]
    last = splitStr[-1]

    if last == 'empty' and first == 'empty':
        return 'empty'
    elif last == 'empty':
        return splitStr[0]
    elif first == 'empty':
        return last
    for w in last:
        if w not in first:
            first += w

    return first


def Intersection(s2):
    splitStr = s2.split(' ')
    first = splitStr[0]
    last = splitStr[-1]
    new = ""
    if first == 'empty':
        return 'empty'
    elif last == 'empty':
        return 'empty'
    for w in last:
        if w in first:
            new += w

    return new


def Difference(s3):
    splitStr = s3.split(' ')
    first = splitStr[0]
    last = splitStr[-1]

    new = ""

    for w in last:
        if w in first:
            new += w

    new2 = ""
    for w in first:
        if w not in new:
            new2 += w

    return new2


inp = input()

while inp != 'X':
    if "U" in inp:
        print(Union(inp))
    elif "I" in inp:
        print(Intersection(inp))
    else:
        print(Difference(inp))
    inp = input()