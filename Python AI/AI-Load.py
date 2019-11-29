import sys
import numpy as no

from nes_py.wrappers import JoypadSpace
import gym_tetris
from gym_tetris.actions import MOVEMENT, SIMPLE_MOVEMENT

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Dropout
from tensorflow.keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy, LinearAnnealedPolicy, BoltzmannQPolicy, GreedyQPolicy
from rl.memory import SequentialMemory
from rl.callbacks import FileLogger, ModelIntervalCheckpoint


env = gym_tetris.make('TetrisA-v1')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

num_actions = env.action_space.n

#this can be the output range 0-6 for the move
print("Num actions: ", num_actions)
model = Sequential()
model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
model.add(Dense(32, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(num_actions, activation='linear'))
print(model.summary())


policy = GreedyQPolicy()
memory= SequentialMemory(limit=50000, window_length = 1)


dqn = DQNAgent(model = model, nb_actions = num_actions , memory=memory, nb_steps_warmup=50000,
        target_model_update=1e+4, policy=policy)
dqn.compile(Adam(lr= 1e-4), metrics=['mae'])

weights_filename= 'dqn_{}_weights.h5f'.format('gym_tetris')
dqn.load_weights(filepath=weights_filename)
nb_episodes = int(input("Inserisci il numero di episodi: ")) 

dqn.test(env,nb_episodes=nb_episodes,visualize=True)