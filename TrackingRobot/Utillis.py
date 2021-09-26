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