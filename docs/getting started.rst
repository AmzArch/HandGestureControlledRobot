Getting Started
===========

Requirements
-------------
  - Python 3.9 or newer
  - ROS2 Galactic
  - VirtualBox with Ubuntu 20.04 or Dual Booted device with Ubuntu 20.04

.. note::

   It is recommended to install Ubuntu 20.04 desktop image on VirtualBox to keep track of changes and revert back in case things go wrong through it's Snapshot feature.


Installation
-------------

Python
""""

.. code-block:: console

   $ pip install -r requirements.txt

If you do not have the requirements.txt file you can run the following commands to get the required python packages installed:

.. code-block:: console

   $ pip install opencv-python pandas mediapipe scikit-learn jupyter


VirtualBox
""""

ROS2 works best with Ubuntu plaftforms and hence it is recommended to use Ubuntu 20.04 for this project since it is stable and has a Long Time Support (LTS) build. You can either dual boot your device with Ubuntu 20.04 desktop or download a virtual box and install an Ubuntu 20.04 desktop image.

  
Install VirtualBox by visiting this link: https://www.virtualbox.org/wiki/Downloads

Download the Ubuntu 20.04 (LTS) desktop image here: https://releases.ubuntu.com/focal/ubuntu-20.04.6-desktop-amd64.iso

After installing VirtualBox follow these instructions here to get it setup with Ubuntu 20.04 desktop image: https://robot-deployment.bitbucket.io/tutorials/virtual%20machine/01-installing-ubuntu-20-on-virtualbox/

ROS2 Galactic Installation
""""

To use the software, first install ROS2 Galactic on your Ubuntu 20.04 desktop environment running in the VirtualBox by running these commands:

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

If you are using Zsh instead of bash, run the following commands to source the ROS2 setup:

.. code-block:: console

   $ echo "source /opt/ros/galactic/setup.zsh" >> ~/.zshrc
   $ source ~/.zshrc

Run Some Examples
""""
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

If all the above steps worked and the listener node is printing messages to your console in sync with the talker node publishing them, ROS2 has been successfully installed.


Essential Tools
""""

.. code-block:: console

    $ sudo apt install net-tools -y
    $ ifconfig
    $ curl -fsSL https://tailscale.com/install.sh | sh
    $ sudo apt install -y tmux


Set Additional Environment Variables
""""

.. code-block:: console

    $ echo "export ROS_DOMAIN_ID=0" >> ~/.bashrc
    $ echo "export ROS_LOCALHOST_ONLY=0" >> ~/.bashrc

More information can be found here: https://docs.ros.org/en/galactic/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html#the-ros-domain-id-variable

Install Other Packages
""""

.. code-block:: console

    $ sudo apt update && sudo apt install -y \
    build-essential \
    cmake \
    git \
    python3-colcon-common-extensions \
    python3-flake8 \
    python3-pip \
    python3-pytest-cov \
    python3-rosdep \
    python3-setuptools \
    python3-vcstool \
    wget

Configure CycloneDDS
""""

Run ip link to get a list of virtualbox network interfaces. In a virtualbox guest you will probably will end up with enp0s3 as your default network interface. If that is the case, copy this code in to a terminal:

.. code-block:: console

    $ cat <<EOT >> ~/cyclonedds_pc.xml
    <CycloneDDS>
    <Domain>
    <General>
    <DontRoute>true</DontRoute>
    <NetworkInterfaceAddress>enp0s3</NetworkInterfaceAddress>
    </General>
    </Domain>
    </CycloneDDS>
    EOT
    $ sudo mv ~/cyclonedds_pc.xml /etc/
    $ echo "export CYCLONEDDS_URI=/etc/cyclonedds_pc.xml" >> ~/.bashrc
    $ source ~/.bashrc

Declare your DDS implementation
""""
.. code-block:: console

    $ echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc

More information can be found in the official documentation of ROS2 from here: https://docs.ros.org/en/galactic/Installation/DDS-Implementations/Working-with-Eclipse-CycloneDDS.html#switch-to-rmw-cyclonedds

Setting Up Turtlebot 4
====

Setting up the Turtlebot 4 might be quite tedious and hence is beyond the scope of this documentation. Please refer to the detailed documentation available at: https://robot-deployment.bitbucket.io/tutorials/turtlebot/02-turtlebot-configuration/ or https://turtlebot.github.io/turtlebot4-user-manual/
