import gym
from gym import error, spaces, utils
from gym.utils import seeding

import pycuber

import logging
logger = logging.getLogger(__name__)

class RubikCubeEnv(gym.Env):

  def __init__(self):
    self.mycube = pycuber.Cube()
  
    self.action_space = spaces.Discrete(6)
    
    # No. of face x No. of possible color
    self.observation_space = spaces.Tuple((spaces.Discrete(3*3*6), spaces.Discrete(6))) 
    
  def step(self, action):
    return self.mycube, 0, 0, {}
    
  def reset(self):
    self.mycube = pycuber.Cube()
    
  def get_state(self):
        return self.mycube
    
  def render(self, mode='human', close=False):
    return