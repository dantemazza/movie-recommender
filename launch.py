from datasets.dataParser import *
import numpy as np
import common.const as const
import common.configuration as config
parseData()

THETA = np.zeros(shape=(const.num_of_users, const.num_of_movies))
X = np.zeros(shape=(const.num_of_users, config.num_X_genres))

