Workflow for Development
===========

Week 1
------

Sort and combine datasets from Kaggle. (Finalized to https://www.kaggle.com/datasets/muhammadkhalid/sign-language-for-numbers?resource=download)
Experiment with Mediapipe to get the coordinates. And create new databse containing the Relational Coordinates (That is origin is shifted to be the the landmark on extreme left and upper side of image as)
Train the Random Forest Classifier Model.
Test the Model using live webcam feed.

Week 2
----------

Create the necessary nodes for remote control of the Turtlebot.
Integrate LIDAR sensor data to create obstacle detection and avoidance nodes.
Filter the LIDAR data to improve the robot's navigation capabilities.

Final Demonstration:
--------------------

Test the robot using actual hand gestures and observe how it responds in both remote control cobot use cases.
Showcase the cobot in action and demonstrate its ability to navigate real-world environments using hand gestures for control.
Highlight the system's obstacle detection and warning capabilities using LIDAR data.

Data Collection
---------------

Initially, we explored numerous datasets on Kaggle, including Hagrid (https://www.kaggle.com/datasets/kapitanov/hagrid). However, due to its size, it did not produce precise results. Additionally, our initial approach involved training a CNN, but during live testing, it proved too large and caused delays.

Eventually, we developed a suitable model and conducted live testing using the Random Forest Classifier. We considered the project a success only when we could accurately distinguish between gestures in real-time with minimal lag.

The success of our project can be observed in the following live video feed: https://drive.google.com/file/d/1cTOBM8yirr-CUNDXlD5NiQ4OxRtWHF7Z/view?usp=sharing

