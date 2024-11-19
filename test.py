import pickle

# Path to your image_shape.pkl file
image_shape_path = "outputs/v1/image_shape.pkl"  # Make sure to update the version if needed

# Load the pickle file to check the contents
with open(image_shape_path, 'rb') as f:
    image_shape = pickle.load(f)

# Print the content of the file
print("Image shape loaded from pickle file:", image_shape)
