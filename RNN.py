import numpy as np


class RNN:

	def __init__(self, hidden_size: np.ndarray, vocab_size, learning_rate):
		self.hidden_size = hidden_size
		self.vocab_size = vocab_size
		self.learning_rate = learning_rate