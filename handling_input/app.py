import argparse
import cv2
import numpy as np

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Handle an input stream")
    # -- Create the descriptions for the commands
    i_desc = "The location of the input file"

    # -- Create the arguments
    parser.add_argument("-i", help=i_desc)
    args = parser.parse_args()

    return args


def capture_stream(args):
    ### TODO: Handle image, video or webcam
    cap = cv2.VideoCapture(args.i)

    ### TODO: Get and open video capture
    ret, frame = cap.read()

    ### TODO: Re-size the frame to 100x100
    frame = cv2.resize(frame, (100,100))

    ### TODO: Add Canny Edge Detection to the frame, 
    ###       with min & max values of 100 and 200
    ###       Make sure to use np.dstack after to make a 3-channel image
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(frame_gray,100,200)

    ### TODO: Write out the frame, depending on image or video
    new_image = np.dstack([edges,edges,edges])
    cv2.imwrite('./test.jpg', new_image)

    ### TODO: Close the stream and any windows at the end of the application
    cap.release()

def main():
    args = get_args()
    capture_stream(args)


if __name__ == "__main__":
    main()
