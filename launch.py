from datasets.dataParser import *
import numpy as np
import common.const as const
import common.configuration as config
parseData()

#the extra user information is drawn from the MySQL db
THETA = np.zeros(shape=(const.num_of_movies, const.num_of_users+1))
Y = np.zeros(shape=(const.num_of_movies, const.num_of_users+1))
X = np.zeros(shape=(const.num_of_movies, config.num_X_genres))


for i, entry in enumerate(const.all_movie_data):
    if int(entry[1]) < const.num_of_movies:
        THETA[int(entry[1])][int(entry[0])-1] = float(entry[2])
        Y[int(entry[1])][int(entry[0])-1] = 1

x = const.num_of_movies

# for i in range(x-1, -1, -1):
#     if sum(THETA[i]) == 0:
#         const.num_of_movies -= 1
