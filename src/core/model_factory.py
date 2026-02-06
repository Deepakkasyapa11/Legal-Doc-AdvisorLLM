import torch
import torch.nn as nn

class JurisNeuralNetwork(nn.Module):
    """
    High-performance transformer-based architecture for legal document classification.
    Refactored for modular scalability.
    """
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(JurisNeuralNetwork, self).__init__()
        self.layer_one = nn.Linear(input_dim, hidden_dim)
        self.activation = nn.ReLU()
        self.layer_two = nn.Linear(hidden_dim, output_dim)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, tensor_input):
        x = self.layer_one(tensor_input)
        x = self.activation(x)
        x = self.layer_two(x)
        return self.softmax(x)