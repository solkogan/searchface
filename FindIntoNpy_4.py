import dlib
import os
import numpy as np
from skimage import io
from scipy.spatial import distance


def get_face_descriptor(filename):
    img = io.imread(filename)
    win1 = dlib.image_window()
    win1.clear_overlay()
    win1.set_image(img)
    detected_faces = detector(img, 1)
    shape = None
    face_descriptor = None
    for k, d in enumerate(detected_faces):
        shape = sp(img, d)
        win1.clear_overlay()
        win1.add_overlay(d)
        win1.add_overlay(shape)
    try:
        face_descriptor = face_rec.compute_face_descriptor(img, shape)
    except Exception as ex:
        print(ex)
    return face_descriptor


if __name__ == '__main__':
    sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    face_rec = dlib.face_recognition_model_v1(
            'dlib_face_recognition_resnet_model_v1.dat')
    detector = dlib.get_frontal_face_detector()

    min_distance_file = ''
    min_distance = 2
    files = os.listdir('npy')
    f1 = get_face_descriptor('1.jpg')

    for file_ in files:
        file_name = 'npy/' + file_
        if os.path.exists(file_name):
            f2 = np.load(file_name)
            euc_distance = distance.euclidean(f1, f2)
            if euc_distance < min_distance:
                min_distance = euc_distance
                min_distance_file = file_
    min_distance_file = min_distance_file.split('_')[0]
    print('https://vk.com/id' + min_distance_file.replace('.npy', ''))
    print('Result: ' + str(min_distance) + ' (< 0,52 = Win!)')
