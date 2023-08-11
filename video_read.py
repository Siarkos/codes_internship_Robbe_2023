#open the video
video_folder = '/home/david/Documents/MOU3828/MOU3828_20230215-1627'
video_name = 'MOU3828_20230215-1627_tracked.avi'
start_frame = 50

import glob, os, time, datetime
import cv2 

video_path = video_folder + '/' + video_name

#check if the video exist
if glob.glob(video_path):
    print('Video found')
else :
    print(video_path)
    raise Exception("Video not found : " + video_path) 

#open the video
Read_video = cv2.VideoCapture(video_path)
if not Read_video.isOpened() :
    raise Exception("Video found but cannot be opened") 
Read_video.set(cv2.CAP_PROP_POS_FRAMES, start_frame) # set the index of the next frame to be read to the one with index 0

while True :
    ret, frame = Read_video.read()#read the frame indicated
    
    #if the frame can be found, plot it, else stop the program
    if not ret : break
    frame = cv2.resize(frame, (1024,1024), interpolation = cv2.INTER_AREA) 
    cv2.imshow("picture", frame)

    key = cv2.waitKey(0)
    if key == ord("q") :
        break
    elif key == ord("j"):
        if start_frame != 0 : 
            start_frame -= 1
    elif key == ord("l") :
        start_frame += 1

    #set the index of the next video to be plotted
    Read_video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)


Read_video.release()
#cv2.destroyAllWindows()