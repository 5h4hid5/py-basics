#List
oddNum = [1,3,5,7,9,11]
print(oddNum)
print('\n')

#Access specific item
numSeven = oddNum[3]
print(numSeven)
print('\n')

#Update item value : -1 to access last item
oddNum[-1] = 17
print(oddNum)
print('\n')

#Add new item to list
oddNum.append(19)
print(oddNum)
print('\n')

#Slice list
newOddNum = oddNum[0:-2]
print(newOddNum)
print('\n')

#Update multiple values
newOddNum[0:2] = [17,29]
print(newOddNum)
print('\n')
#Remove multiple values
newOddNum[0:2] = []
print(newOddNum)
print('\n')

#Remove all items
newOddNum[:] = []
print(newOddNum)
print('\n')
