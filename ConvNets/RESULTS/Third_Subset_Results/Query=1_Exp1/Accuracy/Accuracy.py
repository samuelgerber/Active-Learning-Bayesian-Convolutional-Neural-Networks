# http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
import numpy as np
import matplotlib.pyplot as plt


Bald = np.load('BALD.npy')
Bayes_Segnet = np.load('Segnet.npy')
BCNN_Entropy = np.load('Dropout_Max_Entropy.npy')
Variation = np.load('Variation_Ratio.npy')


Queries = np.arange(0, 51, 1)

plt.figure(figsize=(12, 8), dpi=80)

plt.plot(Queries, Bald, color="red", linewidth=1.0, marker='x', label="Dropout BALD" )
plt.plot(Queries, Bayes_Segnet, color="blue", linewidth=1.0, marker='x', label="Dropout Bayes Segnet")
plt.plot(Queries, BCNN_Entropy, color="black", linewidth=1.0, marker='x', label="Dropout - Max Entropy")
plt.plot(Queries, Variation, color="yellow",linewidth=1.0, marker='x', label="Dropout - Variation Ratio" )


plt.xlabel('Number of Queries')
plt.ylabel('Accuracy on Test Set')
plt.title('Comparing Acquisition Functions')
plt.grid()
# Set x limits
# plt.xlim(1000.0, 10000.0)
# plt.ylim(0.8, 1.0)
plt.legend(loc = 3)
plt.show()
