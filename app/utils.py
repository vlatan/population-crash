import pathlib
import pandas as pd
import streamlit as st


@st.cache_data(show_spinner=False)
def read_placeholder_csv() -> pd.DataFrame:
    csv = pathlib.Path(__file__).parent.resolve() / "placeholder.csv"
    return pd.read_csv(csv, index_col="Reproductive Cycles")


@st.cache_data(show_spinner=False)
def get_readme() -> tuple[str, str]:
    """Get README file content."""
    readme = pathlib.Path(__file__).parent.parent.resolve() / "README.md"
    readme = pathlib.Path(readme).read_text()
    excerpt = readme.split("<!-- EXCERPT -->")
    info = readme.split("<!-- INFO -->")
    return excerpt[1], info[1]
