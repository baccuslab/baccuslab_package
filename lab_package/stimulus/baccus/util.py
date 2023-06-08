import os
import numpy as np
import inspect
import cv2
import lab_package
from flystim import util as futil

def get_resource_path(resource_name):
    path_to_resource = os.path.join(inspect.getfile(lab_package).split('lab_package')[0],
                                    'lab_package',
                                    'resources',
                                    resource_name)

    assert os.path.exists(path_to_resource), 'Resource not found at {}'.format(path_to_resource)

    return path_to_resource

def get_video_dim(fileapth):
    cap = cv2.VideoCapture(fileapth)
    ret = False
    while not ret:
        ret, frame = cap.read()
    return frame.shape
