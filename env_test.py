import sys

print("python == ", sys.version)

import numpy as np

print("numpy ==", np.__version__)

import torch
from torch import Tensor

print("torch == ", torch.__version__)
print(Tensor([1, 2, 3]) * Tensor([1, 2, 3]))
