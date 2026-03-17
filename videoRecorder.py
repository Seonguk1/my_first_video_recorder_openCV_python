import cv2 as cv

video = cv.VideoCapture(0)
if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS)
    wait_msec = int(1 / fps * 1000)
    
    target_fourcc = 'XVID'
    writer = None
    
    is_record = False
    is_flip = False
    is_gray = False
    
    while True:
        valid, img = video.read()
        if not valid:
            break
        height, width = img.shape[:2]
        
        if is_gray:
            # 컬러를 흑백으로 변환 
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            # VideoWriter와 호환성을 위해 다시 BGR로 변환
            img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        
        if is_flip:
            img = cv.flip(img, 1) # 좌우반전
        
        if is_record:
            cv.circle(img, (width//2, 30), 20, (0, 0, 255), -1)
            writer.write(img) # 녹화 중인 영상 저장
        
        
        cv.imshow('Video', img)
        
        key = cv.waitKey(wait_msec)
        if key == 27: # ESC
            break
        elif key == ord(' '): # Space: Record 모드 변환
            is_record = not is_record
            if is_record:
                writer = cv.VideoWriter('output.avi', cv.VideoWriter_fourcc(*target_fourcc), fps, (width, height))
        elif key == ord('f'): # f: Flip 모드 변환
            is_flip = not is_flip
        elif key == ord('g'): # g: 흑백 모드 변환
            is_gray = not is_gray
            
    video.release()
    writer.release()

cv.destroyAllWindows()