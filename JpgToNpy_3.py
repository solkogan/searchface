import dlib, os, shutil
import numpy as np
from skimage import io
from scipy.spatial import distance
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

def getfacedescriptor(x):
    img = io.imread('jpg/'+x)
    dets = detector(img, 1)
    q=0
    for k, d in enumerate(dets):
        shape = sp(img, d)
        try:
            q=q+1
            f = facerec.compute_face_descriptor(img, shape)
            mas = np.array(f)
            fname='npy/'+(x.replace('.jpg',''))
            np.save(fname+'_'+str(q), mas)
        except:
            print('Ошибка')

files = os.listdir('jpg')
z=0
for x in files: 
    z=z+1
    fname='npy/'+(x.replace('.jpg',''))
    
    if (not(os.path.exists(fname+'_1.npy'))):
        print(z)
        getfacedescriptor(x) 



