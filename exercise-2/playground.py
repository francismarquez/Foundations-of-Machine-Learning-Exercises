import numpy as np
import matplotlib.pyplot as plt

from utils import gaussian_distribution

np.random.seed(14)

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1500)

# count, bins, ignored = plt.hist(s, 30, density=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#          linewidth=2, color='r')
# plt.show()
# exit()

s1 = np.array(list(filter(lambda x: x <= (2*sigma) and x >= (-2*sigma), s)))

dataset_len = 1000
TRAIN_SPLIT = int(0.9 * dataset_len)
TEST_SPLIT = int(0.1 * dataset_len)

dataset_x = np.random.choice(s1, dataset_len)
dataset_y = gaussian_distribution(dataset_x,sigma,mu)

train_x, test_x = np.split(dataset_x, [TRAIN_SPLIT])
train_y, test_y = np.split(dataset_y, [TRAIN_SPLIT])

plt.plot(train_x, train_y, '.')
plt.show()

# initialize_parameters()