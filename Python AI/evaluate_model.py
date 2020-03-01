import numpy as np

def evaluate(model, env, num_steps=1000, render = True):
  """
  Evaluate a RL agent
  :param model: (BaseRLModel object) the RL Agent
  :param num_steps: (int) number of timesteps to evaluate it
  :return: (float) Mean reward for the last 100 episodes
  """
  episode_rewards = [0.0]
  obs = env.reset()
  for i in range(num_steps):
    # _states are only useful when using LSTM policies
    action, _states = model.predict(obs)
    # here, action, rewards and dones are arrays
    #because we are using vectorized env
    obs, rewards, dones, info = env.step(action)
    if render:
      env.render()
    # Stats
    episode_rewards[-1] += rewards[0]
    if dones[0]:
        #print(info)
        obs = env.reset()
        episode_rewards.append(0.0)

  # Compute mean reward for the last 100 episodes
  mean_100ep_reward = round(np.mean(episode_rewards[-100:]), 1)
  print("Mean reward:", mean_100ep_reward, "Num episodes:", len(episode_rewards))
  
  return mean_100ep_reward