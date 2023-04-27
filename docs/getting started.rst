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

Clone the repository into your robot platform running ROS2.

.. code-block:: console

   $ git clone https://github.com/VishalNadig/hand-gesture-controlled-turtlebot4.git

**Step 2**

Copy the cobot3_ws folder found in hand-gesture-controlled-turtlebot4 into your home directory and change into the cobot3_ws directory with the following commands:

.. code-block:: console

   $ cp -r hand-gesture-controlled-turtlebot4/cobot3_ws ~/
   $ cd ~/cobot3_ws/
   
 
**Step 3**

Build your workspace by running the command below:

.. code-block:: console

   $ colcon build
   
**Step 4**

Initialize setup.bash file:

.. code-block:: console

   $ . install/setup.bash
 
 **Step 5**

Run the ROS2 node:

.. code-block:: console

   $ ros2 run cobot drive
 
It is highly recommended to go through the next section on setting up your Turtlebot4. It can get quite tedious and the documentation provided in the section below is quite thorough with walking over the important aspects of setting up the Turtlebot4 and getting everything set up properly.


Setting Up Turtlebot4
============

Setting up the Turtlebot4 might be quite tedious and hence is beyond the scope of this documentation. Please refer to the detailed documentation available at: https://robot-deployment.bitbucket.io/tutorials/turtlebot/01-turtlebot-unboxing/
