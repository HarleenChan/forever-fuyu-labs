import streamlit as st

st.set_page_config(
    page_title="SoulSense",
    page_icon="🫧",
    layout="centered"
)

st.title("🫧 SoulSense v0.1")
st.caption("Tiny, kind AI tools for everyday emotions")

# Tabs
tab1, tab2, tab3 = st.tabs(["Check-in", "Journal", "Sigil"])

with tab1:
    st.subheader("Mood Check-in")
    st.slider("How are you feeling?", -5, 5, 0)
    st.text_area("Want to add a few words?")

with tab2:
    st.subheader("Gentle Journal")
    st.text_area("Write freely…")
    st.button("Emergency Fuyu")

with tab3:
    st.subheader("Sigil Maker")
    st.text_input("Your word/phrase for the sigil")
    st.button("Generate Sigil")

