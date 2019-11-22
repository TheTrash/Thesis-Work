# DQN

The Deep Q Learning agent is used for discrete action spaces. The agent comprises of a neural network which learns the Q values for each action state pair, that is, it sees as inputs an observation (the state) and gives as its output values for each possible action. The action chosen from these values is then decided by the policy passed to the agent, and can be different in the training and testing phase. Default policies are EpsGreedyQPolicy during training and GreedyQPolicy during testing, which introduces randomness in the training process while having deterministic actions during testing.

A common problem with using DQN is that the if the network is updated at each step, we are constantly "chasing" a changing "target". Stability can be improved by using a "target" network on top of the original "trainable" network. In each iteration, we retrieve the Q values from the target network and use it to choose our actions, while using the resulting rewards to update only the trainable network. Once in a while (number of steps passed as parameter target_model_update), we "push" these changes from the trainable network to the target network. This allows the "target" we are chasing to be relatively stable.

Double DQN is a variant that reduces overestimation of Q values. The difference between Double DQN and the vanilla version that uses a target network is slight - while the Q values used for calculating discounted rewards are also taken from the target network, the actions are chosen based on the trainable network's Q values. Similarly, changes in the trainable network are pushed to the target network every target_model_update steps.

Dueling DQN is another variant that uses the classic decomposition of the Q values into the value of the state and the value of the action. The two final layers of out network is as follows: the layer before the final output has the shape (nb_samples, nb_actions+1) such that the first value represents the state value V and the other nb_actions represents the action values A. The final layer than combines V and A according to three methods:
- 'avg': Q(s,a) = V(s) + A(s,a) - ave(A)
- 'max': Q(s,a) = V(s) + A(s,a) - max(A)
- 'naive': Q(s,a) = V(s) + A(s,a)

Note that this agent is not compatible with multiple discrete spaces (for example, choose 0 or 1 for each of n buttons), that is, its output is always of the shape (nb_samples, nb_actions). The easiest way to use this agent with multiple discrete spaces would be to detail all possible combinations of actions (in the same example with n=3, this would mean having the action as 000, 001, 010, etc).

All the credits to yujia21 that committed this documentation update [here](https://github.com/keras-rl/keras-rl/pull/331/commits/bcfd6a3a73d28cbb30acf43fc19d1f038ca3a5b6#)