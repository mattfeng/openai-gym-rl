import torch as T
import torch.nn as nn
import torch.nn.functional as F

class DQN(nn.Module):
    """
    DQN (Deep Q-Network)

    """

    def __init__(self):
        super(DQN, self).__init__()
        # input size (84, 84, 6)
        # Takes the current and previous frames
        self.conv1 = nn.Conv2d(6, 32, kernel_size=3, stride=1)
        self.bn1 = nn.BatchNorm2d(32) # num_features = # channels
        self.conv2 = nn.Conv2d(32, 64, kernel_size=5, stride=2)
        self.bn2 = nn.BatchNorm2d(64)
        self.conv3 = nn.Conv2d(64, 10, kernel_size=1)
        self.bn3 = nn.BatchNorm2d(10)
        self.fc1 = nn.Linear(15210, 300)
        self.fc2 = nn.Linear(300, 4)

    def forward(self, x):
        """
        Parameters
        ----------
        x :
        """
        x = x.view(-1, 6, 84, 84)
        x = F.relu(self.bn1(self.conv1(x)))
        x = F.relu(self.bn2(self.conv2(x)))
        x = F.relu(self.bn3(self.conv3(x)))
        x = F.relu(self.fc1(x.view(-1, 15210)))
        x = F.relu(self.fc2(x))

        return x
        