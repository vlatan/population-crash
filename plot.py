import matplotlib.pyplot as plt
from simulation import *


def plot(non_sterile, non_crispr, crispr, sterile, total_pop):
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

    plt.plot(non_sterile, lw=2, label="Healthy Males")
    plt.plot(non_crispr, lw=2, label="Healthy Females")
    plt.plot(crispr, lw=2, label="CRISPR Females")
    plt.plot(sterile, lw=2, label="Sterile Males")
    # plt.plot(total_pop, lw=2, label="Total population")
    plt.xlabel("Cycles")
    plt.ylabel("Population")
    plt.title("Population with CRISPR introduced")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    results = simulate()
    plot(**results)
