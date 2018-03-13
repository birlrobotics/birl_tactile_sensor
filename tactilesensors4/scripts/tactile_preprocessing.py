#!/usr/bin/env python
import rospy
from tactilesensors4.msg import *
from smach_based_introspection_framework.msg import tactile
import copy,ipdb
import numpy as np

pub = None
prev_data = None
def static_data_preprocessing(data):
    global pub
    taxels0_base_values = np.array([16777, 14002, 18110, 12001, 21747, 16140, 11544, 11711, 26977, 10969, 10823, 10873, 36224, 10387, 10379, 10674, 35944, 11123, 13774, 16186, 11730, 36002, 11230, 15860, 37171, 11928, 11458, 17432])
    taxels1_base_values = np.array([17585, 14837, 18458, 12328, 21947, 16390, 11678, 11982, 26232, 10460, 10788, 10869, 35879, 10122, 10280, 10663, 35630, 11288, 13814, 15850, 11939, 35600, 11413, 15589, 37027, 12185, 11612, 17399])
    taxels0 = np.array(data.taxels[0].values) -  taxels1_base_values
    taxels1 = np.array(data.taxels[1].values) -  taxels2_base_values
    taxels0_sorted = np.sort(taxels1)
    taxels1_sorted = np.sort(taxels2)
    taxels0 = taxels0_sorted[-5:]
    taxels1 = taxels1_sorted[-5:]

    if prev_data == None:
        prev_data[0] = taxels0
        prev_data[1] = taxels1
        return
    elif:
        taxels0_diff = taxels0 - prev_data[0]
        taxels1_diff = taxels1 - prev_data[1]
        prev_data[0] = taxels0
        prev_data[1] = taxels1

    msg = tactile()    
    msg.tactile_values_0 = taxels0_diff[0]
    msg.tactile_values_1 = taxels0_diff[1]
    msg.tactile_values_2 = taxels0_diff[2]
    msg.tactile_values_3 = taxels0_diff[3]
    msg.tactile_values_4 = taxels0_diff[4]
    msg.tactile_values_5 = taxels1_diff[0]
    msg.tactile_values_6 = taxels1_diff[1]
    msg.tactile_values_7 = taxels1_diff[2]
    msg.tactile_values_8 = taxels1_diff[3]
    msg.tactile_values_9 = taxels1_diff[4]   
    pub.publish(msg)
    
def main():
    global pub
    rospy.init_node('tactile_preprocessing')
    rospy.Subscriber("/TactileSensor4/StaticData", StaticData, static_data_preprocessing)
    pub = rospy.Publisher('tactile_sensor_data',tactile, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    main()
