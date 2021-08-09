import gym
import env
from stable_baselines3 import DQN
import rospy 
from openface2_ros.msg import Faces
import matplotlib.pyplot as plt
from cozmo_actions import actions


env = env.CozmoEnv()

rospy.Subscriber("/openface2/faces", Faces, env.data_callback, queue_size=1)


# env = gym.make(env)
print(env)

model = DQN("MlpPolicy",
            env,
            buffer_size=50,
            learning_starts=5,
            batch_size=2,
            train_freq=2,
            target_update_interval=4,
            exploration_fraction=0.6,
            exploration_initial_eps=1,
            exploration_final_eps=0.05,
            learning_rate=0.3,
            verbose=1,
            tensorboard_log="./a2c_cartpole_tensorboard/")
model.learn(total_timesteps=20)

plt.plot(range(len(env.movingAvgRewards)), env.movingAvgRewards)
# global party_count,cheerup_count, confused_count, cute_count
# action_counts = [actions.party_count , actions.cheerup_count,actions.confused_count,actions.cute_count]
plt.bar([1,2,3,4], env.actionCounter)

obs = env.reset()
for i in range(10):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    if done:
      obs = env.reset()

 
plt.show()
env.close()