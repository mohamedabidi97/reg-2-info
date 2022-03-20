import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cm2 = ListedColormap(['#0000aa', '#ff2020'])

def reg_plot(model,X,y):  
    line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    plt.figure(figsize=(8, 8))
    plt.plot(line, model.predict(line))
    plt.plot(X, y, 'o', c=cm2(0))
    ax = plt.gca()
    ax.legend(["Model", "Training data"], loc="best")
    ax.grid(True)
    plt.show()

