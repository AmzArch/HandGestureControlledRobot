Troubleshooting
==============

VirtualBox/Ubuntu/ROS2
------

- Can only see */parameter_events* and */rosout* topics when ros2 topic list command is run:

  - Go to VirtualBox settings and Network and make sure the network type is Bridged instead of NAT.
  - Restart your virtual box.


Turtlebot 4
-------
- Create3 topics suddenly disappeared but can still see the Raspberry Pi 4 topics:
  
  - Re-flash the SD card on the Raspberry Pi 4 in the Turtlebot 4 with the turtlebot image found here: http://download.ros.org/downloads/turtlebot4/turtlebot4_lite_galactic_0.1.3.zip
  - Run the following commands:
  
  .. code-block:: console

      $ sudo systemctl stop unattended-upgrades
      $ sudo apt-get purge unattended-upgrades
        
  - Restart Turtlebot 4


Network Issues
-----

- Configuring the netplan configuration yaml file is quite tricky and tedious to figure out. Here is a sample /etc/netplan/50-cloud-init.yaml template file to make things easier:

  - Replace the <SSID_HERE> with the network SSID and the <PASSWORD_HERE> with the network password respectively.

.. code-block:: yaml

    network: 
        version: 2 
        ethernets: 
            eth0: 
                dhcp4: true 
                optional: true 
                addresses: [192.168.185.3/24] 
            usb0: 
                dhcp4: false 
                optional: true 
                addresses: [192.168.186.3/24] 
        version: 2 
        wifis: 
            renderer: NetworkManager 
            wlan0: 
                optional: true 
                access-points: 
                    <SSID_HERE>: 
                        password: <PASSWORD_HERE>
                dhcp4: false
                addresses: 
                    - 10.0.10.21/24
                routes:
                    - to: default
                      via: 10.0.10.1
                nameservers:
                    addresses:
                    - 1.1.1.1
                    - 1.0.0.1
                    - 8.8.8.8
                    - 8.8.4.4

General Issues
----

- The Raspberry Pi 4 needs to connect to 5GHz band of the Wifi Router and the Create3 module needs to connect to the 2.4Ghz band of the Wifi router. So it is required to have a dual band Wifi router.
