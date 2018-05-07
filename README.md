# gym-rubik-cube

An OpenAI environment for Rubik's Cube using [PyCuber](https://github.com/adrianliaw/PyCuber) library.

## Installation

Install the [OpenAI gym](https://gym.openai.com/docs/).

Then install this package via

```
pip install -e .
```

## Usage

```
import gym
import gym_rubik_cube

env = gym.make('RubikCube-v0')
```
