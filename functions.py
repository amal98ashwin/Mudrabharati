# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:22:19 2021

@author: Ashwin
"""

import cv2
import math
import numpy as np
import time
from scipy.spatial import distance
from keras.models import load_model
from typing import Tuple, Union
import scripts

def _normalized_to_pixel_coordinates(
    normalized_x: float, normalized_y: float, image_width: int,
    image_height: int) -> Union[None, Tuple[int, int]]:
  """Converts normalized value pair to pixel coordinates."""

  # Checks if the float value is between 0 and 1.
  def is_valid_normalized_value(value: float) -> bool:
    return (value > 0 or math.isclose(0, value)) and (value < 1 or
                                                      math.isclose(1, value))

  if not (is_valid_normalized_value(normalized_x) and
          is_valid_normalized_value(normalized_y)):
    # TODO: Draw coordinates even if it's outside of the image bounds.
    return None
  x_px = min(math.floor(normalized_x * image_width), image_width - 1)
  y_px = min(math.floor(normalized_y * image_height), image_height - 1)
  return x_px, y_px

def get_face_size(f_l,row_pix):
    if len(f_l)!=0:
        f_l = np.array(f_l)
        fs_min = np.min(f_l[:,0])/row_pix
        fs_max = np.max(f_l[:,0])/row_pix
        fs = round(fs_max-fs_min,2)
    else:
        fs = 0
        
    return fs
    
def locate_and_point(img,face_pt,hand_pts):
    hand_1_flag = "None"
    hand_2_flag = "None"
    # Get face coordinate from the keypoints detected
    face_pt = np.array(face_pt)
    if len(face_pt)!=0:
        face_pt = np.mean(face_pt,axis=0)
        cv2.circle(img,(int(face_pt[0]),int(face_pt[1])),radius = 5,color=(0,0,255),thickness=-1)       
    else:
        face_pt = [0,0]
    # Get hand coordinates of corresponding hand
    hand_pts = np.array(hand_pts)
    hand_1_pt = [0,0]
    hand_2_pt = [0,0]
    if len(hand_pts)==21:
        hand_1_pt = np.mean(hand_pts[:21,:],axis=0)
        hand_2_pt = [0,0]
        cv2.circle(img,(int(hand_1_pt[0]),int(hand_1_pt[1])),radius = 5,color=(255,0,0),thickness=-1)
        if hand_1_pt[0]<face_pt[0]:
            hand_1_flag = "Left"
        elif hand_1_pt[0]>face_pt[0]:
            hand_1_flag = "Right"
    elif len(hand_pts)==42:
        hand_1_pt = np.mean(hand_pts[:21,:],axis=0)
        hand_2_pt = np.mean(hand_pts[21:,:],axis=0)
        if hand_1_pt[0]<hand_2_pt[0]: # Check if 1 is left
            hand_1_flag = "Left"
            hand_2_flag = "Right"
        elif hand_1_pt[0]>hand_2_pt[0]: # Check if 1 is right
            hand_1_flag = "Right"
            hand_2_flag = "Left"
            
        cv2.circle(img,(int(hand_1_pt[0]),int(hand_1_pt[1])),radius = 5,color=(255,0,0),thickness=-1)
        cv2.circle(img,(int(hand_2_pt[0]),int(hand_2_pt[1])),radius = 5,color=(0,255,0),thickness=-1)       
        
    return img,face_pt,hand_1_pt,hand_2_pt,hand_1_flag,hand_2_flag

def calculate_position(image,diff_1,diff_9,face_loc,face_size,face_fac,image_rows,image_cols):
    pos_in_order_left = np.zeros((2,2))
    pos_in_order_right = np.zeros((9,2))
    
    # Right hand positions
    fac = face_size/face_fac
    pos_in_order_right[0,:] = fac*diff_1[0], fac*diff_1[1]
    pos_in_order_right[8,:] = fac*diff_9[0], fac*diff_9[1]
    pos_in_order_right[1,:] = np.mean((pos_in_order_right[0,0],pos_in_order_right[8,0])), pos_in_order_right[0,1]
    pos_in_order_right[2,:] = pos_in_order_right[8,0], pos_in_order_right[0,1]
    pos_in_order_right[3,:] = pos_in_order_right[0,0], np.mean((pos_in_order_right[0,1],pos_in_order_right[8,1]))
    pos_in_order_right[4,:] = pos_in_order_right[1,0], pos_in_order_right[3,1]
    pos_in_order_right[5,:] = pos_in_order_right[8,0], pos_in_order_right[3,1]
    pos_in_order_right[6,:] = pos_in_order_right[0,0], pos_in_order_right[8,1]
    pos_in_order_right[7,:] = pos_in_order_right[1,0], pos_in_order_right[8,1]
    
    # Left hand positions
    pos_in_order_left[0,:] = pos_in_order_right[1,:]
    pos_in_order_left[1,:] = pos_in_order_right[7,:]

    # Display points
    for ii in range(9):
        pos = (int(abs(face_loc[0]+pos_in_order_right[ii][0]*image_rows)),int(abs(face_loc[1]+pos_in_order_right[ii][1]*image_cols)))
        cv2.circle(image, pos, radius=3,color=(255,255,255), thickness=-1)
        
    for ii in range(2):
        pos = (int(abs(face_loc[0]-pos_in_order_left[ii][0]*image_rows)),int(abs(face_loc[1]+pos_in_order_left[ii][1]*image_cols)))
        cv2.circle(image, pos, radius=3,color=(255,255,255), thickness=-1)
        
    return image,pos_in_order_right,pos_in_order_left

def get_position_hand(hc,fc,comp,img_rows,img_cols):
    dists = np.zeros(len(comp))
    pred = abs(fc[0] - hc[0])/img_rows, abs(fc[1] - hc[1])/img_cols
    for i in range(len(comp)):
        dists[i] = distance.euclidean(pred,comp[i])
    pos = np.argmin(dists)
    
    return pos+1

class dictionary():
    def __init__(self, flag):
        self.cons, self.vowel, self.vowel_dheerga, self.swar_cons, self.swar_vow, self.swar_dh, self.punc = scripts.get_characters(flag)

    def get_character(self,c,v,p,pos_r,pos_l):
        # Check if punctuation
        if pos_l==2 and p!="relax":
            try:
                char = self.punc[p]
                dh = self.punc[p]
            except:
                char = "word_edit"
                dh = p
                
        # Check if vowel mode only
        elif (pos_l==1 and v!="relax") and (pos_r==0 or c=="relax"):
            try:
                char = self.vowel[v]
                dh = self.vowel_dheerga[v]
            except:
                char=""
                dh = ""
        
        # Check consonant only mode
        elif (pos_l==0 or v=="relax") and (pos_r!=0 and c!="relax"):
            try:
                char = self.cons[str(pos_r)+'_'+c]
                dh = self.cons[str(pos_r)+'_'+c]
            except:
                char=""
                dh=""
            
        # Check swarayukta mode
        elif (pos_l==1 and v!="relax") and (pos_r!=0 and c!="relax"):
            try:
                char_c = self.swar_cons[str(pos_r)+'_'+c]
                char_v = self.swar_vow[v]
                char_dh = self.swar_dh[v]
                char = char_c+char_v
                dh = char_c+char_dh
            except:
                char = ""
                dh = ""
        
        # Nothing is true
        else:
            char = ""
            dh = ""
        
        return char,dh
        
class gesture_prediction():
    def __init__(self):
        self.consonant_classifier = load_model("consonant_recognizer.h5")
        self.vowel_classifier = load_model("vowel_recognizer.h5")
        self.punctuation_classifier = load_model("punctuation_recognizer.h5")
        self.gesture_consonant = ["fist","thumb_out","index_out","thumb_index_out","nasal","relax"]
        self.gesture_vowel = ["a","e","u","ae","i","o","au","am","ak","relax"]
        self.gesture_punctuation = ["period","comma","space","nextline","question","exclamation","doublequotes","semicolon","delete","backspace","relax"]

    def get_gesture(self,image,face_loc,hand_1_loc,hand_2_loc,hand_1_flag,hand_2_flag,hand_loc,image_rows,image_cols):
        det_flag_cons = "Good" 
        det_flag_vow = "Good" 
        # Predict consonant hand gesture
        if (hand_1_flag == "Right" or hand_2_flag == "Right") and len(hand_loc)>20:
            if hand_1_flag == "Right" and hand_1_loc[0]>face_loc[0]:
                hand_loc_con = np.array(hand_loc[:21])
            elif hand_2_flag == "Right" and hand_2_loc[0]>face_loc[0]:
                hand_loc_con = np.array(hand_loc[21:])
            else:
                hand_loc_con = np.array(hand_loc[:21])
                det_flag_cons = "Glitch"                                     
            X_pro = hand_loc_con[:,:]-hand_loc_con[0,:]
            X_row = X_pro[:,0]/image_rows
            X_col = X_pro[:,1]/image_cols
            X_con = np.concatenate([X_row,X_col])
            X_con = np.reshape(X_con,(1,42))
            Y = np.argmax(np.array(self.consonant_classifier(X_con)))
            # Y = 0
            consonant = self.gesture_consonant[Y]
            if det_flag_cons == "Glitch":
                consonant = "relax"
        else:
            consonant = "relax"
        
        # Predict vowel hand gesture
        if (hand_1_flag == "Left" or hand_2_flag == "Left") and len(hand_loc)>20:
            if hand_1_flag == "Left" and hand_1_loc[0]<face_loc[0]:
                hand_loc_vow = np.array(hand_loc[:21])
            elif hand_2_flag == "Left" and hand_2_loc[0]<face_loc[0]:
                hand_loc_vow = np.array(hand_loc[21:])
            else:
                hand_loc_vow = np.array(hand_loc[:21])
                det_flag_vow = "Glitch"    
            X_pro = hand_loc_vow[:,:]-hand_loc_vow[0,:]
            X_row = X_pro[:,0]/image_rows
            X_col = X_pro[:,1]/image_cols
            X_vow = np.concatenate([X_row,X_col])
            X_vow = np.reshape(X_vow,(1,42))
            Y_vow = np.argmax(np.array(self.vowel_classifier(X_vow)))
            Y_pun = np.argmax(np.array(self.punctuation_classifier(X_vow)))
            # Y_vow = 0
            # Y_pun = 0
            vowel = self.gesture_vowel[Y_vow]
            punctuation = self.gesture_punctuation[Y_pun]
            if det_flag_vow == "Glitch":
                vowel = "relax"
                punctuation = "relax"
        else:
            vowel = "relax"
            punctuation = "relax"
        
        return consonant,vowel,punctuation
    
class state_prediction():
    def __init__(self):
        self.char_time = time.time()
        self.time_thr_normal = 1
        self.time_thr_dh = 2
        self.append_flag = False
        self.replace_flag = False
        self.char_last_append = ""
        self.st = "R"
        
    def get_state(self,ch,ch_t_1):
        # Check if relax state
        if ch=="" or ch!=ch_t_1:
           self.st = "R"
           self.char_time = time.time()
        
        elif ch==ch_t_1:
            # Check if normal state
            if time.time()-self.char_time < self.time_thr_normal:
                self.st = "N"
            # Check if dheerga state
            elif (time.time()-self.char_time > self.time_thr_normal and time.time()-self.char_time < self.time_thr_dh):
                if self.st!="D":
                    self.append_flag = True
                self.st = "D"
            # Check if replace
            elif time.time()-self.char_time > self.time_thr_dh:
                self.st = "RP"
                self.replace_flag = True
                self.char_time = time.time()
                
        return self.st
    
    def get_word(self,w,st,ch,dh):
        # if append_flag is True
        if self.append_flag:
            self.append_flag = False
            self.char_last_append = ch
            if ch == "word_edit":
                if dh=="nextline":
                    w = w+'\n'+'_'
                elif dh=="backspace":
                    w = w[:-1]
                elif dh=="delete":
                    w = ""
            else:
                w = w+ch
            
        # if dheerga is to be appended
        elif self.replace_flag:
            if ch == "word_edit":
                self.replace_flag = False
            else:
                w = w[:-(len(self.char_last_append))]+dh
                self.replace_flag = False
            
        return w
            
        
            
            
            
            