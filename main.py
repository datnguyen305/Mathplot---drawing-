import matplotlib.pyplot as plt
import numpy as np
import argparse


def plot_histogram():
    x = np.random.normal(loc = 4 , scale = 1 , size = 1000)
    plt.hist(x, density= True, bins = 30, histtype= 'bar', ec = 'black')
    plt.show()

def boxplot():
    np.random.seed(10)
    data_1 = np.random.normal(100, 10, 200)
    data_2 = np.random.normal(90, 20, 200)
    data_3 = np.random.normal(80, 30, 200)
    data = [data_1, data_2, data_3]

    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_axes([0, 0, 1, 1])

    bp = ax.boxplot(data)
    plt.show()

def lineplot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

def barplot():
    x = np.arange(5)
    y = np.random.randint(1, 10, 5)
    plt.bar(x, y)
    plt.show()

parser = argparse.ArgumentParser(description="Chạy từng loại biểu đồ")
parser.add_argument("chart_type", choices=["histogram", "boxplot","barplot", "lineplot"], help="Chọn loại biểu đồ để vẽ")
args = parser.parse_args()

if __name__ == "__main__":
    if args.chart_type == "histogram":
        plot_histogram()
    elif args.chart_type == "boxplot":
        boxplot()
    elif args.chart_type == "lineplot":
        lineplot()
    elif args.chart_type == "barplot":
        barplot()