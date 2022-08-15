import simulation as sim
from plot import plot

if __name__ == "__main__":
    results = sim.simulate()
    plot(**results)
