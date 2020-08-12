#!/usr/bin/env python3
# license removed for brevity
import rospy
from beginner_tutorials.msg import my_msg

def talker():
    pub = rospy.Publisher('chatter', my_msg, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    count = 1

    while not rospy.is_shutdown():
       
        msg = my_msg()
        msg.id = count
        msg.title = " hello"
        msg.content = " from python"

        pub.publish(msg)
        rospy.loginfo(str(msg.id) + msg.title + msg.content)
        count = count + 1
        frq = rospy.get_param("/print_freq",1)
        rospy.sleep(frq)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
