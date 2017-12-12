from Testing import testPenData, testCarData, average, stDeviation
import pickle
from matplotlib import pyplot as plt

car = pickle.load(open("q6car.pkl", "rb"))
pen = pickle.load(open("q6pen.pkl", "rb"))
q7 = pickle.load(open("q7.pkl", "rb"))

def plot_learning_curve(title, data):
    plt.figure()
    plt.title(title)
    plt.xlabel("Perceptrons")
    plt.ylabel("Accuracy")


    perps = []
    mean = []
    low = []
    high = []

    for (p, results) in data:
        print(results)
        perps.append(p)

        avg = average(results)
        stdev = stDeviation(results)
        mean.append(avg)
        low.append(avg-2*stdev)
        high.append(avg+2*stdev)


    plt.grid()
    plt.fill_between(perps, low, high, alpha=0.1,
                     color="g")
    plt.plot(perps, mean, 'o-', color="g",
             label="Test score")
    plt.savefig(str(title)+".png")

plot_learning_curve("q6_CarData", car)
plot_learning_curve("q6_PenData", pen)
plot_learning_curve("q7_curve", q7)

