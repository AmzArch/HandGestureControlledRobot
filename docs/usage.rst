Usage
=====

.. _installation:

ROS2 Galactic Installation
-------

To use the software, first install ROS2 Galactic by running these commands as shown:

.. code-block:: console

   $ sudo apt install software-properties-common
   $ sudo add-apt-repository universe
   $ sudo apt update && sudo apt install curl gnupg lsb-release
   $ sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
   $ echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
   $ sudo apt update # update your apt repo caches
   $ sudo apt install ros-galactic-desktop

Then source the setup of ROS2 on bash by running the following commands:

.. code-block:: console

   $ source /opt/ros/galactic/setup.bash
   $ echo "source /opt/ros/galactic/setup.bash" >> ~/.bashrc
   $ source ~/.bashrc

If you are using Zsh then run the following commands instead to source the ROS2 setup:

.. code-block:: console

   $ echo "source /opt/ros/galactic/setup.zsh" >> ~/.zshrc
   $ source ~/.zshrc

Run Some Examples
-------
To verify that ROS2 Galactic has been installed properly run the following commands:

.. code-block:: console

   $ ros2 run demo_nodes_cpp talker

The output should confirm that the talker is successfully publishing messages:

.. code-block:: console

   [INFO] [1652382860.246687611] [talker]: Publishing: 'Hello World: 1'
   [INFO] [1652382861.250208871] [talker]: Publishing: 'Hello World: 2'
   [INFO] [1652382862.246508551] [talker]: Publishing: 'Hello World: 3'
   ...

In another terminal window, run the example Python listener

.. code-block:: console

   $ ros2 run demo_nodes_py listener
   
The output should confirm that the listener is hearing the published messages:

.. code-block:: console

   [INFO] [1652382936.495044030] [listener]: I heard: [Hello World: 1]
   [INFO] [1652382937.478216343] [listener]: I heard: [Hello World: 2]
   [INFO] [1652382938.487370309] [listener]: I heard: [Hello World: 3]
   ...

