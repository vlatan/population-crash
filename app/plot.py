import matplotlib as mpl
import matplotlib.pyplot as plt

from . import config


def plot(
    non_sterile: config.Vector,
    non_crispr: config.Vector,
    crispr: config.Vector,
    sterile: config.Vector,
    total_pop: config.Vector,
) -> None:
    """Plots various different population categories."""

    plt.style.use("fivethirtyeight")
    mpl.rcParams["figure.figsize"] = [16, 9]
    mpl.rcParams["figure.dpi"] = 90
    mpl.rcParams["axes.titlepad"] = 25
    mpl.rcParams["axes.titlesize"] = 15
    mpl.rcParams["axes.titleweight"] = 700
    mpl.rcParams["axes.labelpad"] = 25
    mpl.rcParams["axes.labelsize"] = 14
    mpl.rcParams["axes.labelweight"] = 700
    mpl.rcParams["legend.fontsize"] = 14
    mpl.rcParams["xtick.labelsize"] = 14
    mpl.rcParams["ytick.labelsize"] = 14

    plt.plot(non_sterile, lw=2, label="Healthy Males")
    plt.plot(non_crispr, lw=2, label="Healthy Females")
    plt.plot(crispr, lw=2, label="CRISPR Females")
    plt.plot(sterile, lw=2, label="Sterile Males")
    # plt.plot(total_pop, lw=2, label="Total population")
    plt.xlabel("Cycles")  # type: ignore
    plt.ylabel("Population")  # type: ignore
    plt.title("Population with CRISPR introduced")
    plt.legend()
    plt.tight_layout(pad=2.5)
    plt.show()
