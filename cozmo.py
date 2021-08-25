import gym
import env
from stable_baselines3 import DQN
import rospy 
from openface2_ros.msg import Faces
import matplotlib.pyplot as plt
from cozmo_actions import actions
import torch.nn as nn
from stable_baselines.common.callbacks import BaseCallback


cozmoEnv = env.CozmoEnv()

rospy.Subscriber("/openface2/faces", Faces, cozmoEnv.data_callback, queue_size=1)


# env = gym.make(env)
print(cozmoEnv)

policy_kwargs = dict(activation_fn=nn.ReLU,
                     net_arch=[8,8])

class TensorboardCallback(BaseCallback):
    """
    Custom callback for plotting additional values in tensorboard.
    """

    def __init__(self, verbose=0):
        super(TensorboardCallback, self).__init__(verbose)

    def _on_step(self):
        self.logger.dump(self.num_timesteps)
        self.num_timesteps += 1
        return True

model = DQN("MlpPolicy",
            cozmoEnv,
            buffer_size=50,
            learning_starts=1,
            batch_size=4,
            train_freq=1,
            target_update_interval=2,
            exploration_fraction=0.6,
            exploration_initial_eps=1,
            exploration_final_eps=0.05,
            learning_rate=0.3,
            verbose=1,
            policy_kwargs=policy_kwargs,
            tensorboard_log="./a2c_cartpole_tensorboard/")


model.learn(total_timesteps=30)







plt.plot(range(len(cozmoEnv.movingAvgRewards)), cozmoEnv.movingAvgRewards)
# global party_count,cheerup_count, confused_count, cute_count
# action_counts = [actions.party_count , actions.cheerup_count,actions.confused_count,actions.cute_count]
obs = cozmoEnv.reset()
for i in range(10):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = cozmoEnv.step(action)
    if done:
      obs = cozmoEnv.reset()

 
plt.show()
cozmoEnv.close()