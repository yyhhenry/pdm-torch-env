import sys

print("python == ", sys.version)

import numpy as np

print("numpy ==", np.__version__)

import torch
from torch import Tensor

print("torch == ", torch.__version__)

x = Tensor([1, 2, 3]).cuda()
y = Tensor([1, 4, 9]).cuda()
assert bool((x * x == y).all().item())

import torchvision

print("torchvision == ", torchvision.__version__)
