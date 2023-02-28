#!/usr/bin/env python  
import rospy


if __name__ == '__main__':
    rospy.init_node('my_custom_node_name')
    custom_message = rospy.get_param('~mymsg')
    rospy.loginfo('Parameter %s has value %s', rospy.resolve_name('~mymsg'), custom_message)
    # print
    rospy.spin()
