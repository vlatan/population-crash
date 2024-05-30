import streamlit as st

from plot import plot
import simulation as sim

if __name__ == "__main__":
    results = sim.simulate()
    st.button("Re-run")
    # plot(**results)
