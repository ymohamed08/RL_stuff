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

rospy.init_node('actions', anonymous=True)

class actions: 
    def action_party(): 
        
        say = 'lets party'
        pub_say.publish(say)

        head_angle = (3)
        pub_head_angle.publish(head_angle)

        for i in range(0,12):
            lift_hight = (1)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)
            lift_hight = (0)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)

        # back_color = ColorRGBA(1,1,1,1)
        # pub_back_color.publish(back_color)
    def action_sadness(): 
        say = 'i will cheer you up'
        pub_say.publish(say)

        head_angle = (1)
        pub_head_angle.publish(head_angle)

        for i in range(0,4):
            lift_hight = (0.2)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)
            lift_hight = (0)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)

        # back_color = ColorRGBA(1,1,1,1)
        # pub_back_color.publish(back_color)

 def action_confused_cute(): 
        say = 'What are we doing again?'
        pub_say.publish(say)

        head_angle = (1)
        pub_head_angle.publish(head_angle)

        for i in range(0,2):
            lift_hight = (0.2)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)
            lift_hight = (0)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)

        # back_color = ColorRGBA(1,1,1,1)
        # pub_back_color.publish(back_color)
 def action_cute(): 
        say = 'Kawaiii'
        pub_say.publish(say)

        head_angle = (1)
        pub_head_angle.publish(head_angle)

        for i in range(0,1):
            lift_hight = (0.2)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)
            lift_hight = (0)
            pub_lift_hight.publish(lift_hight)
            time.sleep(0.3)

        # back_color = ColorRGBA(1,1,1,1)
        # pub_back_color.publish(back_color)
