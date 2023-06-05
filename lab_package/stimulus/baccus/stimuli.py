import copy
import time  # for debugging and benchmarking
from math import radians

import numpy as np
from numpy.random import default_rng

from flystim import shapes as fshapes
from flystim import stimuli as fstimuli
from flystim.stimuli import BaseProgram
from flystim.trajectory import make_as_trajectory, return_for_time_t
from flystim.distribution import make_as_distribution

