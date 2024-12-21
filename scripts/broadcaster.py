#!/usr/bin/env python3

import rospy
import tf
from nav_msgs.msg import Odometry



def callback(odom, robotname):
    br = tf.TransformBroadcaster()
    br.sendTransform((odom.pose.pose.position.x, odom.pose.pose.position.y, odom.pose.pose.position.z),
                     (odom.pose.pose.orientation.x, odom.pose.pose.orientation.y,
                      odom.pose.pose.orientation.z, odom.pose.pose.orientation.w),
                     rospy.Time.now(),
                     f"/{robotname}/odom",
                     "world")


def tf_broadcast():
    rospy.init_node('robot_broadcatster', anonymous=True)
    robotname = rospy.get_param('~robot')
    print(f"robot name:{robotname}")
    rospy.Subscriber(f"/{robotname}/odom", Odometry, callback, robotname)

    rospy.spin()
  

if __name__ == '__main__':

    try:
        tf_broadcast()
    except rospy.ROSInterruptException:
        pass