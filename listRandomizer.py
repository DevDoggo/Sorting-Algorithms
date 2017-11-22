
#RandomizedList

import random
class listRandomizer():
    randomList = []
    def __init__(self):
        print("List-Randomizer has been created.")

    def getList(self, listSize):
        for i in range(0, listSize):
            self.randomList.append(random.randint(0, listSize))
        return self.randomList

