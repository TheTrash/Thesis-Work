import numpy as np
from stable_baselines.common.vec_env import VecVideoRecorder

def record(model, env, num_episodes=1):
  """
  Evaluate a RL agent
  :param model: (BaseRLModel object) the RL Agent
  :param num_steps: (int) number of timesteps to evaluate it
  :return: (float) Mean reward for the last 100 episodes
  """
  env = VecVideoRecorder(env,"./vid", record_video_trigger=lambda x: x == 0, video_length=12000, name_prefix="tetris_ai_video")
  obs = env.reset()
  i=0
  steps = 0
  while (i <= num_episodes):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    steps+=1
    if dones[0]:
        obs = env.reset()
        print("=== EPISODE {} ===".format(i+1))
        print("Num_lines: " + str(info[0]['number_of_lines']))
        print("score: " + str(info[0]['score']))
        print("Number of episodes: ", i)
        print("=== END ===")
        i+=1
  
  return "Done"