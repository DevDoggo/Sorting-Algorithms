



from listRandomizer import listRandomizer
lR = listRandomizer()

class InsertionSorter():
    def __init__(self):
        pass
        
    def sortList(self, inputList):
        if len(inputList) <= 1:
            return inputList
       
        for j in range(1, len(inputList)):
            key = inputList[j] 
            i = j-1
            while key < inputList[i] and i >= 0:
                inputList[i+1] = inputList[i]
                i = i-1
            inputList[i + 1] = key
        return inputList



printout = ""
while True:
    x = input("Input Array Size [int]: ")
    try:
        newList = lR.getList(int(x))
        insSorter = InsertionSorter()
        printout = str(insSorter.sortList(newList))
        break

    except:
        print("The input given is invalid.")
        continue
    
print("\n" + printout + "\n")
