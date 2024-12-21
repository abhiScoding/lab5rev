#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math
import tf

vel = Twist()

# pursuer controller
def pursuer():
    rospy.init_node('pursuer', anonymous = True)
    listener = tf.TransformListener()
    pub = rospy.Publisher('/robot_1/cmd_vel', Twist, queue_size=10)
    
    rate = rospy.Rate(10)
    rospy.sleep(1.5)
    while not rospy.is_shutdown():

        try:
            (trans, rot) = listener.lookupTransform("/robot_1/odom", "/robot_0/odom", rospy.Time(0))
        except (tf.Exception, tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        angular = 4.1* math.atan2(trans[1], trans[0])
        linear = 0.52* math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        vel.linear.x = linear
        vel.angular.z = angular

        pub.publish(vel)
        rate.sleep()
      

if __name__ == '__main__':

    try:
        pursuer()
    except rospy.ROSInterruptException:
        pass

