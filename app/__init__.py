import streamlit as st
from . import simulation as sim


def create_app() -> None:
    """Create streamlit application"""

    # meta title - set_page_config needs to be called first in the page
    st.set_page_config(
        page_title="Gene Drive Population Crash Simulation",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon=":material/change_circle:",
    )

    # cursor pointer on dropdown select and h1 link style
    custom_style = """
        <style>
            div[data-baseweb='select'] > div:hover {cursor:pointer}
            h1.main-title > a {text-decoration:none;color:white}
        </style>
    """
    st.html(custom_style)

    # logo and site title
    st.sidebar.title("Population Crash with Gene Drive - Simulation")

    sim.simulate()
