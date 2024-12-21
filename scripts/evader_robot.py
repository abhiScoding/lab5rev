#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import random


def callback(data):

    global front_ranges
    front_ranges = data.ranges[90:270]
    # print(front_ranges)
    return 0

def evader():
    rospy.init_node('evader', anonymous=True)

    rospy.Subscriber("/robot_0/base_scan", LaserScan, callback)
    pub = rospy.Publisher("/robot_0/cmd_vel", Twist, queue_size=10)

    vel = Twist()
    rate = rospy.Rate(10)
    rospy.sleep(1)
    while not rospy.is_shutdown():

    
        if min(front_ranges) < 1.5:
            vel.linear.x = 0
            vel.angular.z = random.uniform(0, 6.3)
        else:
            vel.angular.z = 0
            vel.linear.x = 2
        
        pub.publish(vel)
        rate.sleep()


if __name__ == '__main__':

    try:
        evader()
    except rospy.ROSInterruptException:
        pass