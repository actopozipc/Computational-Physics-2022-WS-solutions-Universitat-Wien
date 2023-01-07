import csv
import matplotlib.pyplot as plt
x = []
y = []

# opening the CSV file
with open('conjugate.csv', mode ='r')as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        time = lines[0]
        size = lines[1]
        y.append(size)
        x.append(time)
plt.plot(x,y)
x = []
y = []

# opening the CSV file
with open('steepest.csv', mode ='r')as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        time = lines[0]
        size = lines[1]
        y.append(size)
        x.append(time)
plt.loglog(x,y)
plt.legend(["Conjugate", "Steepest"])
plt.xlabel("Seconds")
plt.ylabel("Matrix size")
plt.show()