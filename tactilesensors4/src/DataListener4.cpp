/****************************************************************************************
//DataListener V4.1
//Author: Jean-Philippe Roberge Ing, M.Sc.A.
//Date: June 9th 2015
//Affiliations: Laboratoire de commande et de robotique (École de technologie supérieure)
//
//Description:  DataListener.cpp - A example script that listens for any kind of data
//              coming from any sensor(s).
//
//______________________________________________________________________________________
//Version: 1.0 : April 2nd 2015
//Version: 1.1 : June 9th 2015
//
//Last Modified: April 2nd 2015 - Initial release
//               June 9th 2015  - Modified to include acquisition of multiple sensors at
//                                the same time --> e.g. by adding option -sensor 1:10
//                                on the command line
//               October 21st 2016 - Modifications that now allow to listen to data that
//                                has been sent using the new implemented communication
//                                protocol. Just uncomment the core of the callback
//                                related to the data type in which you are interested.
****************************************************************************************/



#include "ros/ros.h"
#include "std_msgs/Int32MultiArray.h"
#include "std_msgs/Float64.h"
#include "tactilesensors4/StaticData.h"
#include "tactilesensors4/Dynamic.h"
#include "tactilesensors4/Accelerometer.h"
#include "tactilesensors4/Gyroscope.h"
#include "tactilesensors4/EulerAngle.h"
#include "tactilesensors4/Magnetometer.h"

void staticdataCallback(const tactilesensors4::StaticData::ConstPtr &msg)
{
    //    for (int i=0; i<msg->taxels.data()->values.size();i++)
    //    {
    //        ROS_INFO("We have received static data: [%i] and [%i] from the sensors", msg->taxels[0].values[i],msg->taxels[1].values[1]);
    //    }
}

void dynamicCallback(const tactilesensors4::Dynamic::ConstPtr &msg)
{
    //    ROS_INFO("We have received dynamic data: [%i] and [%i] from the sensors", msg->data[0].value,msg->data[1].value);
}

void accelerometerCallback(const tactilesensors4::Accelerometer::ConstPtr &msg)
{
    //    ROS_INFO("We have received accelerometer data from sensor #1: ax=[%i], ay=[%i] and az=[%i]", msg->data[0].values[0], msg->data[0].values[1], msg->data[0].values[2]);
    //    ROS_INFO("We have received accelerometer data from sensor #2: ax=[%i], ay=[%i] and az=[%i]", msg->data[1].values[0], msg->data[1].values[1], msg->data[1].values[2]);
}

void gyroscopeCallback(const tactilesensors4::Gyroscope::ConstPtr &msg)
{
//    ROS_INFO("We have received gyroscope data from sensor #1: gx=[%i], gy=[%i] and gz=[%i]", msg->data[0].values[0], msg->data[0].values[1], msg->data[0].values[2]);
//    ROS_INFO("We have received gyroscope data from sensor #2: gx=[%i], gy=[%i] and gz=[%i]", msg->data[1].values[0], msg->data[1].values[1], msg->data[1].values[2]);
}

void magnetometerCallback(const tactilesensors4::Magnetometer::ConstPtr &msg)
{
//    ROS_INFO("We have received magnetometer data from sensor #1: mx=[%i], my=[%i] and mz=[%i]", msg->data[0].values[0], msg->data[0].values[1], msg->data[0].values[2]);
//    ROS_INFO("We have received magnetometer data from sensor #2: mx=[%i], my=[%i] and mz=[%i]", msg->data[1].values[0], msg->data[1].values[1], msg->data[1].values[2]);
}

void euleranglesCallback(const tactilesensors4::EulerAngle::ConstPtr &msg)
{
    //    ROS_INFO("We have received euler angle data from sensor #1: roll=[%f], pitch=[%f] and yaw=[%f]", msg->data[0].values[0], msg->data[0].values[1], msg->data[0].values[2]);
    //    ROS_INFO("We have received euler angle data from sensor #2: roll=[%f], pitch=[%f] and yaw=[%f]", msg->data[1].values[0], msg->data[1].values[1], msg->data[1].values[2]);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "listener");
    ros::NodeHandle n;
    ros::Subscriber sub_static = n.subscribe("/TactileSensor4/StaticData", 1000, staticdataCallback);
    ros::Subscriber sub_dynamic = n.subscribe("/TactileSensor4/Dynamic", 1000, dynamicCallback);
    ros::Subscriber sub_accelerometer = n.subscribe("TactileSensor4/Accelerometer", 1000, accelerometerCallback);
    ros::Subscriber sub_gyroscope = n.subscribe("/TactileSensor4/Gyroscope",1000,gyroscopeCallback);
    ros::Subscriber sub_magnetometer= n.subscribe("/TactileSensor4/Magnetometer",1000,magnetometerCallback);
    ros::Subscriber sub_eulerangles = n.subscribe("/TactileSensor4/EulerAngle",1000, euleranglesCallback);

    ros::spin();
    return 0;
}
