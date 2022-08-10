#!/usr/bin/env python

import rospy
import actionlib

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion

waypoints = {0: Pose(Point(1.0, 0.2, 0.0), Quaternion(0.0, 0.0, 0.0, -0.2)),
             1: Pose(Point(0.5, 0.9, 0.0), Quaternion(0.0, 0.0, 0.0, 0.3)),
             2: Pose(Point(0.3, 0.5, 0.0), Quaternion(0.0, 0.0, 0.0, 0.4)),
             3: Pose(Point(1.0, 0.2, 0.0), Quaternion(0.0, 0.0, 0.0, -0.5))}

def Waypoint(wp):
    goal = MoveBaseGoal()
    goal.target_pose.pose = waypoints[wp]
    goal.target_pose.header.frame_id = 'map'

    return goal

def Nav(Wp):
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    client.send_goal(Waypoint(Wp))
    client.wait_for_result()

    return client.get_goal_status_text()   

if __name__ == '__main__':
    try:
        rospy.init_node('limo_navigator_node')

        for i in range(4):
            result = Nav(i)
            print(result)
    except rospy.ROSInterruptException as err:
        print("Error: ", err)
