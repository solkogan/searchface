import dlib
import numpy as np
from skimage import io
import nmslib


def get_face_descriptor(filename):
    img = io.imread(filename)
    win1 = dlib.image_window()
    win1.clear_overlay()
    win1.set_image(img)
    face_descriptor = None
    shape = None
    detected_faces = detector(img, 1)
    for k, d in enumerate(detected_faces):
        shape = sp(img, d)
        win1.clear_overlay()
        win1.add_overlay(d)
        win1.add_overlay(shape)
    try:
        face_descriptor = face_rec.compute_face_descriptor(img, shape)
        face_descriptor = np.asarray(face_descriptor)
    except Exception as ex:
        print(ex)

    return face_descriptor


def print_id(n):
    best_dx = ids[n]
    s = ''
    with open('associations.txt', 'r') as file_:
        for line in file_:
            w = str(best_dx) + '|'
            if line.find(w) == 0:
                s = line.split('|')[1]
    s = 'https://vk.com/id' + s.split('_')[0]
    for bad_symbols in ['.txt', '.npy', '\n']:
        s = s.replace(bad_symbols, '')
    print(s)


if __name__ == '__main__':
    sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    face_rec = dlib.face_recognition_model_v1(
        'dlib_face_recognition_resnet_model_v1.dat')
    detector = dlib.get_frontal_face_detector()
    index = nmslib.init(method='hnsw', space='l2',
                        data_type=nmslib.DataType.DENSE_VECTOR)
    index.loadIndex('embeddings.bin')

    query_time_params = {'efSearch': 400}
    index.setQueryTimeParams(query_time_params)

    embedding = get_face_descriptor('1.jpg')

    ids, dists = index.knnQuery(embedding, k=5)
    print_id(0)
    print_id(1)
    print_id(2)
    print_id(3)
    print_id(4)
