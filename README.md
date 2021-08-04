### Reinforcement Learning

##### Description

In this repo I am going to place all my experimentation around reinforcement learning and that includes notes, references to papers, scripts and anything that could potentially help with my personal learning process.

##### Concepts

- Agent: Is like a more specific definition that a model in Deep learning. An agent looks like an active model that learns but also makes decisions
- Environment: Is all what the agent interacts with and changes with the set of actions the agent takes
- State Space: Is the set of all possible states
- Action Space: Is the set of all possible actions
- Rewards: Is the info needed for the agent to come to a conclussion based on some actions
- Markov Decision Process: At each time the agent observes a state and executes an action, which incurs intermediate costs to be minimized (or, in the inverse scenario, rewards to be maximized). The cost and the successor state depend only on the current state and the chosen action. Successor generation may be probabilistic, based on the uncertainty we have on the environment in which the search takes place. For example, an action might sometimes fail to result in the desired target state, instead staying in the current state with a small probability
- Actions cause state transitions
- Episode: is a discrete period of game play
- Episodic game play: Terminal state is unique and can only be accesed by ending the episode and no future rewards are supposed to follow after we reach terminal state
- Not all tasks are episodic so this means the future expected rewards tend to infinity but we can solve this by discounting. Exactly the way we do when calculating returns for cashflow methods. The far a reward is in the future, the more impact it receives in terms of discount value.
- The discount value is called γ(gamma) and is a hyperparameter `0 <= γ <= 1`. Normally its chosen to be between 0.95 and 0.99 for continuous tasks.
- Policy: is a mapping between actions and states. Can be probabilistic
