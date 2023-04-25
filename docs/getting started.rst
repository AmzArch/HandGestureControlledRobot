Getting Started
===========

Requirements
-------------
  - Python 3.9 or newer

Installation
-------------

.. code-block:: console

   $ pip install -r requirements.txt

Quick Start
-------------
If you have the ROS2 setup on your Turtlebot4 or any other mobile platform running ROS2 and installed all the required python dependencies you can follow the instructions in this section to get your robot moving to the commands of the user through the webcam of your laptop.

**Step 1**

Clone https://github.com/AmzArch/HandGestureControlledRobot and copy the cobot3_ws folder found in HandGestureControlledRobot folder into your robot platform running ROS2.

**Step 2**

Go into the HandGestureControlledRobot directory with the following command:

.. code-block:: console

   $ cd HandGestureControlledRobot
 
**Step 3**

Build your workspace by running the command below:

.. code-block:: console

   $ colcon build
   
**Step 4**

Initialize setup.bash file:

.. code-block:: console

   $ . install/setup.bash
 
It is highly recommended to go through the next section on setting up your Turtlebot4. It can get quite tedious and the documentation provided in the section below is quite thorough with walking over the important aspects of setting up the Turtlebot4 and getting everything set up properly.


Setting Up Turtlebot4
-------------

Setting up the Turtlebot4 might be quite tedious and hence is beyond the scope of this documentation. Please refer to the detailed documentation available at: https://robot-deployment.bitbucket.io/tutorials/turtlebot/01-turtlebot-unboxing/
