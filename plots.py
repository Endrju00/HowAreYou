import matplotlib.pyplot as plt
import numpy as np
from ing_theme_matplotlib import mpl_style


def plotData(days, data_1, data_2, data_1_label="data1", data_2_label="data2", x_label='Days', y_label='Scaled values', color1="Purple", color2="Orange", dark=False, filename='Plt.png'):
    plt.close('all')
    x = np.linspace(0, days, days)
    mpl_style(dark=dark)

    plt.plot(x, data_1, label=data_1_label, color=color1)
    plt.plot(x, data_2, label=data_2_label, color=color2)

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.legend()
    plt.tight_layout()
    plt.savefig('plots/{}'.format(filename))
