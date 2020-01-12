import datasets.dataParser as ds
import numpy as np
import common.const as const
import common.configuration as config

ds.parseData()
#the extra user information is drawn from the MySQL db
Y = np.zeros(shape=(const.num_of_movies, const.num_of_users+1))
R = np.zeros(shape=(const.num_of_movies, const.num_of_users+1))

for i, entry in enumerate(const.all_movie_data):
    if int(entry[1]) < const.num_of_movies:
        Y[int(entry[1])][int(entry[0])-1] = float(entry[2])
        R[int(entry[1])][int(entry[0])-1] = 1

np.save("numpy_files/Y.npy", Y)
np.save("numpy_files/R.npy", R)

