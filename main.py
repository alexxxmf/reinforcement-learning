import gym

env = gym.make('FrozenLake-v0')

for iteration in range(1):
  observation = env.reset()

  finished = False
  count = 0
  while finished is False:
    count += 1

    env.render()

    action = env.action_space.sample()

    observation, reward, done, info = env.step(action)

    # print('====observation====')
    # print(observation)
    # print('====reward====')
    # print(reward)
    # print('====done====')
    # print(done)
    # print('====info====')
    # print(info)

    finished = done

  print(f'Attempt #{iteration + 1}, Steps taken until done: {count}')

env.close()