import csv
import common.const as const


def convert_to_list(filename):
    with open(filename, errors='ignore') as f:
        for index, l in enumerate(f):
            pass
    len = index + 1
    result = [[] for x in range(len)]
    with open(filename, errors='ignore') as file:
        reader = csv.reader(file, delimiter=',')
        for i, row in enumerate(reader):
            if not i:
                continue
            for k in row:
                if k and k != ',':
                    result[i - 1].append(k)
    return result

def parseData():
    tmdbid_to_title = {}
    movieid_to_tmdbid = {}

    for filename, mapname in zip(['datasets/movies_metadata.csv', 'datasets/links_small.csv'], [tmdbid_to_title, movieid_to_tmdbid]):
        with open(filename, errors='ignore') as file:
            reader = csv.reader(file, delimiter=',')
            for i, row in enumerate(reader):
                if i:
                    mapname[row[0]] = row[1]

    movieid_to_title = {}

    for i in movieid_to_tmdbid.keys():
        if movieid_to_tmdbid[i] in tmdbid_to_title.keys():
            movieid_to_title[i] = tmdbid_to_title[movieid_to_tmdbid[i]]

    all_movie_data = convert_to_list('datasets/ratings_small.csv')
    del all_movie_data[-1]
    for j in range(len(all_movie_data)-1, -1, -1):
        if all_movie_data[j][1] in movieid_to_title.keys():
            all_movie_data[j].append(movieid_to_title[all_movie_data[j][1]])
        else:
            del all_movie_data[j]

    const.movieid_to_title = movieid_to_title
    const.all_movie_data = all_movie_data
    const.num_of_users = all_movie_data[-1][0]
    const.num_of_movies = len(movieid_to_title.keys())
