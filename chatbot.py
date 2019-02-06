import random
class chatbot:
    def __init__(self, theStandartAns, theQuestionAnsw):
        self.answer=theStandartAns
        self.questans=theQuestionAnsw
    def myanswer(self, text):
        if '?' in text:
            index = random.randint(0, len(self.questans)-1)
            print(self.questans[index])
        else:
            index = random.randint(0,len(self.answer)-1)
            print(self.answer[index])
Mybot=chatbot(['Sama dura', 'Ovca'],['da','net','ne znau'])

while True:
    text = input()
    Mybot.myanswer(text)
    