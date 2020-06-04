import cv2
import numpy as np

def pose_estimation(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related pose estimation model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)
    resized_image = cv2.resize(preprocessed_image,(456,256))
    preprocessed_image = resized_image[np.newaxis, :, :, :]
    preprocessed_image = preprocessed_image.transpose(0,3,1,2)

    # TODO: Preprocess the image for the pose estimation model

    return preprocessed_image


def text_detection(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related text detection model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)
    resized_image = cv2.resize(preprocessed_image,(1280,768))
    preprocessed_image = resized_image[np.newaxis, :, :, :]
    preprocessed_image = preprocessed_image.transpose(0,3,1,2)

    # TODO: Preprocess the image for the text detection model

    return preprocessed_image


def car_meta(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related car metadata model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    preprocessed_image = np.copy(input_image)
    resized_image = cv2.resize(preprocessed_image,(72,72))
    preprocessed_image = resized_image[np.newaxis, :, :, :]
    preprocessed_image = preprocessed_image.transpose(0,3,1,2)

    # TODO: Preprocess the image for the car metadata model

    return preprocessed_image
