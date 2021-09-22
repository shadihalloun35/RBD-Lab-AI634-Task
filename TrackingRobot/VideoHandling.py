# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:57:27 2021

@author: shadi
"""

import cv2
#import numpy as np

def WritingVvideo():

    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)
    
    # Check if camera opened successfully
    if (cap.isOpened() == False): 
      print("Unable to read camera feed")
    
    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    
    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

    while(True):
      ret, frame = cap.read()
    
      if ret == True: 
        
        # Write the frame into the file 'output.avi'
        out.write(frame)
    
        # Display the resulting frame    
        cv2.imshow('frame',frame)
    
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    
      # Break the loop
      else:
        break  
    
    # When everything done, release the video capture and video write objects
    cap.release()
    out.release()

# Closes all the frames
cv2.destroyAllWindows()
def DisplayVideo(videoPath):
    
    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture(videoPath)
    
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
      print("Error opening video stream or file")
    
    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
      ret, frame = cap.read()
      if ret == True:
    
        # Display the resulting frame
        cv2.imshow('Frame',frame)
    
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break
    
      # Break the loop
      else: 
        break
    
    # When everything done, release the video capture object
    cap.release()
    
    # Closes all the frames
    cv2.destroyAllWindows()