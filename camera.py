import numpy as np
import argparse
import cv2
import os


def save_img(frame, ouput_dir):
    idx = len(os.listdir(ouput_dir)) + 1
    file = "img" + str(idx) + "__.jpg"
    path = os.path.join(ouput_dir, file)
    cv2.imwrite(path, frame)


def cap_vid(output_dir):
    cap = cv2.VideoCapture(0)  # Capture video from camera

    while cap.isOpened():
        ret, frame = cap.read()

        if ret == True:
            frame = cv2.flip(frame, 180)
            frame = frame[120:600, 400:880]

            cv2.imshow("frame", frame)
            save_img(frame, output_dir)
            if (cv2.waitKey(1) & 0xFF) == ord("q"):  # Hit `q` to exit
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()


def main(args):
    cap_vid(args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Give output name for video")

    parser.add_argument("--output", type=str, help="output img dir", default="output")
    args = parser.parse_args()
    main(args)
