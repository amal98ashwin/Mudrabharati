# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:49:56 2021

@author: Ashwin
"""

import tkinter as tk
import pickle
from PIL import Image, ImageTk
import cv2
import mediapipe as mp
from functions import _normalized_to_pixel_coordinates,get_face_size,locate_and_point,calculate_position,get_position_hand,gesture_prediction,dictionary,state_prediction

class MainWindow():
    def __init__(self, window, cap):
        self.window = window
        self.cap = cap
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.interval = 1 # Interval in ms to get the latest frame
        # Create canvas for image
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height+200)
        self.canvas.grid(row=0, column=0)
        # Declare detection variables
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.mp_face_detection = mp.solutions.face_detection      
        self.PRESENCE_THRESHOLD = 0.5
        self.RGB_CHANNELS = 3
        self.RED_COLOR = (0, 0, 255)
        self.VISIBILITY_THRESHOLD = 0.5
        # Declare word variables
        self.gesture = gesture_prediction()
        self.lang_flag = "hindi"
        self.hit = dictionary(self.lang_flag)
        self.mode = state_prediction()
        self.character_t_1 = ""
        self.word = ""
        # Load saved calibration files
        with open("diff_1.txt",'rb') as fp:
            self.diff_1 = pickle.load(fp)
        with open("diff_9.txt",'rb') as fp:
            self.diff_9 = pickle.load(fp)
        with open("calibrated_position_face_factor.txt",'rb') as fp:
            self.face_fac = pickle.load(fp)
        # Update image on canvas
        self.update_image()
        
    def update_image(self):
        # Get the latest frame and convert image format
        self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # to RGB
        self.image = cv2.flip(self.image, 1)
        
        # Detect hand and face
        with self.mp_hands.Hands(
            min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
            with self.mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
                face_loc = []
                hand_loc = []
                # det_flag_cons = "Good" 
                # det_flag_vow = "Good"
                image_rows, image_cols, _ = self.image.shape
                self.image.flags.writeable = True
                
                # Detect face
                results_face = face_detection.process(self.image)
                if results_face.detections:
                    for detection in results_face.detections:
                        # self.mp_drawing.draw_detection(self.image, detection)
                        for keypoint in detection.location_data.relative_keypoints:
                        
                            landmark_px = _normalized_to_pixel_coordinates(keypoint.x, keypoint.y,
                                                                          image_cols, image_rows)
                            if landmark_px:
                                face_loc.append(landmark_px)                      
                        
                # Detect hands
                results_hands = hands.process(self.image)
                if results_hands.multi_hand_landmarks:
                    for hand_landmarks in results_hands.multi_hand_landmarks:
                        # self.mp_drawing.draw_landmarks(self.image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)   
                        for idx, landmark in enumerate(hand_landmarks.landmark):
                        
                            landmark_px = _normalized_to_pixel_coordinates(landmark.x, landmark.y,
                                                                          image_cols, image_rows)
                            if landmark_px:
                                hand_loc.append(landmark_px)  
        
        # Get face size and hand locations
        face_size = get_face_size(face_loc,image_rows)
        image,face_loc,hand_1_loc,hand_2_loc,hand_1_flag,hand_2_flag = locate_and_point(self.image,face_loc,hand_loc)
                
        # get hand gesture
        consonant,vowel,punctuation = gesture_prediction.get_gesture(self.gesture,self.image,face_loc,hand_1_loc,hand_2_loc,hand_1_flag,hand_2_flag,hand_loc,image_rows,image_cols)
        
        # get hand position
        self.image,pos_in_order_right,pos_in_order_left = calculate_position(self.image,self.diff_1,self.diff_9,face_loc,face_size,self.face_fac,image_rows,image_cols)
        
        if hand_1_flag=="Right":
            position_right = get_position_hand(hand_1_loc,face_loc,pos_in_order_right,image_rows,image_cols)
            position_left = 0
        elif hand_1_flag=="Left":
            position_left = get_position_hand(hand_1_loc,face_loc,pos_in_order_left,image_rows,image_cols)
            position_right = 0
        else:
            position_left = 0
            position_right = 0
        
        if hand_2_flag=="Right":
            position_right = get_position_hand(hand_2_loc,face_loc,pos_in_order_right,image_rows,image_cols)
        elif hand_2_flag=="Left":
            position_left = get_position_hand(hand_2_loc,face_loc,pos_in_order_left,image_rows,image_cols)
        
        # get character
        character, dheerga = dictionary.get_character(self.hit,consonant,vowel,punctuation,position_right,position_left)
        state = state_prediction.get_state(self.mode,character,self.character_t_1)            
        self.character_t_1 = character
        
        # Edit word
        self.word = state_prediction.get_word(self.mode,self.word,state,character,dheerga)
        
        # Convert image to tkinter displayable format
        self.image = Image.fromarray(self.image) # to PIL format
        self.image = ImageTk.PhotoImage(self.image) # to ImageTk format
        # Update image
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        self.canvas.create_text(20,self.height+10,anchor='nw',fill="black",font="Times 20 bold",
                        text=self.word+'\n')
        self.canvas.create_text(self.width-10,self.height+10,anchor='ne',fill="darkblue",font="Times 20 bold",
                        text=character+'\n'+dheerga+'\n') # \n is needed to diplay full character
        # Repeat every 'interval' ms
        self.window.after(self.interval, self.update_image)
        
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root, cv2.VideoCapture(1))
    root.mainloop()
    