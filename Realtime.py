import cv2 
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt 
from collections import deque
import os 
from datetime import datetime
import test as t
import traceback


bot = t.TelegramBot(t.token, t.chat_id)



titre= ['WeaponViolence', 'ViolenceCleaned', 'NonViolence']
mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")


def preprocess_frame(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (224, 224)).astype("float32")
    frame -= mean
    return frame


def Detect():

    video = "fight.mp4"
    #video = "camera"
    print("[INFO] loading model and label binarizer...")
    model = load_model("model.h5")
    vpath = "fight.mp4"
    if video == "camera":
        vpath = 1
    vs = cv2.VideoCapture(vpath)


    """
    output_file = 'wepon_video.avi'
    fourcc =  cv2.VideoWriter_fourcc(*'MJPG')
    fps = 30
    output_width, output_height = (640, 480)  # Adjust the output video resolution as needed
    output_video = cv2.VideoWriter(output_file, fourcc, fps, (output_width, output_height))
    """
    message = ''
    frame1 = 0
    image_path = ''
    counter = 0
    while True:
        grabbed, frame = vs.read()
        count = 0
        
        if not grabbed:
            break

        processed_frame = preprocess_frame(frame)
        preds = model.predict(np.expand_dims(processed_frame, axis=0))[0]
        i = np.argmax(preds)
        label = titre[i]
        # Save frames and timestamps for 'Weapon' class  C:\Users\user\Downloads\Smart Eye\violence_frames\frame_2023-06-04_20-00-54-859484.jpg
        if label == 'WeaponViolence' or label == 'ViolenceCleaned':
            counter +=1
            if counter >= 60:
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
                frame1 = frame
                cv2.imshow(f"{label}", frame1)
                cv2.waitKey(1)

                message = f"{label} detected at {timestamp}"
                print(message)

                # Save the frame as an image
                image_path = f"frame_{timestamp}.jpg"
                cv2.imwrite(image_path, frame1)

                # Send the image
                bot.send_message(message)
                bot.send_image(image_path, caption='Here is the Violence Image')
                if counter == 61:
                    import smartEyeBot
                    counter = 0
                    
                

        if label == 'NonViolence':
            cv2.imshow(f"{label}", frame)
            cv2.waitKey(1)
            pass

        #cv2.imshow("WeponViolence", frame1)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
    # Release the video writer and capture
    #output_video.release()

    vs.release()
    cv2.destroyAllWindows()
    # Provide the path to the saved video file

    return message, image_path

# Run this
try:
    message, image_path = Detect()

# If error occurs, send the error with its trace
except Exception as e:
    print(traceback.format_exc())
    bot.send_error_message(traceback.format_exc())


#print("Saved video file:", output_file_path)
#print("Saved video file:", output_file_path1)