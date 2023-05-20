#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

def callback(data):
    rospy.loginfo("Received std_id: %s", data.data)

def subscribe_std_id():
    rospy.init_node('final_subscriber', anonymous=True)
    rospy.Subscriber('/std_id', Int64, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscribe_std_id()
    except rospy.ROSInterruptException:
        pass
