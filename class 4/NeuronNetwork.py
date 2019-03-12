import numpy
class GoToWalkANN:
    def __init__(self, theWeather=1.0, theMood=1.0, theFriends=1.0):
        self.weather=theWeather
        self.mood=theMood
        self.friends=theFriends
    def activationFunction(self, x):
        if x>=0.5:
            return 1
        else:
            return 0
    def solve(self):
        inputs=numpy.array([self.weather,self.mood,self.friends])

#weights from input to hidden layer
        weightsInputToHidden1 = [0.5, 0.5, 0.0]
        weightsInputToHidden2 = [0.7, 0.0, 0.0]
        weightsInputToHidden=numpy.array([weightsInputToHidden1, weightsInputToHidden2])

#weights from hidden to output layer

        weightsHiddenToOutput=numpy.array([0.5,0.5])

#we calculate what will come as input to hidden layer
#multiplying weights to inputs and adding separately for 2 inputs

        hiddenInput=numpy.dot(weightsInputToHidden, inputs)
        print("hidden input:"+str(hiddenInput))
#we apply activation function to every hidden input(2 elements)

        hiddenOutput=numpy.array([self.activationFunction(x) for x in hiddenInput])
        print("hidden output:"+str(hiddenOutput))

#we calculate output signal
        output=numpy.dot(weightsHiddenToOutput, hiddenOutput)
        print("output:"+str(output))
        return self.activationFunction(output)

someNeuralNetwork=GoToWalkANN(0, 1, 0)
print("result:"+str(someNeuralNetwork.solve()))