#!/usr/bin/env python
import rospy
from tactilesensors4.msg import *
from smach_based_introspection_framework.msg import tactile
import copy,ipdb
import numpy as np

pub = None 
def static_data_preprocessing(data):
    global pub
    taxels1_base_values = np.array([16884, 14131, 18246, 12081, 21928, 16342, 11646, 11801, 27208, 10953, 10925, 10974, 36376, 10554, 10482, 10776, 36159, 11215, 13934, 16362, 11855, 36329, 11364, 16047, 37449, 12054, 11610, 17657])
    taxels2_base_values = np.array([17325, 14641, 18280, 12145, 21834, 16248, 11538, 11833, 26077, 10372, 10689, 10787, 35742, 10021, 10187, 10557, 35477, 11163, 13711, 15729, 11805, 35462, 11285, 15483, 36841, 12052, 11457, 17275])
    taxels1 = np.array(data.taxels[0].values) -  taxels1_base_values
    taxels2 = np.array(data.taxels[1].values) -  taxels2_base_values
#    taxels1 = copy.deepcopy(np.subtract(data.taxels[0].values, taxels1_base_values))
#    taxels2 = copy.deepcopy(np.subtract(data.taxels[1].values, taxels2_base_values))
#    taxels1 = np.divide(copy.deepcopy(data.taxels[0].values), 10000.00)
#    taxels2 = np.divide(copy.deepcopy(data.taxels[1].values), 10000.00)
#    rospy.loginfo(data.taxels[0].values)
    taxels1_sorted = np.sort(taxels1)
    taxels2_sorted = np.sort(taxels2)
    taxels1 = taxels1_sorted[-5:]
    taxels2 = taxels2_sorted[-5:]

    ''''
    if (np.max(taxels1) or abs(np.min(taxels1))) > 1000:
        rospy.loginfo('tactile[0] sensor noise...')
        return
    if (np.max(taxels2) or abs(np.min(taxels2))) > 1000:
        rospy.loginfo('tactile[1] sensor noise...')
        return
    '''


    msg = tactile()    
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
    pub = rospy.Publisher('tactile_sensor_data',tactile, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    main()
