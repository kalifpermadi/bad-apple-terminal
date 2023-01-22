# Import all necessary library
import cv2
import os
import time
from playsound import playsound
from wakepy import keepawake

def start(): # Define a functino to start the code
    video = cv2.VideoCapture("video.mp4") # Set video file
    totalFrames = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) # Get video total frames
    fps = int(video.get(cv2.CAP_PROP_FPS) * 8 / 30) # Calculate the fps that we want (30 * 8 / 30 = 8 fps)
    interval = 1 / fps # Calculate the interval between frames in seconds
    audio = "audio.mp3" # Set audio file
    playsound(audio, False) # Play audio

    # Loop through all the frames times 4 with increment by 15
    for n in range(0, totalFrames * 4, 15):
        n = round(n / 4) # Divide by 4 after multiplying it by 4
        startTime = time.time() # Start time
        video.set(cv2.CAP_PROP_POS_FRAMES, n) # Set the n-th frame of the video
        _, frame = video.read() # Take the n-th frame
        height, width, _ = frame.shape # Get height and width of the frame
        
        # Resize frame if the width is more than 144px
        if width > 144:
            frame = cv2.resize(frame, (144, round(height * 144 / width)), interpolation = cv2.INTER_NEAREST)

        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Grayscale the frame
        height, width, _ = frame.shape # Get height and width of the frame after resize

        string = "" # Declare strings to be printed
        afterString = ""
        brightness = [" ", ".", ",", ":", ";", "+", "*", "?", "@"] # Set brightness strings from black, dark gray, light gray, to white

        # Loop through every row of pixels, increment by 2 to maintain aspect ratio in terminal
        for row in range(0, height, 2):

            # Center the display
            for i in range(46):
                string += " "

            # Loop through every column of pixels
            for col in range(0, width):
                b, g, r = frame[row, col] # Get pixel information
                string += brightness[round(int(b + g + r) / 32)] # Calculate how "bright" the pixel is and add a character from the "brightness" list

                # Add credit (lmao)
                if n <= 40 and row == height // 2 and col == width // 3:
                    string += "Created by Kalif (https://kalifpermadi.github.io)" 

            string += "\n" # Add a new line

        os.system('cls') # Clear command line
        print(string) # Print frame that has been "translated" to string

        # Keep the credit while the code is running
        if n > 40:
            print("Created by Kalif (https://kalifpermadi.github.io)")
        endTime = time.time() # End time
        delay = interval - (endTime - startTime) # Calculate interval minus execution time

        # If it's less than 0, then set to 0
        if delay < 0:
            delay = 0

        time.sleep(delay) # Delay for a few moment before execute the next frame
        
    video.release() # Release video (idk why but it seems important)

with keepawake(keep_screen_awake=True): # Keep the screen awake
    while True: # Loop infinitely
        start() # Run the function 
        os.system("cls") # CLear command line after the function has finished
        time.sleep(3) # Add delay for 3 seconds