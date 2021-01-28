import cv2
import mediapipe as mp
import os
from tensorflow import keras
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.55, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

model = keras.models.load_model('model.h5')

count_gest = 0
state = False
gesture = []
filler = [-1.0]*63
gestures = ['hello', 'money', 'bye', 'good', 'mom']

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
            if count_gest % 3 == 0 and state:
                for points in hand_landmarks.landmark:
                    gesture.extend([points.x, points.y, points.z])

            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)


    key = cv2.waitKey(5)
    if key & key == 27:
        break
    if key == ord('q'):
        if state == False:
            print(f'НАЧАЛО ЗАПИСИ')
        else:
            length = len(gesture)
            diff = (1764 - length) // 63
            front = True
            for _ in range(diff):
                if front:
                    gesture = list(np.insert(gesture, 0, filler))
                else:
                    gesture.extend(filler)
                front = not front

            gesture = np.array(gesture).reshape((-1, 28, 63))
            pred = np.argmax(model.predict(gesture)[0])
            print(gestures[pred])

            gesture = []
            print("КОНЕЦ")
        state = not state



    count_gest += 1

hands.close()
cap.release()
