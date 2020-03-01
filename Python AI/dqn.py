import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=Warning)

from evaluate_model import evaluate

from nes_py.wrappers import JoypadSpace
import gym_tetris
from gym_tetris.actions import MOVEMENT, SIMPLE_MOVEMENT, TRAIN_MOVEMENT
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN

env = gym_tetris.make('TetrisA-v3')
env = JoypadSpace(env,TRAIN_MOVEMENT)
env = DummyVecEnv([lambda: env])


model = DQN.load("TetrisA-v0_DQN_300k", env=env, verbose=1)


mean_reward=evaluate( model=model, env=env, num_steps=6000, render=True)
