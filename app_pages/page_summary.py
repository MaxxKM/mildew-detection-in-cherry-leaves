import streamlit as st
from matplotlib.pyplot as plt

def page_summary_body():
    st.write('### Project Summary')

    st.info(
        f"**Mildew Information**  /n"
        f"Our client, Farm & Foody, approached us to address a critical challenge in their cherry orchards:  /n/n"
        f"distinguishing healthy cherry leaves from those affected by powdery mildew. Powdery mildew can /n"
        f"significantly impact crop yield and quality, and early detection is vital for effective management.  /n/n"
    )