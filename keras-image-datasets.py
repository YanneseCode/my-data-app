# Install Dependencies
!pip install streamlit
!pip install tensorflow
!pip install matplotlib
import streamlit as st
import tensorflow
from tensorflow.keras import datasets
import matplotlib.pyplot as plt


def get_dataset_mappings():
  """
    Get mappings for dataset key
    to dataset and name.
  """
  mappings = {
    'CIFAR-10': datasets.cifar10,
    'CIFAR-100': datasets.cifar100,
    'Fashion MNIST': datasets.fashion_mnist,
    'MNIST': datasets.mnist
  }
  return mappings
  

def load_dataset(name):
  """
    Load a dataset
  """
  # Define name mapping
  name_mapping = get_dataset_mappings()
  
  # Get train data
  (X, _), (_, _) = name_mapping[name].load_data()
  
  # Return data
  return X


def draw_images(data, start_index, num_rows, num_cols):
  """
    Generate multiplot with selected samples.
  """
  # Get figure and axes
  fig, axs = plt.subplots(num_rows, num_cols)
  # Show number of items
  show_items = num_rows * num_cols
  # Iterate over items from start index
  iterator = 0
  for row in range(0, num_rows):
    for col in range(0, num_cols):
      index = iterator + start_index
      axs[row, col].imshow(data[index])
      axs[row, col].axis('off')
      iterator += 1
  # Return figure
  return st.pyplot(fig)


def do_streamlit():
  """
    Set up the Streamlit dashboard and capture
    interactions.
  """
  # Styling
  plt.style.use('dark_background')

  # Set title
  st.title('Interactive visualization of Keras image datasets')

  # Define select box
  dataset_selection = st.selectbox('Dataset', ('CIFAR-10', 'CIFAR-100', 'Fashion MNIST', 'MNIST'))

  # Dataset
  dataset = load_dataset(dataset_selection)
  
  # Number of images in dataset
  maximum_length = dataset.shape[0]

  # Define sliders
  picture_id = st.slider('Start at picture', 0, maximum_length, 0)
  no_rows = st.slider('Number of rows', 2, 30, 5)
  no_cols = st.slider('Number of columns', 2, 30, 5)

  # Show image
  try:
    st.image(draw_images(dataset, picture_id, no_rows, no_cols))
  except:
    print()


if __name__ == '__main__':
  do_streamlit()
