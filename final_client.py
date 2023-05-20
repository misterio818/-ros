#!/usr/bin/env python3
import rospy
from std_srvs.srv import Empty

def final_client():
    rospy.wait_for_service('/hi')
    try:
        hi_service = rospy.ServiceProxy('/hi', Empty)
        response = hi_service()
        rospy.loginfo("Service Response: %s", response)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == '__main__':
    rospy.init_node('final_client')
    final_client()
