import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_leaves_visualizer_body():
    st.write("### Leaves Visualizer")
    st.info(
        f"Here, you can explore a visual study designed "
        f"to distinguish between "
        f"healthy cherry leaves and those affected by powdery mildew."
    )

    if st.checkbox("Difference between average and variability image"):

        avg_mildew = plt.imread(f"outputs/v1/avg_var_healthy.png")
        avg_healthy = plt.imread(f"outputs/v1/avg_var_powdery_mildew.png")

        st.warning(
            f"We observed that the average and variability "
            f"images did not reveal clear patterns "
            f"that would allow us to intuitively differentiate "
            f"between the two."
            f"However, a subtle difference in the color pigmentation "
            f"of the average images is observed for both labels."
        )

        st.image(
            avg_mildew,
            caption="Powdery Mildew - Average and Variability.")
        st.image(
            avg_healthy,
            caption="Healthy - Average and Variability.")
        st.write("---")

    if st.checkbox("Difference between average mildew and healthy."):
        diff_between_avgs = plt.imread(f"outputs/v1/avg_diff.png")

        st.warning(
            f"We observed that this study did not reveal "
            f"patterns that would allow us to "
            f"intuitively differentiate between the two."
        )

        st.image(
            diff_between_avgs,
            caption="Difference between average images.")

    if st.checkbox("Image Montage"):
        st.write(
            "To refresh the montage,"
            " please click on the 'Create Montage' button")
        my_data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label",
                                        options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(
                dir_path=my_data_dir + '/validation',
                label_to_display=label_to_display,
                nrows=8, ncols=3, figsize=(10, 25)
            )
    st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # Check if the label_to_display exists in the directory
    if label_to_display in labels:
        images_list = os.listdir(os.path.join(dir_path, label_to_display))

        # Ensure that we do not exceed the number of available images
        if nrows * ncols <= len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Reduce the number of rows (nrows) "
                f"or columns (ncols) to create your montage. \n"
                f"There are {len(images_list)} images in your subset. "
                f"You requested a montage with {nrows * ncols} spaces."
            )
            return  # Exit the function if the montage size is too large

        # Prepare the grid for subplots
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # Create the figure and axes for the montage
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

        # Iterate through the grid and populate the montage
        for x in range(nrows * ncols):
            img = imread(os.path.join(dir_path, label_to_display, img_idx[x]))
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])

        # Adjust layout and show the plot
        plt.tight_layout()
        st.pyplot(fig=fig)
    else:
        # Handle case where the label is not found
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
