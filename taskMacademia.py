import unittest

orderQuantity =25 # a value of Product A, which you can change to check, how many boxes you need
boxes = {"smallBoxCapacity": 3,
        "mediumBoxCapacity": 6,
        "bigBoxCapacity": 9}

def howManyAndKindOfBoxes(quantity):
    if quantity >100:
        return "quantity is too large, max 100"
    if  quantity <= 100:
            numberOfMediumBoxes=0
            numberOfSmallBoxes=0
            numberOfBigBoxes = quantity // boxes["bigBoxCapacity"]
            restOf = quantity - numberOfBigBoxes * boxes["bigBoxCapacity"]
            if restOf <  boxes["bigBoxCapacity"] and restOf > boxes["mediumBoxCapacity"]:
                numberOfBigBoxes+=1
            if restOf <=boxes["mediumBoxCapacity"] and restOf > boxes["smallBoxCapacity"]:
                numberOfMediumBoxes += 1
            if restOf <=boxes["smallBoxCapacity"] and restOf > 0:
                numberOfSmallBoxes += 1
         
            sumOfBoxes = (numberOfBigBoxes+numberOfMediumBoxes+numberOfSmallBoxes)
            if sumOfBoxes % 3 ==0:
                collectivePackage =(numberOfBigBoxes+numberOfMediumBoxes+numberOfSmallBoxes)/3
            if sumOfBoxes % 3 !=0:
                collectivePackage =((numberOfBigBoxes+numberOfMediumBoxes+numberOfSmallBoxes)/3) + 1
        

            return ('Big Boxes: ',numberOfBigBoxes,'Medium Boxes :', numberOfMediumBoxes,'Small Boxes ', numberOfSmallBoxes,'collective package:', int(collectivePackage))


print (howManyAndKindOfBoxes(orderQuantity))
