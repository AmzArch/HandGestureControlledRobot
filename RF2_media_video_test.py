import keras
import numpy as np
import cv2
import tensorflow as tf
import mediapipe as mp
import copy
import pickle

# Define the list of landmark names to be used
# landmark_names = ['cx1', 'cx2', 'cx3', 'cx4', 'cx5', 'cx6', 'cx7', 'cx8', 'cx9', 'cx10', 'cx11', 'cx12', 'cx13', 'cx14', 'cx15', 'cx16', 'cx17', 'cx18', 'cx19', 'cx20', 'cx21', 'cy1', 'cy2', 'cy3', 'cy4', 'cy5', 'cy6', 'cy7', 'cy8', 'cy9', 'cy10', 'cy11', 'cy12', 'cy13', 'cy14', 'cy15', 'cy16', 'cy17', 'cy18', 'cy19', 'cy20', 'cy21']
# model_dict = pickle.load(open(fr"C:\Users\Archit Jain\OneDrive - Arizona State University\Desktop\ASU Classes\EGR 598 Exp and Depl of Robotics\Project\model_1.p", 'rb'))
model_dict = pickle.load(open(fr"C:\Users\Archit Jain\OneDrive - Arizona State University\Desktop\ASU Classes\EGR 598 Exp and Depl of Robotics\Project\Sign_Language_Grey_classifier_2.p", 'rb'))



model = model_dict['model']
cap = cv2.VideoCapture(0)
key = [0,1,2,3,4,5,6,7,8,9]


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.7)

while True:
    data_aux = []
    x_ = []
    y_ = []

    ret, image = cap.read()
    if not ret:
            break
    H, W, _ = image.shape
    # image = cv2.flip(image, 1)  # Mirror display
    # debug_image = copy.deepcopy(image)
    # Detection implementation #############################################################
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # image.flags.writeable = False
    # # results = hands.process(image)
    # image.flags.writeable = True


    # # Initialize the Mediapipe Hands model
    # mp_hands = mp.solutions.hands
    # hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.85)

    # # Process the current frame with Mediapipe Hands model
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract the cx and cy coordinates of the landmarks and store them in a list
            mp_drawing.draw_landmarks(
                image,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        x1 = int(min(x_) * W) - 10
        y1 = int(min(y_) * H) - 10

        x2 = int(max(x_) * W) - 10
        y2 = int(max(y_) * H) - 10

        prediction = model.predict([np.asarray(data_aux)])

        predicted_character = key[int(prediction[0])]

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 0), 4)
        # cv2.putText(image, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
        #             cv2.LINE_AA)

        print(predicted_character)

    cv2.imshow('frame', image)
    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()






