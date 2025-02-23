import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(loc = 4 , scale = 1 , size = 1000)

def plot_histogram(x):
    plt.hist(x, density= True, bins = 30, histtype= 'bar', ec = 'black')
    plt.show()

if __name__ == "__main__":
    plot_histogram(x)