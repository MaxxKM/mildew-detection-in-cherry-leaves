import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
from app_pages.page_mildew_detection import page_mildew_detection_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_machine_learning_performance import (
    page_ml_performance_metrics
)


app = MultiPage(app_name="Mildew Detector")

app.add_page("Project Summary", page_summary_body)
app.add_page("Leaves Visualizer", page_leaves_visualizer_body)
app.add_page("Mildew Detection", page_mildew_detection_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("Machine Learning Process", page_ml_performance_metrics)

app.run()
