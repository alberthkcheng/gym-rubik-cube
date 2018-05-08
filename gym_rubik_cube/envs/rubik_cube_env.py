import gym
from gym import error, spaces, utils
from gym.utils import seeding

import pycuber
from sklearn.preprocessing import LabelBinarizer

import logging
logger = logging.getLogger(__name__)

class RubikCubeEnv(gym.Env):

  def __init__(self):
    self.mycube = pycuber.Cube()
  
    self.action_space = spaces.Discrete(6)
    
    # No. of face x No. of possible color
    self.observation_space = spaces.Tuple((spaces.Discrete(3*3*6), spaces.Discrete(6))) 
    
    # LabelBinarizer to transform cube to array
    self.color_binarizer = LabelBinarizer()
    self.color_binarizer.fit(['[r]','[o]','[y]','[w]','[b]','[g]'])

  def step(self, action):
    self._take_action(action)
    reward = self._get_reward()
    episode_over = self.mycube == pycuber.Cube()
    return self.get_state(), reward, episode_over, {}
    
  def reset(self):
    self.mycube = pycuber.Cube()
    
  def get_state(self):
    return self._cubeAsArray(self.mycube)

  def _take_action(self, action):
    self.mycube(ACTION_LOOKUP[action])

  def _get_reward(self):
    if self.mycube == pycuber.Cube():
        return 1
    else:
        return 0

  def render(self):
    print(self.mycube)
    
  def _cubeAsArray(self, cube):
    cubeArray = []
    for face in ACTION_LOOKUP:
        f = self.mycube.get_face(ACTION_LOOKUP[face])
        for x in [0,1,2]:
            for y in [0,1,2]:
                cubeArray.append(str(f[x][y]))
    return self.color_binarizer.transform(cubeArray)

ACTION_LOOKUP = {
    0 : 'L',
    1 : 'R',
    2 : 'U',
    3 : 'D',
    4 : 'F',
    5 : 'B',
}
