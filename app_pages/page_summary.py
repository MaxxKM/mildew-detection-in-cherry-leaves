import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():
    st.write('### Project Summary')

    st.info(
        f"**Mildew Information**\n\n"
        f"Our client, Farm & Foody, approached us to address "
        f"a critical challenge in their cherry orchards:  \n\n"
        f"distinguishing healthy cherry leaves from those "
        f"affected by powdery mildew. Powdery mildew can \n"
        f"significantly impact crop yield and quality, and "
        f"early detection is vital for effective management.  \n\n"
        f"To support their efforts, Farm & Foody tasked us "
        f"with developing a solution to visually differentiate\n"
        f"healthy leaves from those showing signs of this "
        f"fungal disease. Additionally, the client is keen on\n"
        f"leveraging predictive tools to classify cherry leaves "
        f"based on their health status, enabling more"
        f"precise and timely interventions.\n\n"
        f"Our project focuses on creating a reliable, efficient, "
        f"and scalable system that meets Farm & Foody’s\n"
        f"needs for disease detection and prediction, "
        f"ensuring healthier crops and optimized operations."
    )

    st.write(
        f"* For additional info, please visit and **read** the "
        f"[project README.md file]"
        f"(https://github.com/MaxxKM/"
        f"mildew-detection-in-cherry-leaves/blob/main/README.md)"
    )

    st.success(
        f"The project had 2 business requirements:\n\n"
        f"1 - The client is interested in conducting "
        f"a study to visually differentiate \n"
        f"a cherry leaf that is healthy from one that "
        f"contains powdery mildew.\n\n"
        f"2 - The client is interested in predicting if "
        f"a cherry leaf is healthy or contains\n"
        f"powdery mildew."
    )
