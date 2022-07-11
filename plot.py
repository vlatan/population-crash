import matplotlib as mpl
import matplotlib.pyplot as plt
import simulation as sim


def plot(non_sterile, non_crispr, crispr, sterile, total_pop):
    """Plots various different population categories."""
    plt.style.use("fivethirtyeight")
    mpl.rcParams["figure.figsize"] = [16, 9]
    mpl.rcParams["axes.titlepad"] = 25
    mpl.rcParams["axes.titlesize"] = 15
    mpl.rcParams["axes.titleweight"] = 700
    mpl.rcParams["axes.labelpad"] = 25
    mpl.rcParams["axes.labelsize"] = 14
    mpl.rcParams["axes.labelweight"] = 700
    mpl.rcParams["legend.fontsize"] = 14
    mpl.rcParams["xtick.labelsize"] = 14
    mpl.rcParams["ytick.labelsize"] = 14
    mpl.rcParams["savefig.bbox"] = "tight"
    mpl.rcParams["savefig.pad_inches"] = 0.8
    # mpl.rcParams['savefig.dpi'] = 80
    # mpl.rcParams['figure.dpi'] = 80

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
    results = sim.simulate()
    plot(**results)
