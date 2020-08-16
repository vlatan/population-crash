import matplotlib.pyplot as plt
from matplotlib import rcParams
from simulation import *


def plot(nonSterile, nonCrispr, crispr, sterile, totalPop):
    """ Plots various different population categories. """
    plt.style.use('fivethirtyeight')
    rcParams['figure.figsize'] = [16, 9]
    rcParams['axes.titlepad'] = 25
    rcParams['axes.titlesize'] = 15
    rcParams['axes.titleweight'] = 700
    rcParams['axes.labelpad'] = 25
    rcParams['axes.labelsize'] = 14
    rcParams['axes.labelweight'] = 700
    rcParams['legend.fontsize'] = 14
    rcParams['xtick.labelsize'] = 14
    rcParams['ytick.labelsize'] = 14
    rcParams['savefig.bbox'] = 'tight'
    rcParams['savefig.pad_inches'] = 0.8
    # rcParams['savefig.dpi'] = 80
    # rcParams['figure.dpi'] = 80

    plt.plot(nonSterile, lw=2, label="Healthy Males")
    plt.plot(nonCrispr, lw=2, label="Healthy Females")
    plt.plot(crispr, lw=2, label="CRISPR Females")
    plt.plot(sterile, lw=2, label="Sterile Males")
    # plt.plot(totalPop, label="Total population")
    plt.xlabel('Cycles')
    plt.ylabel('Population')
    plt.title('Population with CRISPR introduced')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    results = simulate(cycles=400,
                       initSize=1900,
                       offspring=12,
                       lifespan=4,
                       crisprFems=500,
                       popLimit=2000)

    plot(results['nonSterile'],
         results['nonCrispr'],
         results['crispr'],
         results['sterile'],
         results['totalPop'])
