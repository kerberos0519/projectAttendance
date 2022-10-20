###############################################
# TM(TeachableMachine) 관련 및 화면 처리 파일
###############################################
import cv2
import numpy as np
from keras.models import load_model

import time
import commonutil
import db

# 웹캠에서 받은 이미지 처리
def processingCam():
    # Load the model
    model = load_model(commonutil.getRootPath() +'/asset/model/keras_model.h5')

    # 가중치 파일 경로
    cascade_filename = commonutil.getRootPath() +'/asset/model/haarcascade_frontalface_alt.xml'

    # 모델 불러오기
    cascade = cv2.CascadeClassifier(cascade_filename)

    # CAMERA can be 0 or 1 based on default camera of your computer.
    camera = cv2.VideoCapture(0)

    # Grab the labels from the labels.txt file. This will be used later.
    labels = open(commonutil.getRootPath() +'/asset/model/labels.txt', 'r', encoding='utf_8').readlines()

    for i, lb in enumerate(labels):
        # print("[{}, {}]".format(i, lb))
        labels[i] = lb.replace('\n', '')

    outText = 'Not Defined'

    while True:
        # Grab the webcameras image.
        ret, image = camera.read()

        # Resize the raw image into (224-height,224-width) pixels.
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        imageTemp = cv2.resize(image,dsize=None,fx=1.0,fy=1.0)
        # 그레이 스케일 변환
        gray = cv2.cvtColor(imageTemp, cv2.COLOR_BGR2GRAY)
        # cascade 얼굴 탐지 알고리즘 
        results = cascade.detectMultiScale(gray,            # 입력 이미지
                                        scaleFactor= 1.5,# 이미지 피라미드 스케일 factor
                                        minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                        minSize=(20,20)  # 탐지 객체 최소 크기
                                        )        
                                        
        # 결과값 = 탐지된 객체의 경계상자 list                                                                           
        for box in results:
            # 좌표 추출       
            x, y, w, h = box
            # 경계 상자 그리기
            cv2.rectangle(image, (x,y), (x+w, y+h), (255,255,255), thickness=2)

        cv2.putText(image, outText, (0,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))

        # Show the image in a window
        cv2.imshow('Webcam Image', image)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1
        # Have the model predict what the current image is. Model.predict
        # returns an array of percentages. Example:[0.2,0.8] meaning its 20% sure
        # it is the first label and 80% sure its the second label.
        probabilities = model.predict(image)
        # print(probabilities)

        pbList = probabilities[0]
        sumPb = round(sum(pbList), 3)
        print(labels)
        print("{} %".format(100 * np.round(pbList, 3)))

        # Print what the highest value probabilitie label
        maxLabel = labels[np.argmax(probabilities)].split(' ')

        resultDict = {'maxPb':round(np.max(probabilities) * 100, 2), 'maxId':maxLabel[0], 'maxName':maxLabel[1]}
        print('주어진 모델 중 가장 높은 확률인 {0} % 확률로 {1} 으/로 추정'.format(resultDict['maxPb'], resultDict['maxName']))

        if resultDict['maxPb'] >= 90:
            try :
                # db 입력 처리 - 임시로 DB 입력은 안함
                # db.doAttend(resultDict['maxName'], commonutil.getNowDateYmd())
                # 0.5초 대기(연속 입력 저지)
                # time.sleep(0.5)
                pass
            except :
                # nop... T.T
                cv2.putText(image, 'already attend today !!!', (0,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))

        outText = str(resultDict['maxId']) +' '+ str(resultDict['maxPb']) +' %'

        # Listen to the keyboard for presses.
        keyboard_input = cv2.waitKey(1)
        # 27 is the ASCII for the esc key on your keyboard.
        if keyboard_input == 27:
            break

        # 0.2 sec wait
        time.sleep(0.2)

    camera.release()
    cv2.destroyAllWindows()
    


