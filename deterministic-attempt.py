import gym
import numpy as np
import matplotlib.pyplot as plt

# Apparently the correct mapping for the action_space is the following:
# 0 => left
# 1 => down
# 2 => right
# 3 => up
# SFFF
# FHFH
# FFFH
# HFFG
# If we move from S to F. Observation goes from 0 to 4 (index position)
# env.step(action) the agent does not follow this in a deterministic way 100% of the time
# sometimes it takes a step into a random direction so it has some stochastic element
# if we print out info from env.step(action) we will see a probability of 0.33/33%
# I guess this means agent just follow orders 33% of the time


policy = {
  0: 1, 1: 1, 2: 1, 3: 1,
  3: 1, 4: 1, 5: 1, 6: 1,
  7: 1, 8: 1, 9: 1, 10: 1,
  11: 2, 12: 2, 13: 2, 14: 2
}



env = gym.make('FrozenLake-v0')

NUMBER_OF_GAMES = 1000
win_percentage = []
scores = []

for i in range(NUMBER_OF_GAMES):
  observation = env.reset()

  done = False
  score = 0


  while not done:
    action = policy[observation]
    observation, reward, done, info = env.step(action)
    score += reward
    env.render()

  scores.append(score)

  if i % 10 == 0:
    average = np.mean(scores[-10:])
    win_percentage.append(average)

plt.plot(win_percentage)
plt.show()

env.close()