# Blackjack Reinforcement Learning (RL) Agent

This repository contains a Reinforcement Learning framework designed to train and evaluate an intelligent agent to play Blackjack. The project implements a custom environment and an RL agent, focusing on optimizing decision-making strategies through training.

## 🚀 Project Overview

The goal of this project is to explore how reinforcement learning agents can learn optimal policies in a stochastic card game environment. The repository is organized into three main modules:
- **`blackjack_rl_agent`**: Core logic and brain of the RL agent.
- **`environment`**: A custom-built Blackjack simulation environment.
- **`training`**: Scripts and utilities for training the agent and visualizing performance.

## 📊 Training Results

The following plots illustrate the learning progress and the final strategy developed by the agent. These visualizations track performance metrics and value functions across training episodes.

![Plot 1](training/plots/Expected_winnings.png)

![Plot 2](training/plots/hard_hands.png)

![Plot 3](training/plots/soft_hands.png)

![Plot 4](training/plots/splittable_hands.png)

## 🛠 Installation

To set up the environment and dependencies, run:

```bash
pip install -r requirements.txt
