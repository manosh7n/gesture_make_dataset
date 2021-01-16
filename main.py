# Запись датасета
# каждый жест записывается в отдельную папку
# dataset/(жест)/(номер жеста)/(txt файл координат + скриншот)


import cv2
import mediapipe as mp
import os


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.55, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

count_gest = 0
state = False
dir_name = 0

GESTURE = 'bye'

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
                with open(f'dataset/{GESTURE}/{dir_name}/a_{count_gest}_.txt', 'a+') as out:
                    for points in hand_landmarks.landmark:
                        print(points.x, points.y, points.z, file=out, end=' ')
                    print(file=out)

            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)
    if count_gest % 3 == 0 and state:
        cv2.imwrite(f'dataset/{GESTURE}/{dir_name}/a_{count_gest}.png', image)

    key = cv2.waitKey(5)
    if key & key == 27:
        break
    if key == ord('q'):
        if state == False:
            dir_name += 1
            os.mkdir(f'dataset/{GESTURE}/{dir_name}')
            print(f'{dir_name} НАЧАЛО')
        else:
            print("End")
        state = not state

    count_gest += 1

hands.close()
cap.release()
