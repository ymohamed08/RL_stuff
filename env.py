from logging import info
import gym
import time 
from gym import spaces
from cozmo_actions import actions
import rospy 
from openface2_ros.msg import Faces

class CozmoEnv(gym.Env):

  def __init__(self):
    super(CozmoEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:

    self.action_maps = {0 : actions.action_party, 1 : actions.action_sadness}

    self.action_space = spaces.Discrete(2)
    self.observation_space = spaces.Box(0, 1, [18])
    self.action_units = None

  def data_callback(self,data):
    # print(data.faces[0].action_units)
    self.action_units = data.faces[0].action_units
 




  def step(self, action):
    reward = 0
    step_action = self.action_maps[action]
    step_action()
    time.sleep(5)
    if self.action_units:
      observation = [unit.intensity for unit in self.action_units]
    else:
      observation = [0] * 18
    print(observation)
    print(len(observation))
    if observation[0]  > 0.5: 
        reward = 1 
    
    return observation, reward, False, {}
  def reset(self):
    return [0] * 18

  def close (self):
    pass




# rospy.spin()
