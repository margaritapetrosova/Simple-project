def supervised(animal):
    if animal.wings == 'No' and animal.legs == 4 and animal.niceears == 'Yes':
        print('The animal has not wings, may be it is dog, pig, or cow')
    else:
        print('The animal has wings, it is bird')


class animal:
    def __init__(self, theLegs, theWings, theNiceEars):
        self.legs = theLegs
        self.wings = theWings
        self.niceears = theNiceEars


cow = animal(4, 'No', 'Yes')
penguin = animal(2, 'Yes', 'No')
dog = animal(4, 'No', 'Yes')

supervised(cow)
supervised(penguin)
supervised(dog)