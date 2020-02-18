#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String

def callback(msg):
	rospy.loginfo("Yeah: {}".format(msg.data))

def memory_subscriber():
	rospy.init_node("subscriptor", anonymous=True)
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()

if __name__ == "__main__":
	try:
		memory_subscriber()
	except rospy.ROSInterruptException:
		pass
