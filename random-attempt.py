import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('FrozenLake-v0')

NUMBER_OF_GAMES = 1000
win_percentage = []
scores = []

for i in range(NUMBER_OF_GAMES):
  observation = env.reset()

  done = False
  score = 0

  while not done:
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    score += reward

  scores.append(score)

  if i % 10 == 0:
    average = np.mean(scores[-10:])
    win_percentage.append(average)

plt.plot(win_percentage)
plt.show()

env.close()