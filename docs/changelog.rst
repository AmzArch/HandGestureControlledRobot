Changelog
=============

2.2.0
-------

New:

- To address the GIL limitation, we combined the three separate nodes into one Python node, which improved performance.
- However, the fastest approach was live control without crash detection functionality.
- A potential solution to overcome this limitation would be to use separate edge computers to process different types of data and inputs, with one central node making decisions.

2.1.2
-------

New:

- Previous implementation had three nodes, publishing gesture, filtered LIDAR readings and publishing Twist messages, also showing the camera view of Turtlebot4.
- Video feed would turn red if it sensed an obstacle in proximity.
- Running multiple Python nodes caused performance issues due to Global Interpreter Lock(GIL) limitation.


2.1.1
-----

New:

- Ensured safety of the robot and avoided collisions by using readings from the Turtlebot4's lidar.
- Filtered the lidar data using an FIR filter with a memory of past 50 readings due to erratic readings between subsequent readings.
- Implemented a feature to prevent the robot from moving forward if an obstacle was detected to be too close by the lidar.

.. note::

   Adjusted for the offset of the Turtlebot4's lidar, which was placed at an offset of 90 degrees.
   Modified the readings to account for the offset, with the front of the lidar being considered the left side of the Turtlebot4.

2.1.0
-----

New:

- Integrated the trained model into a ROS2 publisher node.
- Used the model to predict gestures from video feeds obtained from the laptop's webcam.
- Implemented a function to publish Twist messages to the /cmd/vel topic on the Turtlebot4 based on the recognized gestures.

2.0.2
-----
New:

- Online research led to the discovery that successful solutions used relational coordinates of hand landmarks for gesture recognition instead of absolute coordinates.
- Adopting this approach yielded a model accuracy of 97%.


2.0.1
------
New:

- Trained a model using the Random Forest Classifier in scikit-learn library to recognize gestures based on landmark segment coordinates.
- Achieved a model accuracy of 85% with this approach.


2.0.0
------
New:

- The previous approach was ineffective due to the model's size and lack of improvement in accuracy and latency.
- Mediapipe python library was adopted as an alternative solution, leveraging 21 hand landmarks to segment human hands. More information on mediapipe python library can be found here: https://developers.google.com/mediapipe/solutions/vision/hand_landmarker.
- The X and Y coordinates of the landmarks can be recorded and used to train a machine learning model for gesture recognition.

1.0.2
-------
New:

- The model was trained on isolated hand images obtained from a dataset on Kaggle found in https://www.kaggle.com/datasets/muhammadkhalid/sign-language-for-numbers?resource=download.
- Accurate predictions required segmentation of hands from the video feed.
- Testing the model on live video feed revealed a significant latency between video input and gesture recognition.
- The latency was unsuitable for real-time control of the Turtlebot4, hindering its use as a remote-controlled collaborative robot.

1.0.1
-------
New:

- Technical challenges arose while training the model on Virtualbox running Ubuntu 20.04 due to the absence of AVX and AVX2 instruction sets required by Tensorflow.
- A possible workaround is to use Tensorflow Lite instead of Tensorflow.
- The large size of the model prompted a need to reduce inference time, leading to the decision to dualboot laptops with Ubuntu 20.04 and continue using Tensorflow.


1.0.0
-------
New:

- We plan on training a Convolutional Neural Network (CNN) using Tensorflow library for the gesture detection mechanism.
- We plan on creating the CNN model using Tensorflow and feeding it images found on Kaggle dataset.
- The Model will be trained on a vast dataset containing images of people and hands in various positions, backgrounds and also have some unknown set of images to train the network.

To achieve the above we follow the steps given below:

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
If tensorflow was installed correctly then it should list the GPU on the device.

More details on installing tensorflow on Windows can be found here: https://www.tensorflow.org/install/pip#windows-native_1 
