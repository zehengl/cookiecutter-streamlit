import streamlit as st


st.set_page_config(page_title="{{cookiecutter.name}}", page_icon="random")
_, center, _ = st.columns([2, 1, 2])
with center:
    st.image(
        "{{cookiecutter.img}}",
        use_column_width=True,
    )
st.title("{{cookiecutter.name}}")
st.caption("{{cookiecutter.description}}")
