#default
default = '/home/mrpi314/Music/Super_Mario_Bros.mp3'
#other options:
#Careless Whisper:
a = '/home/mrpi314/Music/Careless_whisper.mp3'
wstp=input('what song? (a=Mario theme b=Careless whisper ')
if 'a' in wstp:
    song=default
elif 'b' in wstp:
    song=a
else:
    song=default
from pygame import mixer
from datetime import datetime
currentTime = datetime.now().strftime("%H:%M")
mixer.init()
entx = 0
smt=0
brk=0
wait = 400
tmr = wait
while True:
    import cv2, time, os
    import time as timey
    #from rpi_lcd import LCD
    #lcd=LCD()
    static_back = None
    motion_list = [ None, None ]
    time = []
    video = cv2.VideoCapture(0)
    print('ready')
    while True:
        currentTime = datetime.now().strftime("%H:%M")
        timey.sleep(0.35)
        if not tmr == 'Game Over':
            if entx == 0:
                #lcd.text(currentTime, 1)
                pass
            else:
                tmr-=1
                #lcd.text(str(tmr), 1)
        if tmr == 100:
            mixer.music.set_volume(0)
            mixer.Channel(1).play(mixer.Sound('/home/mrpi314/Music/smb_warning.wav'))
            timey.sleep(2)
            mixer.music.set_volume(1)
        if tmr == 0:
            mixer.music.stop()
            timey.sleep(1)
            mixer.Channel(2).play(mixer.Sound('/home/mrpi314/Music/smb_mariodie.wav'))
            tmr='Game Over'
            lcd.text(tmr, 1)
        check, frame = video.read()
        motion = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if static_back is None:
            static_back = gray
            continue
        diff_frame = cv2.absdiff(static_back, gray)
        thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
        cnts,_ = cv2.findContours(thresh_frame.copy(), 
                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            smt+=1
            if smt == 20:
                print('error')
                smt=0
                brk=1
                break
            motion = 1
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if brk == 1:
            print('resetting')
            timey.sleep(3)
            brk = 0
            break
        motion_list.append(motion)
        motion_list = motion_list[-2:]
    
        if motion_list[-1] == 1 and motion_list[-2] == 0:
            video.release()
            cv2.destroyAllWindows()
            if entx == 0:
                mixer.music.load("/home/mrpi314/Music/Mario_Pipe.mp3")
                mixer.music.play()
                timey.sleep(0.8)
                mixer.music.load(song)
                mixer.music.play(-1)
                timey.sleep(3)
                entx = 1
                break
            else:
                mixer.music.stop()
                mixer.music.load("/home/mrpi314/Music/Mario_Pipe.mp3")
                mixer.music.play()
                timey.sleep(3)
                entx = 0
                tmr=wait
                break
        if motion_list[-1] == 0 and motion_list[-2] == 1:
            video.release()
            cv2.destroyAllWindows()
            if entx == 0:
                mixer.music.load(song)
                mixer.music.play(-1)
                timey.sleep(3)
                entx = 1
                break
            else:
                mixer.music.stop()
                mixer.music.load("/home/mrpi314/Music/Mario_Pipe.mp3")
                mixer.music.play()
                timey.sleep(3)
                entx = 0
                tmr=wait
                break
        #cv2.imshow("Color Frame", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            if motion == 1:
                video.release()
                cv2.destroyAllWindows()
                if entx == 0:
                    mixer.music.load(song)
                    mixer.music.play(-1)
                    timey.sleep(3)
                    entx = 1
                    break
                else:
                    mixer.music.stop()
                    mixer.music.load("/home/mrpi314/Music/Mario_Pipe.mp3")
                    mixer.music.play()
                    timey.sleep(3)
                    entx = 0
                    tmr=wait
                    break
            break 
    video.release()
    cv2.destroyAllWindows()
