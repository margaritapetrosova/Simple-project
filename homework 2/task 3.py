def clastering(Human):
    group1=[]
    group2=[]
    group3=[]
    for human in people:
        if human.age<13:
            group1.append(human.age)
            print(group1, '- Child')
        elif 13<human.age<18:
            group2.append(human.age)
            print(group2, '- teen')
        else:
            group3.append(human.age)
            print(group3, '- OLD))')
class Human:
    def __init__(self, theAge):
        self.age=theAge

Human1=Human(12)
Human2=Human(17)
Human3=Human(60)

people=[]
people.append(Human1)
people.append(Human2)
people.append(Human3)

clastering(people)
