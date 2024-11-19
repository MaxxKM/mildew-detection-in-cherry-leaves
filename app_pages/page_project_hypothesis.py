import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"Our initial hypothesis was to identify clear patterns that could distinguish "
        f"healthy leaves from those affected by powdery mildew, "
        f"focusing mainly on the presence of a white covering and damaged "
        f"leaf edges.\n\n"
        f"We observed that powdery mildew leaves tend to lack pigmentation, "
        f"resulting in a darker green color, with the edges curling toward the center of the leaf.\n\n"
        f"When comparing the Average Images and Variability Images of healthy "
        f"and powdery mildew leaves, we noticed a wider, oval shape with scattered "
        f"white spots on the powdery mildew leaves. "
        f"However, this difference alone wasn't sufficient to visually differentiate the two classes."
    )