lines = open("day1-input.txt").read().splitlines()

elfArray = [[]]
tempArr = []

#formats list
for i in range(len(lines)): 
    
    if lines[i] == '':
        elfArray.insert(i, tempArr)
        tempArr = []
    else:
        tempArr.append(lines[i])

tempElfArray = elfArray
tempArr = []

elfArray = [list( map(int,i) ) for i in elfArray]


#addups all elfs
for i in range(len(elfArray)):
    tempTotal = sum(elfArray[i])
    tempArr.append(tempTotal)

#sorts
tempArr.sort()

#gets top 3
print(tempArr[-1] + tempArr[-2] + tempArr[-3])
