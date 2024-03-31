import gym
import numpy as np


def discretize_observation(observation, bins):
    # Функція для дискретизації спостережень
    # Припустимо, ми дискретизуємо кожен компонент спостереження до заданої кількості бінів
    # Для Acrobot ми можемо вибрати дискретизацію кутів і швидкостей
    discretized = [np.digitize(observation[i], bins[i]) for i in range(len(observation))]
    return tuple(discretized)


# Ініціалізація середовища
env = gym.make('Acrobot-v1')

# Параметри Q-Learning
learning_rate = 0.1
discount_factor = 0.99
epsilon = 0.1
num_episodes = 1000
max_steps_per_episode = 500

# Дискретизація простору спостережень
num_bins = 10  # Кількість бінів для кожної змінної у спостереженні
bins = [np.linspace(-1, 1, num_bins) for _ in range(env.observation_space.shape[0])]

# Ініціалізація Q-таблиці
q_table = np.zeros([num_bins] * env.observation_space.shape[0] + [env.action_space.n])

for episode in range(num_episodes):
    observation = env.reset()
    state = discretize_observation(observation, bins)

    for t in range(max_steps_per_episode):
        # Епсилон-жадібний вибір дії
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Дослідження
        else:
            action = np.argmax(q_table[state])  # Використання

        next_observation, reward, done, info = env.step(action)
        next_state = discretize_observation(next_observation, bins)

        # Оновлення Q-таблиці
        old_value = q_table[state + (action,)]
        next_max = np.max(q_table[next_state])

        # Формула оновлення Q-значення
        new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_factor * next_max)
        q_table[state + (action,)] = new_value

        state = next_state

        if done:
            break

env.close()
