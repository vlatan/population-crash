import matplotlib.pyplot as plt
from simulation import *


def plot(nonSterile, nonCrispr, crispr, sterile, totalPop):
    """Plots various different population categories."""
    plt.style.use("fivethirtyeight")
    plt.rcParams["figure.figsize"] = [16, 9]
    plt.rcParams["axes.titlepad"] = 25
    plt.rcParams["axes.titlesize"] = 15
    plt.rcParams["axes.titleweight"] = 700
    plt.rcParams["axes.labelpad"] = 25
    plt.rcParams["axes.labelsize"] = 14
    plt.rcParams["axes.labelweight"] = 700
    plt.rcParams["legend.fontsize"] = 14
    plt.rcParams["xtick.labelsize"] = 14
    plt.rcParams["ytick.labelsize"] = 14
    plt.rcParams["savefig.bbox"] = "tight"
    plt.rcParams["savefig.pad_inches"] = 0.8
    # plt.rcParams['savefig.dpi'] = 80
    # plt.rcParams['figure.dpi'] = 80

    plt.plot(nonSterile, lw=2, label="Healthy Males")
    plt.plot(nonCrispr, lw=2, label="Healthy Females")
    plt.plot(crispr, lw=2, label="CRISPR Females")
    plt.plot(sterile, lw=2, label="Sterile Males")
    # plt.plot(totalPop, label="Total population")
    plt.xlabel("Cycles")
    plt.ylabel("Population")
    plt.title("Population with CRISPR introduced")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    results = simulate(
        cycles=400,
        initSize=1900,
        offspring=12,
        lifespan=4,
        crisprFems=500,
        popLimit=2000,
    )

    plot(
        results["nonSterile"],
        results["nonCrispr"],
        results["crispr"],
        results["sterile"],
        results["totalPop"],
    )
