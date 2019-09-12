import dlib, os, shutil
import numpy as np
from skimage import io
from scipy.spatial import distance
import pickle
import nmslib

index = nmslib.init(method='hnsw', space='l2', data_type=nmslib.DataType.DENSE_VECTOR)

files = os.listdir('npy') 

es = []  
e=0

ff=open('associations.txt', 'w')

for x in files: 
    e=e+1
    name, _ = os.path.splitext(x)
    embedding=np.load('npy/'+x)
    ff.write(str(e)+'|'+x+'\n')
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

ff.close()
