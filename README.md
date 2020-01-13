# movie-recommender

## Introduction
Flask/MySQL app for making movie recommendations. The model is trained on [this dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset) and uses ratings from 670 users on 9000+ movies. An additional user is reserved for data entered into the MySQL database and is loaded prior to training. 

## Structure
The data is extracted into NumPy arrays in launch.py with helper functions in parseData.py. The app is contained within main.py - run this file to start the project. train.py contains the model. NumPy arrays (inputs, trained outputs) are stored in the numpy_files directory. 

## Model
The model uses standard low-rank matrix factorization/collaborative filtering techniques implemented in NumPy. It learns algorithmically genres(the number specified in configuration), as opposed to having a predetermined matrix. A vector of all movie predictions for the database user is extracted by taking the last user column of XΘ<sup>T</sup>, and the 5 highest values are taken as recommendations. 


### Configuration
Important model parameters can be configured in configuration.py:
```python3
num_X_genres = 10
alpha = 0.000001
lambda_reg = 1
iterations = 1000
launch = False
train = False
```
Alpha is the learning rate used for gradient descent, launch reloads the training data, and train will recalibrate the model. 
