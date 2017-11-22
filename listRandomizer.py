
#RandomizedList

import random
class listRandomizer():
    randomList = []
    def __init__(self):
        print("\nList-Randomizer has been created.")

    def getList(self, listSize, lowerBound = 0, upperBound = 100000):
        if listSize < 1:
            print("\nInvalid input!\n")
            return
        for i in range(0, listSize):
            self.randomList.append(random.randint(lowerBound, upperBound))
        return self.randomList

