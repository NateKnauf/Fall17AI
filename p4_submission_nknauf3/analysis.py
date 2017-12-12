from Testing import testPenData, testCarData, average, stDeviation
import pickle
from matplotlib import pyplot as plt
import csv

car = pickle.load(open("q6car.pkl", "rb"))
pen = pickle.load(open("q6pen.pkl", "rb"))

with open("q6analysis.csv", "w") as csvfile:
    fieldnames = ["Perp", "Pmax", "Pavg", "Pstd", "Cmax", "Cavg", "Cstd"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for (c, p) in zip(car, pen):
        writer.writerow({'Perp':p[0], 'Pmax':max(p[1]), 'Pavg':average(p[1]), 'Pstd':stDeviation(p[1]),
                                      'Cmax':max(c[1]), 'Cavg':average(c[1]), 'Cstd':stDeviation(c[1])})


