# Import all necessary library
import cv2
import os
import time
from playsound import playsound
from wakepy import keepawake

def start():
    video = cv2.VideoCapture("video.mp4")
    totalFrames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS) * 8 / 30) # Video fps is 30, so fps = 8
    interval = 1 / fps
    audio = "audio.mp3"
    playsound(audio, False)
    brightness = [" ", ".", ",", ":", ";", "+", "*", "?", "@"]

    # Loop through the frames in 8 fps
    for n in range(0, totalFrames * 4, 15):
        n = round(n / 4)
        startTime = time.time()
        video.set(cv2.CAP_PROP_POS_FRAMES, n)
        _, frame = video.read()
        height, width, _ = frame.shape
        
        # Resize video to 144p if it's larger than 144p
        if width > 144:
            frame = cv2.resize(frame, (144, round(height * 144 / width)), interpolation = cv2.INTER_NEAREST)
            height, width, _ = frame.shape
        string = ""

        # Loop through all the frame height
        for row in range(0, height, 2):
            # Loop through all the frame width
            for col in range(0, width):
                b, g, r = frame[row, col]
                string += brightness[round(int(b + g + r) / 32)]    # Convert pixels into ASCII characters
            string += "\n"
        os.system('cls')
        print(string)
        endTime = time.time()
        delay = interval - (endTime - startTime)
        if delay < 0:
            delay = 0
        time.sleep(delay)
    video.release()

# Repeat the function infinitely and keep the screen awake
with keepawake(keep_screen_awake=True):
    while True:
        start()
        os.system("cls")
        time.sleep(5)