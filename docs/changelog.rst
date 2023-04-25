Changelogs
=============

1.0.0
-------

Initially we wanted to train a Convolutional Neural Network (CNN) using GPU's but faced problems with installing tensorflow2 on our Windows laptops to train it. We had to follow the commands below in the end to successfully install and use tensorflow:

Created a new environment named 'tf' with Python 3.9 using the following command:
.. code-block:: console

   $ conda create --name tf python=3.9

Deactivated the current environment and activated the newly created environment using the following commands:
.. code-block:: console

   $ conda deactivate

   $ conda activate tf

Installed the necessary libraries for GPU support using the following commands:
.. code-block:: console

   $ conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0

Upgraded pip to the latest version using the following command:
.. code-block:: console

   $ pip install --upgrade pip

Installed tensorflow version 2.10 using the following command:
.. code-block:: console

   $ pip install "tensorflow<2.11"

Note: Anything above 2.10 is not supported on the GPU on Windows Native.

Verified the installation by running the following commands:
.. code-block:: console

   $ python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
   $ python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

The first command checks if tensorflow can run a simple operation on the GPU, while the second command checks if the GPU is detected by tensorflow.

More details on installing tensorflow on Windows can be found here: https://www.tensorflow.org/install/pip#windows-native_1
