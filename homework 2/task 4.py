def predict(wether):
    result=(wether.cloud*0.1+wether.rein*0.1+wether.sun*0.8)
    print('Вероятность солнечной погоды ', result)

class wether:
    def __init__(self, theCloud, theRein, theSun):
        self.cloud=theCloud
        self.rein=theRein
        self.sun=theSun

Mondey=wether(0,0,10)
Tusday=wether(10,10,7)
Wednesday=wether(4,5,3)



predict(Mondey)
predict(Tusday)
predict(Wednesday)
