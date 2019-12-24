import dlib
import os
import numpy as np
from skimage import io


sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
face_rec = \
    dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()


def get_face_descriptor(x):
    img = io.imread('jpg/'+x)
    detected_faces = detector(img, 1)
    q = 0
    for k, d in enumerate(detected_faces):
        shape = sp(img, d)
        try:
            q += 1
            f = face_rec.compute_face_descriptor(img, shape)
            mas = np.array(f)
            file_name_ = 'npy/' + x.replace('.jpg', '')
            np.save(file_name_ + '_' + str(q), mas)
        except Exception as ex:
            print(ex)


files = os.listdir('jpg')
z = 0
for x in files: 
    z += 1
    file_name = 'npy/' + (x.replace('.jpg', ''))
    if not os.path.exists(file_name + '_1.npy'):
        print(z)
        get_face_descriptor(x)
