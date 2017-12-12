from Testing import testPenData, testCarData, average, stDeviation
import sys
import pickle
import itertools
#from tqdm import tqdm


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

    if len(sys.argv) == 1 or sys.argv[1] == "5":
        print("Q5")
        f = open("q5results.txt", "w")

        f.write("\n>>> QUESTION 5 Pen \n")
        ans = []
        for x in range(5):
            nnet, accuracy = testPenData(hiddenLayers = [24])
            ans.append(accuracy)
        results(ans, f)

        f.write("\n\n\n>>> QUESTION 5 Car \n")
        ans = []
        for x in range(5):
            nnet, accuracy = testCarData(hiddenLayers = [24])
            ans.append(accuracy)
        results(ans, f)

        f.close()

    if len(sys.argv) == 1 or sys.argv[1] == "6":
        print("Q6")

        pans = []
        for p in range(0, 41, 5):
            perp = []
            for x in range(5):
                print("P=" + str(p) + " I=" + str(x))
                nnet, accuracy = testPenData(hiddenLayers = [p])
                perp.append(accuracy)
            pans.append((p, perp))

        print("Saving " + str(pans))
        pickle.dump(pans, open("q6pen.pkl", "wb"))

        cans = []
        for p in range(0, 41, 5):
            perp = []
            for x in range(5):
                print("P=" + str(p) + " I=" + str(x))
                nnet, accuracy = testPenData(hiddenLayers = [p])
                perp.append(accuracy)
            cans.append((p, perp))

        print("Saving " + str(cans))
        pickle.dump(cans, open("q6car.pkl", "wb"))