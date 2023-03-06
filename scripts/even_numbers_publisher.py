#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('even_numbers_publisher')

pub = rospy.Publisher('even_numbers', Int32, queue_size=10)

rate = rospy.Rate(10)

def start_even_numbers_publisher():

    count = 0

    while not rospy.is_shutdown():
        rospy.loginfo(count)
        if count % 2 == 0:
            pub.publish(count)
        count += 1
        
        rate.sleep()

try:
    start_even_numbers_publisher()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')