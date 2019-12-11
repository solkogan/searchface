import dlib
import os
import numpy as np
import nmslib


if __name__ == '__main__':
    index = nmslib.init(method='hnsw',
                        space='l2',
                        data_type=nmslib.DataType.DENSE_VECTOR)

    files = os.listdir('npy')

    es = []
    e = 0

    with open('associations.txt', 'w') as embedding_file:

        for file in files:
            e += 1
            name, _ = os.path.splitext(file)
            embedding = np.load('npy/' + file)
            embedding_file.write(str(e) + '|' + file + '\n')
            index.addDataPoint(e, embedding)

        index_time_params = {
            'indexThreadQty': 4,
            'skip_optimized_index': 0,
            'post': 2,
            'delaunay_type': 1,
            'M': 100,
            'efConstruction': 2000
        }

        index.createIndex(index_time_params, print_progress=True)
        index.saveIndex('embeddings.bin')
