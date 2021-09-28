# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:45:18 2021

@author: shadi
"""

import numpy as np
import cv2

def GetBackground(videoPath):
    cap = cv2.VideoCapture(videoPath)
    # we will randomly select 50 frames for the calculating the median
    frame_indices = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=50)
    # we will store the frames in array
    frames = []
    for idx in frame_indices:
        # set the frame id to read that particular frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        frames.append(frame)
    # calculate the median
    median_frame = np.median(frames, axis=0).astype(np.uint8)
    return median_frame


def GetTemplateImage(frame_Xcoordinates,frame_Ycoordinates,frame_Wcoordinates,frame_Hcoordinates):
    
    firstPoint = (frame_Xcoordinates[0],frame_Ycoordinates[0])
    secondPoint = (frame_Xcoordinates[0]+frame_Wcoordinates[0],frame_Ycoordinates[0])
    thirdPoint = (frame_Xcoordinates[0],frame_Ycoordinates[0]+frame_Hcoordinates[0])
    fourthPoint = (frame_Xcoordinates[0]+frame_Wcoordinates[0],frame_Ycoordinates[0]+frame_Hcoordinates[0])
    return [firstPoint,secondPoint,thirdPoint,fourthPoint]


def FindingCentroids(points,dim):
    
    sumPointsX = 0
    sumPointsY = 0
    
    for point in points:
        sumPointsX += point[0]
        sumPointsY += point[1]
    
    return (sumPointsX/dim,sumPointsY/dim)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
