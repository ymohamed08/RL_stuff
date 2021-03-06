import numpy as np
import rospy 
import time
from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import ColorRGBA

pub_say = rospy.Publisher('/cozmo/say', String, queue_size=10)
pub_head_angle = rospy.Publisher('/cozmo/head_angle', Float64, queue_size=10)
pub_lift_hight = rospy.Publisher('/cozmo/lift_height',Float64, queue_size=10)
pub_back_color = rospy.Publisher('/cozmo/backpack_led', ColorRGBA, queue_size=10)

party_count = 0
cheerup_count = 0 
confused_count= 0 
cute_count = 0

rospy.init_node('actions', anonymous=True)

class actions(): 


    def action_party(self): 
        global party_count
        
        say = 'lets party'
        pub_say.publish(say)
        time.sleep(0.3)

        head_angle = (3)
        pub_head_angle.publish(head_angle)

        # party_count += 1 

        for i in range(0,12):
            lift_hight = (1)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)
            lift_hight = (0)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)


        # back_color = ColorRGBA(1,1,1,1)
        # pub_back_color.publish(back_color)

    def action_sadness(self): 
        global cheerup_count
        say = 'i will cheer you up'
        pub_say.publish(say)
        time.sleep(0.3)

        head_angle = (1)
        pub_head_angle.publish(head_angle)

        # cheerup_count += 1 


        for i in range(0,4):
            lift_hight = (0.2)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)
            lift_hight = (0)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)

        # back_color = ColorRGBA(1,1,1,1)
        # pub_back_color.publish(back_color)

    def action_confused_cute(self): 
        global confused_count
        say = 'What are we doing again?'
        pub_say.publish(say)
        time.sleep(0.3)

        head_angle = (3)
        pub_head_angle.publish(head_angle)
        # confused_count += 1 


        for i in range(0,2):
            lift_hight = (0.2)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)
            lift_hight = (0)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)

        # back_color = ColorRGBA(1,1,1,1)
        # pub_back_color.publish(back_color)
    def action_cute(self): 
        global cute_count
        say = 'You are cute'
        pub_say.publish(say)
        time.sleep(0.3)

        head_angle = (3)
        pub_head_angle.publish(head_angle)
        # cute_count += 1 


        for i in range(0,1):
            lift_hight = (0.2)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)
            lift_hight = (0)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)

        # back_color = ColorRGBA(1,1,1,1)
        # pub_back_color.publish(back_color)
