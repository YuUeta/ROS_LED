#! /usr/bin/env python
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('led', String, queue_size=10)
    rospy.init_node('led_pub', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        str = raw_input("your data: ")
        #str = "hello world %s"%rospy.get_time()
        #rospy.loginfo(str)
        pub.publish(str)

        r.sleep()
        

if __name__ == '__main__':
    talker()
