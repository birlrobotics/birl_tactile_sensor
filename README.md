# BIRL Tactile Sensor 
There are 3 possibilities to interface with the sensors:  

- You can also use the ROS package by downloading **this package** . The serial communication stack is provided by this package. Until the contrary is proved, the package is compatible with any revision of ROS starting from "Fuerte".

- Using the Sensor Graphical User Interface available on Wiwndows. The source code and installation file is publicly available [here](https://github.com/birlrobotics/CoRoSensorUI).  

- Developing your own serial communication software stack. The sensor protocol is documented in research_group_central google driver tactile_sensor_materials folder. 

A Video showing some of the sensor's capabilities and characteristics is [here](https://www.youtube.com/watch?v=ihfxfyxzeoY&feature=youtu.be). 


## The ROS interface node
### PollData4
Responsible for extracting and publishing the static, dynamic and IMU data from tactile sensors. The results are then published on `/TactileSensor3/StaticData`, `/TactileSensor3/DynamicData` or `/TactileSensor3/DynamicAndIMUData` respectively. 
The static data are published in format std_msgs::Int32MultiArray while dynamic and imu data are published in format std_msgs::Float64.

### DataListener4
DataListener.cpp - A example script that listens for any kind of data