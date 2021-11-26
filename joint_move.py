#!/usr/bin/env python3
# license removed for brevity
import rospy
from sensor_msgs.msg import JointState

joint_publisher = rospy.Publisher('/custom_joint_states', JointState, queue_size=10)
joint = JointState()
joint.name = ["base", "shoulder", "elbow", "wrist", "wrist_twist", "gripper"]
joint.position = [0, 0, 0, 0, 0, 0]

def move0():
    global joint
    joint.position[0] = 0
    joint.position[1] = 0
    joint.position[2] = 0
    joint.position[3] = 0
    joint.position[4] = 0


    joint_publisher.publish(joint)
    rospy.sleep(1)

def move1():
    global joint
    joint.position[0] = 0
    joint.position[1] = 0.15
    joint.position[2] = 0
    joint.position[3] = 0
    joint.position[4] = 0


    joint_publisher.publish(joint)
    rospy.sleep(0.5)

def movea():
    global joint
    #joint.postion[1]==-0.72 and joint.postion[2]==-0.24 and joint.postion[3]==0.96:
    for x in range(23):
        joint.position[1]-=0.03
        joint.position[2]-=0.03
        joint.position[3]+=0.06
        joint_publisher.publish(joint)
        rospy.sleep(0.05)


    
def moveb():
    global joint
    #joint.postion[1]==-0.72 and joint.postion[2]==-0.24 and joint.postion[3]==0.96:
    for x in range(23):
        joint.position[1]+=0.03
        joint.position[2]+=0.03
        joint.position[3]-=0.06
        joint_publisher.publish(joint)
        rospy.sleep(0.05)

def movepp1a():
    global joint
    #joint.postion[1]==-0.72 and joint.postion[2]==-0.24 and joint.postion[3]==0.96:
    for x in range(22):
        joint.position[1]-=0.02
        joint_publisher.publish(joint)
        rospy.sleep(0.05)

def movepp1b():
    global joint
    #joint.postion[1]==-0.72 and joint.postion[2]==-0.24 and joint.postion[3]==0.96:
    for x in range(22):
        joint.position[2]+=0.02
        joint_publisher.publish(joint)
        rospy.sleep(0.05)

def movepp1c():
    global joint
    #joint.postion[1]==-0.72 and joint.postion[2]==-0.24 and joint.postion[3]==0.96:
    for x in range(22):
        joint.position[3]-=0.07
        joint_publisher.publish(joint)
        rospy.sleep(0.05)

    
def movepp2a():
    global joint
    #joint.postion[1]==-0.44 and joint.postion[2]==0.44 and joint.postion[3]==1.54:
    for x in range(22):
        joint.position[3]+=0.07
        joint_publisher.publish(joint)
        rospy.sleep(0.05)

def movepp2b():
    global joint
    #joint.postion[1]==-0.44 and joint.postion[2]==0.44 and joint.postion[3]==1.54:
    for x in range(22):

        joint.position[2]-=0.02

        joint_publisher.publish(joint)
        rospy.sleep(0.05)

def movepp2c():
    global joint
    #joint.postion[1]==-0.44 and joint.postion[2]==0.44 and joint.postion[3]==1.54:
    for x in range(22):
        joint.position[1]+=0.02
        joint_publisher.publish(joint)
        rospy.sleep(0.05)

def grip_cl():
    global joint
    for x in range(22):
        joint.position[5]+=0.07
        joint_publisher.publish(joint)
        rospy.sleep(0.05)

def grip_op():
    global joint
    for x in range(22):
        joint.position[5]-=0.07
        joint_publisher.publish(joint)
        rospy.sleep(0.05)


if __name__ == '__main__':
    rospy.init_node('Movement')
    try:
        move0()
        #grip_cl()

        while not rospy.is_shutdown():
            #Repeatability
            #movea()
           # moveb()
            move0()

            #Pick and place
            movepp1a()
            movepp1b()
            movepp1c()
            grip_cl()
            grip_op()
            movepp2a()
            movepp2b()
            movepp2c()

            
            
            
    except rospy.ROSInterruptException:
        pass