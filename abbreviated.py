def abbrev_name(name):
    nameList = name.upper().split(" ")
    firstInitial = nameList[0][0]
    secondInitial = nameList[1][0]
    return firstInitial + '.' + secondInitial