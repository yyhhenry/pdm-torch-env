import sys

import numpy as np
import torch
import torchvision
from torch import Tensor

print("python == ", sys.version)

print("numpy ==", np.__version__)

print("torch == ", torch.__version__)

print("torchvision == ", torchvision.__version__)

x = Tensor([1, 2, 3]).cuda()
y = Tensor([1, 4, 9]).cuda()
assert bool((x * x == y).all().item())
print("torch.cuda works!")
