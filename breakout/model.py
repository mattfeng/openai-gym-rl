from collections import namedtuple
import torch as T
import torch.nn as nn
import torch.nn.functional as F

Transition = namedtuple("Transition",
    ("state", "action", "next_state", "reward"))

class DQN(nn.Module):
    """
    DQN (Deep Q-Network)
    """

    def __init__(self):
        super(DQN, self).__init__()
        # input size (84, 84, 2)
        # Takes the current and previous frames
        self.conv1 = nn.Conv2d(2, 32, kernel_size=8, stride=4)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=4, stride=2)
        self.conv3 = nn.Conv2d(64, 64, kernel_size=3, stride=1)
        self.fc1 = nn.Linear(7 * 7 * 64, 512)
        self.fc2 = nn.Linear(512, 4)

    def forward(self, x):
        """
        Parameters
        ----------
        x :
        """
        x = x.view(-1, 2, 84, 84)
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.relu(self.fc1(x.view(-1, 7 * 7 * 64)))
        x = F.relu(self.fc2(x))

        return x
        