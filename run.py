import simulation as sim
from plot import plot
import streamlit as st

if __name__ == "__main__":
    results = sim.simulate()
    st.button("Re-run")
    # plot(**results)
