#!/usr/bin/env python
import rospy
from tactilesensors4.msg import *
from smach_based_introspection_framework.msg import tactile
import copy,ipdb
import numpy as np

pub = None

def static_data_preprocessing(data):
    global pub
    taxels0_base_values = np.array([16777, 14002, 18110, 12001, 21747, 16140, 11544, 11711, 26977, 10969, 10823, 10873, 36224, 10387, 10379, 10674, 35944, 11123, 13774, 16186, 11730, 36002, 11230, 15860, 37171, 11928, 11458, 17432])
    taxels1_base_values = np.array([17585, 14837, 18458, 12328, 21947, 16390, 11678, 11982, 26232, 10460, 10788, 10869, 35879, 10122, 10280, 10663, 35630, 11288, 13814, 15850, 11939, 35600, 11413, 15589, 37027, 12185, 11612, 17399])
    taxels0 = np.array(data.taxels[0].values) -  taxels0_base_values
    taxels1 = np.array(data.taxels[1].values) -  taxels1_base_values

#    taxels0_sorted = np.sort(taxels0)
#    taxels1_sorted = np.sort(taxels1)
#    taxels0 = taxels0_sorted[-10:]
#    taxels1 = taxels1_sorted[-10:]
    
    msg = tactile()    
    msg.tactile0_values_0 = taxels0[0]
    msg.tactile0_values_1 = taxels0[1]
    msg.tactile0_values_2 = taxels0[2]
    msg.tactile0_values_3 = taxels0[3]
    msg.tactile0_values_4 = taxels0[4]
    msg.tactile0_values_5 = taxels0[5]
    msg.tactile0_values_6 = taxels0[6]
    msg.tactile0_values_7 = taxels0[7]
    msg.tactile0_values_8 = taxels0[8]
    msg.tactile0_values_9 = taxels0[9] 
    msg.tactile0_values_10 = taxels0[10]
    msg.tactile0_values_11 = taxels0[11]
    msg.tactile0_values_12 = taxels0[12]
    msg.tactile0_values_13 = taxels0[13]
    msg.tactile0_values_14 = taxels0[14]
    msg.tactile0_values_15 = taxels0[15]
    msg.tactile0_values_16 = taxels0[16]
    msg.tactile0_values_17 = taxels0[17]
    msg.tactile0_values_18 = taxels0[18]
    msg.tactile0_values_19 = taxels0[19] 
    msg.tactile0_values_20 = taxels0[20]
    msg.tactile0_values_21 = taxels0[21]
    msg.tactile0_values_22 = taxels0[22]
    msg.tactile0_values_23 = taxels0[23]
    msg.tactile0_values_24 = taxels0[24]
    msg.tactile0_values_25 = taxels0[25]
    msg.tactile0_values_26 = taxels0[26]
    msg.tactile0_values_27 = taxels0[27]

    msg.tactile1_values_0 = taxels1[0]
    msg.tactile1_values_1 = taxels1[1]
    msg.tactile1_values_2 = taxels1[2]
    msg.tactile1_values_3 = taxels1[3]
    msg.tactile1_values_4 = taxels1[4]
    msg.tactile1_values_5 = taxels1[5]
    msg.tactile1_values_6 = taxels1[6]
    msg.tactile1_values_7 = taxels1[7]
    msg.tactile1_values_8 = taxels1[8]
    msg.tactile1_values_9 = taxels1[9] 
    msg.tactile1_values_10 = taxels1[10]
    msg.tactile1_values_11 = taxels1[11]
    msg.tactile1_values_12 = taxels1[12]
    msg.tactile1_values_13 = taxels1[13]
    msg.tactile1_values_14 = taxels1[14]
    msg.tactile1_values_15 = taxels1[15]
    msg.tactile1_values_16 = taxels1[16]
    msg.tactile1_values_17 = taxels1[17]
    msg.tactile1_values_18 = taxels1[18]
    msg.tactile1_values_19 = taxels1[19] 
    msg.tactile1_values_20 = taxels1[20]
    msg.tactile1_values_21 = taxels1[21]
    msg.tactile1_values_22 = taxels1[22]
    msg.tactile1_values_23 = taxels1[23]
    msg.tactile1_values_24 = taxels1[24]
    msg.tactile1_values_25 = taxels1[25]
    msg.tactile1_values_26 = taxels1[26]
    msg.tactile1_values_27 = taxels1[27]


    pub.publish(msg)
    
def main():
    global pub
    rospy.init_node('tactile_preprocessing')
    rospy.Subscriber("/TactileSensor4/StaticData", StaticData, static_data_preprocessing)
    pub = rospy.Publisher('tactile_sensor_data',tactile, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    main()
