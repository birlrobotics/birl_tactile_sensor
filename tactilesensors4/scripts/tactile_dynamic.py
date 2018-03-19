#!/usr/bin/env python
import rospy
from tactilesensors4.msg import *
from smach_based_introspection_framework.msg import tactile_dynamic
import copy,ipdb
import numpy as np

pub = None 
def _data_preprocessing(data):
    global pub
    msg = tactile_dynamic()
    msg.tactile_values_0 = data.data[0].value
    msg.tactile_values_1 = data.data[1].value
    rospy.loginfo(msg)
    pub.publish(msg)
    
def main():
    global pub
    rospy.init_node('tactile_preprocessing')
    rospy.Subscriber("/TactileSensor4/Dynamic", Dynamic, _data_preprocessing)
    pub = rospy.Publisher('tactile_sensor_data',tactile_dynamic, queue_size=10)
    rospy.loginfo('connected, publishing')
    rospy.spin()

if __name__ == "__main__":
    main()
