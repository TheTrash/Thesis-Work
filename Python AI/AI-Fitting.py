import sys
import numpy as no

from nes_py.wrappers import JoypadSpace
import gym_tetris
from gym_tetris.actions import MOVEMENT, SIMPLE_MOVEMENT

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Dropout
from tensorflow.keras.optimizers import Adam, SGD

from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy, LinearAnnealedPolicy, BoltzmannQPolicy, GreedyQPolicy,  BoltzmannGumbelQPolicy
from rl.memory import SequentialMemory
from rl.callbacks import FileLogger, ModelIntervalCheckpoint


env = gym_tetris.make('TetrisA-v1')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

num_actions = env.action_space.n

#this can be the output range 0-6 for the move
print("Num actions: ", num_actions)
model = Sequential()

model.add(Convolution2D(32, (4, 4), strides=(4, 4),padding='valid', input_shape= input_shape, data_format = "channels_last"))
model.add(Activation('relu'))
model.add(Convolution2D(64, (4, 4), strides=(2, 2)))
model.add(Activation('relu'))
model.add(Convolution2D(64, (3, 3), strides=(1, 1)))
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
print(model.summary())


policy =  BoltzmannGumbelQPolicy(1)
memory= SequentialMemory(limit=50000, window_length = 1)


dqn = DQNAgent(model = model, nb_actions = num_actions , memory=memory, nb_steps_warmup=5000,
        target_model_update=1e+3, policy=policy)
dqn.compile(SGD(lr= .001), metrics=['mae'])


nb_episodes = int(input("Inserisci il numero di steps: ")) 

dqn.fit(env,nb_steps=nb_episodes,visualize=True)

weights_filename = 'dqn_{}_weights.h5f'.format("gym_tetris")
dqn.save_weights(weights_filename, overwrite=True)