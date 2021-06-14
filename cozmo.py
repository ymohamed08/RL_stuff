import gym
import env
from stable_baselines3 import DQN
import rospy 
from openface2_ros.msg import Faces

env = env.CozmoEnv()

rospy.Subscriber("/openface2/faces", Faces, env.data_callback, queue_size=1)


# env = gym.make(env)
print(env)

model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
      obs = env.reset()

env.close()