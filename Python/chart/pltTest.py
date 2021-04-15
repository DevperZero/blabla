import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 5, 0])
mylabels = ["PASS", "Fail", "Not test"]
mycolors = ["violet", "red", "lightgray"]

figu = plt.figure(figsize=(8, 8))
plt.pie(y, labels = mylabels, startangle = 90, autopct='%1.1f%%', colors=mycolors)
plt.savefig('./test/test.png')