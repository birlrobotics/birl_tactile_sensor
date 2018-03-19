#!/usr/bin/env python
import rospy
from tactilesensors4.msg import *
from smach_based_introspection_framework.msg import tactile_static
import copy,ipdb
import numpy as np

pub = None
def static_data_preprocessing(data):
    global pub
    taxels1_base_values = np.array([16970, 14215, 18313, 12150, 21927, 16321, 11678, 11854, 27145, 10963, 10929, 10993, 36377, 10492, 10473, 10794, 36170, 11209, 13874, 16319, 11901, 36179, 11369, 16020, 37404, 12054, 11590, 17609])
    taxels2_base_values = np.array([17777, 14998, 18550, 12515, 22085, 16456, 11742, 12089, 26353, 10498, 10836, 10933, 35987, 10156, 10319, 10717, 35729, 11322, 13837, 15917, 12071, 35630, 11487, 15648, 37144, 12271, 11653, 17458])

    taxels1 = np.array(data.taxels[0].values) -  taxels1_base_values
    taxels2 = np.array(data.taxels[1].values) -  taxels2_base_values

    taxels1_sorted = np.sort(taxels1)
    taxels2_sorted = np.sort(taxels2)
    taxels1 = taxels1_sorted[-5:]
    taxels2 = taxels2_sorted[-5:]

    msg = tactile_static()
    msg.tactile_values_0 = taxels1[0]
    msg.tactile_values_1 = taxels1[1]
    msg.tactile_values_2 = taxels1[2]
    msg.tactile_values_3 = taxels1[3]
    msg.tactile_values_4 = taxels1[4]
    msg.tactile_values_5 = taxels2[0]
    msg.tactile_values_6 = taxels2[1]
    msg.tactile_values_7 = taxels2[2]
    msg.tactile_values_8 = taxels2[3]
    msg.tactile_values_9 = taxels2[4]
    pub.publish(msg)

def main():
    global pub
    rospy.init_node('tactile_preprocessing')
    rospy.Subscriber("/TactileSensor4/StaticData", StaticData, static_data_preprocessing)
    pub = rospy.Publisher('tactile_sensor_data',tactile_static, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    main()
