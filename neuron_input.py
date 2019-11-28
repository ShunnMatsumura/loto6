# coding: UTF-8
import math
import matplotlib.pyplot as plt

def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))

class Neuron:
    input_sum = 0.0
    output = 0.0

    def setInput(self, inp):
        self.input_sum += inp

    def getOutPut(self):
        self.output = sigmoid(self.input_sum)
        return self.output

    def reset(self):
        self.input_sum = 0
        self.output = 0

class NeuralNetwork:
    w = [-0.5, 0.5, -0.2]
    neuron = Neuron()
    def commit(self, input_data):
        self.neuron.reset()
        bias = 1.0
        self.neuron.setInput(input_data[0] * self.w[0])
        self.neuron.setInput(input_data[1] * self.w[1])
        self.neuron.setInput(bias * self.w[2])
        return self.neuron.getOutPut()

refer_point_0 = 34.5
refer_point_1 = 137.5

trial_data = []
trial_data_file = open("./datas/test_data.txt", "r")
for line in trial_data_file:
    line = line.rstrip().split(",")
    trial_data.append([float(line[0]) - refer_point_0, float(line[1]) - refer_point_1])
trial_data_file.close()

neural_network = NeuralNetwork()

position_tokyo = [ [], [] ]
position_kanagawa = [ [], [] ]
for data in trial_data:
    if(neural_network.commit(data) < 0.5):
        position_tokyo[0].append(data[1]+refer_point_1)
        position_tokyo[1].append(data[0]+refer_point_0)
    else:
        position_kanagawa[0].append(data[1]+refer_point_1)
        position_kanagawa[1].append(data[0]+refer_point_0)

plt.scatter(position_tokyo[0], position_tokyo[1], c="red", label= "tokyo", marker="+")
plt.scatter(position_kanagawa[0], position_kanagawa[1], c="blue", label= "kanagawa", marker="+")
plt.legend() # 散布図には必要なこと
plt.show()