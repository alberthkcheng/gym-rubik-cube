import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='RubikCube-v0',
    entry_point='gym_rubik_cube.envs:RubikCubeEnv',
)