#!/usr/bin/env python3

import rospy
from std_srvs.srv import Empty
from rospy_tutorials.srv import Empty

def handle_hi(request):
    rospy.loginfo("Hi, My name is watcharaphon")
    return []

def final_server():
    rospy.init_node('final_server')
    s = rospy.Service('/hi', Empty, handle_hi)
    rospy.loginfo("Ready to say Hi")
    rospy.spin()

if __name__ == '__main__':
    final_server()
