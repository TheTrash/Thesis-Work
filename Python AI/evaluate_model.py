import numpy as np

def evaluate(model, env, episode,  render=False):
    episode_rewards = [0.0]
    obs = env.reset()
    step = 0
    i = 1
    while i <= episode:
        step=step+1
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        if render:
            env.render()
        episode_rewards[-1] += rewards[0]
        if dones[0]:
            print("Num_lines: " + str(info[0]['number_of_lines']))
            print("score: " + str(info[0]['score']))
            print("Number of episodes: ", i)
            print("Number of Step", step)
            print("============================")
            #print("statistics: " , info[0]['statistics'])
            i=i+1
            obs = env.reset()
            episode_rewards.append(rewards)

 
    mean_100ep_reward = np.mean(episode_rewards[-100:])
    print("Mean reward:", mean_100ep_reward, "Num episodes:", len(episode_rewards), "\nSingle Reward: ", episode_rewards )
  
    return mean_100ep_reward
