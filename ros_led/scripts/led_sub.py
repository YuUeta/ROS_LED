#! /usr/bin/env python
import rospy
import RPi.GPIO as GPIO
import time

from std_msgs.msg import String

#COUNT = 3
PIN_LIST = {"a":4, "b":17,"c":5,"d":6}
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(PIN, GPIO.OUT)

#SetUp GPIO
for pin in PIN_LIST.values():
    #print(pin)
    GPIO.setup(pin, GPIO.OUT)


def callback(data):
    #rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
    print("data: " + data.data)
    cnt = data.data
    #print(cnt)
    if(cnt == 'q'):
        for pin in PIN_LIST.values():
            GPIO.output(pin,False)
    elif(cnt in PIN_LIST):
        GPIO.output(PIN_LIST[cnt],True)
    else:
        print("No Item")

def listener():
    rospy.init_node('led_sub', anonymous=True)
    rospy.Subscriber("led", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
