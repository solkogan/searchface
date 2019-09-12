import dlib, os, shutil
import numpy as np
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
    except:
	    face_descriptor1=None
    return(face_descriptor1)


nm=''
d=2
files = os.listdir('npy')
f1=getfacedescriptor('1.jpg')  


for x in files: 
    fname='npy/'+x
    if(os.path.exists(fname)):
        f2=np.load(fname)
        a = distance.euclidean(f1,f2)
        if(a<d):
            d=a
            nm=x
mv=nm.split('_')
nm=mv[0]
print('https://vk.com/id'+nm.replace('.npy',''))
print('Result: '+str(d)+' (< 0,52 = Win!)')


