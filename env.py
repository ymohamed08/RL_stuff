from logging import info
from collections import deque
import gym
import time 
from gym import spaces
from torch.nn.modules.module import register_module_forward_hook
from cozmo_actions import actions
import rospy 
import keyboard
from openface2_ros.msg import Faces
import time 

class CozmoEnv(gym.Env):
  
  def __init__(self):
    super(CozmoEnv, self).__init__()
    self.queue = deque(maxlen=7)
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:

    self.action_maps = {0 : actions.action_party, 1 : actions.action_sadness, 2 : actions.action_confused_cute, 3 : actions.action_cute}

    self.action_space = spaces.Discrete(4)
    self.observation_space = spaces.Box(0, 1, [2])
    self.action_units = None
    
    self.movingAvgRewards = []
    self.actionCounter = [0, 0, 0, 0]

  def data_callback(self,data):
    # print(data.faces[0].action_units)
    self.action_units = data.faces[0].action_units
 




  def step(self, action):
    reward = 0
    self.actionCounter[action] += 1
    step_action = self.action_maps[action]
    step_action(self)
    # print("smile! or don't, I don't care")
    start_time = time.time()
    smile_count = 0
    while time.time() - start_time < 5.0:
      
      if self.action_units:
        observation = [self.action_units[8].intensity/5, self.action_units[13].intensity/5]
      else:
        observation = [0] * 2
      
      if observation[0]  > 0.3/5 and observation[1] > 0.5/5: 
        smile_count += 1
      time.sleep(0.1)

    if smile_count >= 5:
      reward = 1
    print(smile_count)
    print("observation registered")
    # Calculates moving average reward
    self.queue.appendleft(reward)
    if len(self.queue) == 7:
      self.queue.pop()
      tmp = self.queue.copy()
      movingAvgReward = 0
      while len(tmp)!=0:
        movingAvgReward += tmp.pop()
      movingAvgReward /= 7
      self.movingAvgRewards.append(movingAvgReward)
      print(movingAvgReward)
      print(self.movingAvgRewards)

    
    return observation, reward, False, {}
  def reset(self):
    return [0] * 2

  def close (self):
    pass




# rospy.spin()
