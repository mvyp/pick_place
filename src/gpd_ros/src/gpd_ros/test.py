

from turtle import width
import rospy
from gpd_ros.msg import GraspConfig
 
def talker():
    pub = rospy.Publisher('goal_pose', GraspConfig, queue_size=10)
    rospy.init_node('talker')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        goal = GraspConfig()
        goal.position.x = 0.705
        goal.position.y = 0.005
        goal.position.z = 0.680

        goal.approach.x = 0
        goal.approach.y = 1
        goal.approach.z = 0

        goal.binormal.x = 0
        goal.binormal.y = 0
        goal.binormal.z = 1

        goal.axis.x = 1
        goal.axis.y = 0
        goal.axis.z = 0

        goal.width.data = 1000

        goal.sample.x = 0
        goal.sample.y = 0
        goal.sample.z = 0
        
        pub.publish(goal)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass