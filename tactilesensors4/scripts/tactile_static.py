#!/usr/bin/env python
from std_srvs.srv import Trigger,TriggerResponse
import rospy
from tactilesensors4.msg import *
from smach_based_introspection_framework.msg import tactile_static
import copy,ipdb
import numpy as np

pub   = None
data0 = None
data1 = None 
tmp_0 = 0
tmp_1 = 0

def reset(req):
    global pub,tmp_0,tmp_1, data0, data1
    res = TriggerResponse()
    tmp_0 = copy.deepcopy(data0)
    tmp_1 = copy.deepcopy(data1)
    return res 

def static_data_preprocessing(data):
    global pub, tmp_0, tmp_1, data0, data1

    data0 = data.taxels[0].values
    data1 = data.taxels[1].values

    taxels1 = np.array(data0) -  np.array(tmp_0)
    taxels2 = np.array(data1) -  np.array(tmp_1)

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
    rospy.Service('tactile_reset_service', Trigger, reset)
    pub = rospy.Publisher('/tactile_sensor_data',tactile_static, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    main()
