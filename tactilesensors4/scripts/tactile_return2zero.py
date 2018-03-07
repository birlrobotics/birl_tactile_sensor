#!/usr/bin/env python

from std_srvs.srv import Trigger,TriggerResponse
import rospy
from tactilesensors4.msg  import *
from std_msgs.msg import Int64
import copy,ipdb

A = None
pub = None 
tmp = 0

def cb(req):
    global A,tmp
    res = TriggerResponse()
    tmp = copy.deepcopy(A)
    return res
    


def static_data_cb(data):
    global A,pub,tmp
    # ipdb.set_trace()
    A = sum(data.taxels[0].values)+sum(data.taxels[1].values)
    msg = Int64()
    msg.data = A - tmp
    pub.publish(msg)

def main():
    global pub
    rospy.init_node('tactile_sensor2_zero')
    rospy.Subscriber("/TactileSensor4/StaticData", StaticData, static_data_cb)
    rospy.Service('tactile_texel_sum_reset', Trigger, cb)
    pub = rospy.Publisher('tactile_texel_sum',Int64, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    main()