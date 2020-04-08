import cv2
import os
import argparse


def getFrame(vidcap, sec, output_dir, idx):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        path = os.path.join(output_dir, "image" + str(idx) + ".jpg")
        print(idx)
        cv2.imwrite(path, image)  # save frame as JPG file
    return hasFrames


def get_vid(input_vid, frate, output_dir):
    vidcap = cv2.VideoCapture(input_vid)
    sec = 0
    frameRate = args.frate  # //it will capture image in each 0.5 second
    if len(os.listdir(output_dir)) > 0:
        idx = len(os.listdir(output_dir))
    else:
        idx = 1
    success = getFrame(vidcap, sec, output_dir, idx)
    while success:
        idx += 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(vidcap, sec, output_dir, idx)


def main(args):
    if os.path.exists(args.input):
        get_vid(args.input, args.frate, args.output)
    else:
        print("Input video does not exist")
        exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Give input video path, output video path, and framerate"
    )
    parser.add_argument(
        "--input", type=str, help="Video input file path", default="input.mp4"
    )
    parser.add_argument(
        "--output", type=str, help="image output dir", default="output_imgs/"
    )
    parser.add_argument(
        "--frate", type=float, help="Video frame rate 1.0 - 0 per second", default=0.5
    )
    args = parser.parse_args()
    main(args)
