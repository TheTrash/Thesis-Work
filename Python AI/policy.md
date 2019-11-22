**Policy**
---
---

Breve presentazione delle policy di scelta offerte dalla libreria

# Linear annealing policy

Linear Annealing Policy computes a current threshold value and transfers it to an inner policy which chooses the action. The threshold value is following a linear function decreasing over time.

The init for declaring the policy
```
'def __init__(self, inner_policy, attr, value_max, value_min, value_test, nb_steps):
```
## Action Select :
```
Choose an action to perform
Returns: 
    Action to take (int)
```
# Softmax Policy

 Implement softmax policy for multinimial distribution. Takes action according to the pobability distribution
## Action Select :
> Return the selected action
```
    Arguments :
       probs (np.ndarray) : Probabilty for each action
    Returns :
       action
```

EpsGreedy Q Policy
Implement the epsilon greedy policy
Eps Greedy policy either:
- takes a random action with probability epsilon
- takes current best action with prob (1 - epsilon)
## Action Select :
> Return the selected action
```
    Arguments :
        q_values (np.ndarray): List of the estimations of Q for each action
    Returns :
        Selection action
```

# Greedy Q Policy

Greedy policy returns the current best action according to q_values.
## Action Select :
> Return the selected action
```
    Arguments :
       probs (np.ndarray) : Probabilty for each action
    Returns :
        action
```

# Boltzmann Q Policy

Boltzmann Q Policy builds a probability law on q values and returns an action selected randomly according to this law.
## Action Select :
> Return the selected action
```
    Arguments :
        q_values (np.ndarray): List of the estimations of Q  for each action
    Returns :
        Selection action
```
# MaxBoltzmannQPolicy

A combination of the eps-greedy and Boltzman q-policy. 
Wiering, M.: Explorations in Efficient Reinforcement Learning. PhD thesis, University of Amsterdam, Amsterdam (1999) https://
pure.uva.nl/ws/files/3153478/8461_UBA003000033.pdf

## Action Select :
> Return the selected action
The selected action follows the BoltzmannQPolicy with probability epsilon or return the Greedy Policy with probability (1 - epsilon)
```
    Arguments :
        q_values (np.ndarray): List of the estimations of Q for each action
    Returns :
        Selection action
```
# Boltzmann-Gumbel Q Policy
Implements Boltzmann-Gumbel exploration (BGE) adapted for Q learning
based on the paper Boltzmann Exploration Done Right (https://arxiv.org/pdf/1705.10257.pdf).
* BGE is invariant with respect to the mean of the rewards but not their variance. The parameter C, which defaults to 1, can be used to correct for this, and should be set to the least upper bound on the standard deviation of the rewards.

* BGE is only available for training, not testing. For testing purposes, you can achieve approximately the same result as BGE after training for N steps on K actions with parameter C by using the BoltzmannQPolicy and setting tau = C/sqrt(N/K).

## Action Select :
> Return the selected action
```
    Arguments :
        q_values (np.ndarray): List of the estimations of Q for each action
    Returns :
        Selection action
```