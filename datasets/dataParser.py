import csv



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

tmdbid_to_title = {}
movieid_to_tmdbid = {}

for filename, mapname in zip(['movies_metadata.csv', 'links_small.csv'], [tmdbid_to_title, movieid_to_tmdbid]):
    with open(filename, errors='ignore') as file:
        reader = csv.reader(file, delimiter=',')
        for i, row in enumerate(reader):
            if i:
                mapname[row[0]] = row[1]

movieid_to_title = {}

for i in movieid_to_tmdbid.keys():
    if movieid_to_tmdbid[i] in tmdbid_to_title.keys():
        movieid_to_title[i] = tmdbid_to_title[movieid_to_tmdbid[i]]

all_movie_data = convert_to_list('ratings_small.csv')
del all_movie_data[-1]
for j in range(len(all_movie_data)-1, -1, -1):
    if all_movie_data[j][1] in movieid_to_title.keys():
        all_movie_data[j].append(movieid_to_title[all_movie_data[j][1]])
    else:
        del all_movie_data[j]

x = 5



