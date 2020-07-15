import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=Warning)

#Import custom function for evaluation and video recording
from evaluate_model import evaluate
from record_model import record

from nes_py.wrappers import JoypadSpace
import gym_tetris
from gym_tetris.actions import MOVEMENT, SIMPLE_MOVEMENT, TRAIN_MOVEMENT
from stable_baselines.common.vec_env import DummyVecEnv, VecVideoRecorder
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN

env = gym_tetris.make('TetrisA-v3')
env = JoypadSpace(env,TRAIN_MOVEMENT)
env = DummyVecEnv([lambda: env])


model = DQN.load("TetrisA-v2_DQN_200k", env=env, verbose=1)
mean_reward = evaluate(model=model, env=env, episode=20, render=True)

#status = evaluate(model, env, num_steps=12000, render = True)
#status = record( model=model, env=env, num_episodes=3)

print(mean_reward)
