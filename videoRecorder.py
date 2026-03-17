import cv2 as cv

video = cv.VideoCapture(0)
if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS)
    wait_msec = int(1 / fps * 1000)
    
    while True:
        valid, img = video.read()
        if not valid:
            break
        
        cv.imshow('Video', img)
        
        key = cv.waitKey(wait_msec)
        if key == 27: # ESC
            break
        
cv.destroyAllWindows()