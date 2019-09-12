import dlib, os, shutil
import numpy as np
import pickle
from skimage import io
from scipy.spatial import distance
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

def getfacedescriptor(filename):
    img = io.imread(filename)
    win1 = dlib.image_window()
    win1.clear_overlay()
    win1.set_image(img)
    dets = detector(img, 1)
    for k, d in enumerate(dets):
        shape = sp(img, d)
        win1.clear_overlay()
        win1.add_overlay(d)
        win1.add_overlay(shape)
    try:
	    face_descriptor1 = facerec.compute_face_descriptor(img, shape)
	    face_descriptor1=np.asarray(face_descriptor1)
    except:
	    face_descriptor1=None
    return(face_descriptor1)

import nmslib
index = nmslib.init(method='hnsw', space='l2', data_type=nmslib.DataType.DENSE_VECTOR)
index.loadIndex('embeddings.bin')

query_time_params = {'efSearch': 400}
index.setQueryTimeParams(query_time_params)

embedding=getfacedescriptor('1.jpg')

ids, dists = index.knnQuery(embedding, k=5)


def printid(n):
    best_dx = ids[n]
    best_dist = dists[n]
    s=''
    fff=open('associations.txt', 'r')
    for fs in fff:
        w=str(best_dx)+'|'
        if(fs.find(w)==0):
            s=fs.split('|')[1]
    s='https://vk.com/id'+s.split('_')[0]
    fff.close()
    s=s.replace('.txt','')
    s=s.replace('.npy','')
    s=s.replace('\n','')
    print(s)

printid(0)
printid(1)
printid(2)
printid(3)
printid(4)
