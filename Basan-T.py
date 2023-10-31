import cv2
import mediapipe as mp
import time
from google.protobuf.json_format import MessageToDict
from HotKeys import *
import os
import sys
import threading


# Play
# Pause
# forward
# reverse
# brightness
# volume
# full screen
# exit full screen

vlc_path=r"C:\Program Files\VideoLAN\VLC"
video_path=r"I:\loli.mp4"

VLC=True



time.sleep(2.0)

mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands

def get_label(results):
    for i in results.multi_handedness:				
        # Return whether it is Right or Left Hand
        label = MessageToDict(i)['classification'][0]['label']
    return label

tipIds=[4,8,12,16,20]


def cal_distance(list,id1,id2):
    x1=list[tipIds[id1]][1]
    y1=list[tipIds[id1]][2]
    x2=list[tipIds[id2]][1]
    y2=list[tipIds[id2]][2]
    return (((x2-x1)**2 +(y2-y1)**2)**0.5)//4



def startVLC():
    try:
        os.chdir(vlc_path)
        command = f'"vlc ""{video_path}"'
        os.system(command)
        # os.startfile('C:\Program Files\VideoLAN\VLC\\vlc.exe')
    except:
        print("File not found.\n Please start a video of your choice")

def camera():
    video=cv2.VideoCapture(0)
    with mp_hand.Hands(min_detection_confidence=0.5,
                min_tracking_confidence=0.5,max_num_hands=1) as hands:
        while True:
            ret,image=video.read()        
            if not ret:
                print("Error: Video capture failed.")
                break
            image = cv2.flip(image, flipCode = 1)     
            image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)        
            image.flags.writeable=False
            results=hands.process(image)
            image.flags.writeable=True
            image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            lmList=[]
            if results.multi_hand_landmarks:
                for num,hand in enumerate(results.multi_hand_landmarks):
                    myHands=results.multi_hand_landmarks[0]
                    for id, lm in enumerate(myHands.landmark):
                        h,w,c=image.shape
                        cx,cy= int(lm.x*w), int(lm.y*h)
                        lmList.append([id,cx,cy])
                        mp_draw.draw_landmarks(image, hand, mp_hand.HAND_CONNECTIONS)

                    if get_label(results):
                        hand_label= get_label(results)
                        #print(hand_label)



            fingers=[]
            if len(lmList)!=0:
                if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1,5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                total=fingers.count(1)

                VOLUME=False 
                BRIGHTNESS=False         

                #Right thumb,index and pinky

                if hand_label=="Right" and lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2] :
                    PlayPause()
                    print("Play")
                
                # Right thumb towards right

                if hand_label=="Right" and lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] and lmList[tipIds[1]][2] > lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2] :
                    Forward()
                    print("Forward")

                #Right index towards left

                if hand_label=="Right" and lmList[tipIds[1]][1] < lmList[tipIds[1]-1][1] and lmList[tipIds[1]][2] > lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2] :
                    Backward()
                    print("Backward")  

                # print(cal_distance(lmList,2,3))

                #Touch right index and middle to activate, pinch to change

                if hand_label=="Right" and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2] and cal_distance(lmList,1,2)<10:# and calculate distance 
                    VOLUME=True
                    print("Volume")

                if VOLUME==True:
                    cv2.line(image,(lmList[tipIds[1]][1],lmList[tipIds[1]][2]),(lmList[tipIds[0]][1],lmList[tipIds[0]][2]),(180,105,255),5) 
                    dist=cal_distance(lmList,0,1)
                    if dist>10:
                        VolumeUp()
                    else:
                        VolumeDown()   

                #Touch left index and middle to activate, pinch to change   

                if hand_label=="Left" and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] < lmList[tipIds[2]-2][2] and cal_distance(lmList,1,2)<10:# and calculate distance 
                    BRIGHTNESS=True
                    print("Brightness")

                if BRIGHTNESS==True:
                    cv2.line(image,(lmList[tipIds[1]][1],lmList[tipIds[1]][2]),(lmList[tipIds[0]][1],lmList[tipIds[0]][2]),(180,105,255),5) 
                    dist=cal_distance(lmList,0,1)
                    if dist>10:
                        BrightnessUp()
                    else:
                        BrightnessDown()  

                #Reverse fist left hand
            
                if hand_label=="Left" and lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1] and lmList[tipIds[1]][2] > lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4]-2][2] :
                    mute()
                    print("Mute")

                #Left index and pinky

                if hand_label=="Left" and lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] and lmList[tipIds[1]][2] < lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2] > lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2] > lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4]-2][2] :
                    FullScreen()
                    print("Fullscreen")
                
                
                
            
                
            cv2.imshow("Frame",image)
            
            
            
            k=cv2.waitKey(1)
            if k==27:
                break
            
    video.release()
    cv2.destroyAllWindows()
    sys.exit()
    
camera_thread=threading.Thread(target=camera)
camera_thread.start()
startVLC()


