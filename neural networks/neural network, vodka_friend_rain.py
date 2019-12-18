import numpy as np
class GoToDrink:
    def _init_(self, theVodka, theRain, theFriend):
        self.vodka=theVodka
        self.rain=theRain
        self.friend=theFriend
    def activation_function(self, x):
        if x>=0.5:
            return 1
        else:
            return 0

    def predict(self):
        inputs = np.array([1.0, 0.0, 1.0])

        weights_input_to_hidden_1 = [0.25, 0.25, 0]
        weights_input_to_hidden_2 = [0.5, -0.4, 0.9]
        weights_input_to_hidden=np.array([weights_input_to_hidden_1, weights_input_to_hidden_2])


        weights_hidden_to_output=np.array([-1.0,1.0])


        hidden_input=np.dot(weights_input_to_hidden, inputs)
        print("hidden_input: " + str(hidden_input))

        hidden_output=np.array([self.activation_function(x) for x in hidden_input])
        print("hidden_output: " + str(hidden_output))

        output=np.dot(weights_hidden_to_output, hidden_output)
        print("output: " + str(output))
        return self.activation_function(output)

someNeuralNetwork=GoToDrink()
print("result: " + str(someNeuralNetwork.predict()))