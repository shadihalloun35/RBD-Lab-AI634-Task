# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:41:51 2021

@author: shadi
"""

import VideoHandling
import ObjectTracking
import ObjectDetection
import Utillis

shadiVideoPath = 'C:\\HaifaUniversity\\RBD Lab\\RBD-Lab-AI634-Task\\ai634Data\\wetransfer_algo_2021-08-26_1138\\Camera2_1280_720.mp4'
ibrahemVideoPath = 'C:\\HaifaUniversity\\RBD Lab\\RBD-Lab-AI634-Task\\ai634Data\\wetransfer_algo_2021-08-26_1138\\Camera2_1280_720.mp4'


if __name__=="__main__":
    
    videoPath = shadiVideoPath
    #VideoHandling.DisplayVideo(videoPath)
    #VideoHandling.WritingVideo()
    #ObjectTracking.TrackObject(videoPath)
    frame_Xcoordinates,frame_Ycoordinates,frame_Wcoordinates,frame_Hcoordinates = ObjectDetection.DetectObject(videoPath)
    templateImage = Utillis.GetTemplateImage(frame_Xcoordinates,frame_Ycoordinates,frame_Wcoordinates,frame_Hcoordinates)
    centroidsA = Utillis.FindingCentroids(templateImage,len(templateImage))
    
    
   
        