from NeuralNet import buildNeuralNet
from NeuralNetUtil import buildIrisData
from Testing import testPenData, testCarData, average, stDeviation
import sys
import pickle
import csv
import random

XORtruth = [([0, 0], [0]),
            ([0, 1], [1]),
            ([1, 0], [1]),
            ([1, 1], [0])]

# Xin = [[0, 0], [0, 1], [1, 0], [1, 1]]
# Xout = [[0], [1], [1], [0]]
# XORtruth = zip(Xin*100, Xout*100)

# XORamples = (zip(Xin, Xout), zip(Xin, Xout))
XORtrain = XORtruth*100
XORtest = XORtruth*100

XORdata = (XORtrain, XORtest)

iris =buildIrisData()
#print(iris)

def results(a, f):
    print('\nMax     : ' + str(max(a)))
    print('\nSt Dev  : ' + str(stDeviation(a)))
    print('\nMean    : ' + str(average(a)))
    f.write("\nAnswers: \n")
    f.write(str(a))
    f.write("\n")
    f.write('\nMax    : ' + str(max(a)))
    f.write('\nStDev  : ' + str(stDeviation(a)))
    f.write('\nMean   : ' + str(average(a)))

if __name__ == '__main__':

    if len(sys.argv) == 1 or sys.argv[1] == "7":

        ans = []
        res = []
        for p in range(50):
            ans = []
            for x in range(10):
                nnet, accuracy = buildNeuralNet(XORdata, maxItr=400, hiddenLayerList=[p], printer=False)
                ans.append(accuracy)
            print("P=" + str(p) + " : " + str(sum(ans)/len(ans)) + " -> " + str(ans))
            res.append((p, ans))

        pickle.dump(res, open("q7.pkl", "wb"))

    if len(sys.argv) == 1 or sys.argv[1] == "8":
        print("Q8")
        f = open("q8results.txt", "w")


        f.write("\n>>> QUESTION 8 Iris \n")
        ans = []
        for x in range(5):
            nnet, accuracy = buildNeuralNet(iris, maxItr=200, hiddenLayerList=[42])#, printer=False)
            ans.append(accuracy)
        results(ans, f)

        f.close()