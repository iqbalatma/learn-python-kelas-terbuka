#list
listOfNumbers = [1,2,5,1,6,8]

for number in listOfNumbers:
    print(f"number = {number}")

lengthOfList = len(listOfNumbers)

for i in range(lengthOfList):
    print(f"number = {listOfNumbers[i]}")


while i < lengthOfList:
    print(f"number = {listOfNumbers[i]}")
    i+=1;


for index,number in enumerate(listOfNumbers):
    print(f"index = {index} number = {number}")