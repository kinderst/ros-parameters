#!/usr/bin/env python  
import rospy


if __name__ == '__main__':
    rospy.init_node('tf2_turtle_broadcaster')
    custom_message = rospy.get_param('~mymsg')
    rospy.loginfo('Parameter %s has value %s', rospy.resolve_name('~mymsg'), custom_message)
    # print
    rospy.spin()