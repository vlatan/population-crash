import pathlib
import streamlit as st
import simulation as sim


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
    custom_h1 = f"<h1 class='main-title'><a href='/' target = '_self' title='Home'>Population Crash with Gene Drive - Simulation</a></h1>"
    st.sidebar.markdown(custom_h1, unsafe_allow_html=True)

    # st.sidebar.divider()

    sim.simulate()

    info = get_info()
    st.markdown(info)


# @st.cache_data(show_spinner=False)
def get_info() -> str:
    """Get README file content."""

    readme = pathlib.Path(__file__).parent.resolve() / "README.md"
    return pathlib.Path(readme).read_text()
