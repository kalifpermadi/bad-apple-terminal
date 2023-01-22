# Import all necessary library
import cv2
import os
import time
from playsound import playsound

def start(): # Define a functino to start the code
    video = cv2.VideoCapture("video.mp4") # Get the video
    totalFrames = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) # Get video total frames
    fps = int(video.get(cv2.CAP_PROP_FPS)) / 5 # Calculate the fps that we want (30 / 5 = 6 fps)
    interval = 1 / fps # Calculate the interval between frames in seconds
    playsound("audio.mp3", False) # Play audio

    # Loop through all the frames divided by 5 (6 fps)
    for loop in range(0, totalFrames, 5):
        startTime = time.time() # Start time
        video.set(cv2.CAP_PROP_POS_FRAMES, loop) # Set the loop-th frame of the video
        _, frame = video.read() # Take the frame
        height, width, _ = frame.shape # Get height and width of the frame
        
        # Resize frame if the width is more than 144px
        if width > 144:
            frame = cv2.resize(frame, (144, round(height * 144 / width)), interpolation = cv2.INTER_NEAREST)

        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Grayscale the frame
        height, width, _ = frame.shape # Get height and with of the frame after resize

        string = "" # Declare string to be printed
        brightness = " .,-~:;=!*#$@" # Set brightness string from black, dark gray, light gray, to white

        # Loop through every row of pixels, divided by 2 to maintain aspect ratio
        for row in range(0, height, 2):

            # Loop through every width of pixels
            for col in range(0, width):
                b, g, r = frame[row, col] # Get pixel information
                string += brightness[round(int(b + g + r) / 21)] # Calculate how "bright" the pixel is and add a character according to the "brightness" string

            string += "\n" # Add a new line

        os.system('cls') # Clear command line
        print(string) # Print the string
        endTime = time.time() # End time
        interval -= (endTime - startTime) # Calculate interval minus execution time

        # If it's less than 0, then set to 0
        if interval < 0:
            interval = 0

        time.sleep(interval) # Delay for interval seconds before execute the next frame
        
    video.release() # Release video (idk why but it seems important)

start() # Run the function 
os.system("cls") # CLear command line after the function has finished