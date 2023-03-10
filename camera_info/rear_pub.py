#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from sensor_msgs.msg import CameraInfo

def publish_camera_info(width, height, fx, fy, cx, cy, k1, k2, k3, k4):
    # Initialize ROS node
    rospy.init_node('camera_info_publisher')

    # Initialize camera info message
    camera_info_msg = CameraInfo()

    # Set camera info message parameters
    camera_info_msg.width = width
    camera_info_msg.height = height
    camera_info_msg.K = [fx, 0, cx, 0, fy, cy, 0, 0, 1]
    camera_info_msg.P = [fx, 0, cx, 0, 0, fy, cy, 0, 0, 0, 1, 0]
    camera_info_msg.distortion_model="equidistant"
    camera_info_msg.D = [k1, k2, k3, k4]
    
    # Initialize publisher
    pub = rospy.Publisher('/rear_cam/camera_info', CameraInfo, queue_size=10)

    # 10Hz 마다 반복.
    rate = rospy.Rate(10)

    # Initialize publisher
    while not rospy.is_shutdown():
        # Publish camera info message
        pub.publish(camera_info_msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        # Call the publish_camera_info function with your desired camera parameters
        publish_camera_info(
         width = 1920, height = 1080, 
         fx = 584.9987710608711, fy = 586.018158433203, 
         cx = 1017.7654596437173, cy = 608.3373015582448, 
         k1 = -0.020816152115767796, k2 = 0.010799634587420281, 
         k3 = -0.005262927922546367, k4 = 0.0003466164368110067, 
         )
    except rospy.ROSInterruptException:
        pass
