import numpy as np
import common.const as const
import common.configuration as config
import datasets.dataParser as ds

def train(data):
    Y = np.load("numpy_files/Y.npy")
    R = np.load("numpy_files/R.npy")
    for row in data:
        title = row[0]
        if title[-1].isspace():
            title = title[:-1]
        if title in const.title_to_movieid.keys():
            Y[int(const.title_to_index[title])][const.num_of_users] = float(row[1])
            R[int(const.title_to_index[title])][const.num_of_users] = 1

    X = np.random.rand(const.num_of_movies, config.num_X_genres)
    THETA = np.random.rand(const.num_of_users + 1, config.num_X_genres)

    # implementation of collaborative filtering
    for i in range(config.iterations):
        # print(i)
        for u, theta in enumerate(THETA):
            regTerm_theta = config.lambda_reg * theta
            regTerm_theta[0] = 0
            thetaGrad = np.matmul(X.T, (np.matmul(X, theta).T - Y[:, u])) + regTerm_theta
            THETA[u, :] = theta - config.alpha * thetaGrad
        for m, x in enumerate(X):
            regTerm_x = config.lambda_reg * x
            regTerm_x[0] = 0
            xGrad = np.matmul(THETA.T, (np.matmul(THETA, x.T).T - Y[m, :])) + regTerm_x
            X[m, :] = x - config.alpha * xGrad

    np.save("numpy_files/THETA.npy", THETA)
    np.save("numpy_files/X.npy", X)

def output():
    THETA = np.load("numpy_files/THETA.npy")
    X = np.load("numpy_files/X.npy")
    userPredictions = np.matmul(X, THETA.T)
    webPred = userPredictions[:, -1]
    indexes = np.argpartition(webPred, -5)[-5:]
    movies = [const.index_to_title[index] for index in indexes]
    return movies

