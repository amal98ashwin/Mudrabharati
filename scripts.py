# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:43:20 2021

@author: Ashwin
"""
def get_characters(flag):
    if flag == "tamil":
        cons = {
        # Consonants
        '1_fist':u'\u0b95\u0bcd','1_thumb_out':u'\u0b95\u0bcd','1_index_out':u'\u0b95\u0bcd','1_thumb_index_out':u'\u0b95\u0bcd','1_nasal':u'\u0b99\u0bcd',
        '2_fist':u'\u0b9a\u0bcd','2_thumb_out':u'\u0b9a\u0bcd','2_index_out':u'\u0b9c\u0bcd','2_thumb_index_out':u'\u0b9c\u0bcd','2_nasal':u'\u0b9e\u0bcd',
        '3_fist':u'\u0b9f\u0bcd','3_thumb_out':u'\u0b9f\u0bcd','3_index_out':u'\u0b9f\u0bcd','3_thumb_index_out':u'\u0b9f\u0bcd','3_nasal':u'\u0ba3\u0bcd',
        '4_fist':u'\u0ba4\u0bcd','4_thumb_out':u'\u0ba4\u0bcd','4_index_out':u'\u0ba4\u0bcd','4_thumb_index_out':u'\u0ba4\u0bcd','4_nasal':u'\u0ba9\u0bcd',
        '5_fist':u'\u0baa\u0bcd','5_thumb_out':u'\u0baa\u0bcd','5_index_out':u'\u0baa\u0bcd','5_thumb_index_out':u'\u0baa\u0bcd','5_nasal':u'\u0bae\u0bcd',
        '6_fist':u'\u0baf\u0bcd','6_thumb_out':u'\u0bb5\u0bcd','6_index_out':u'\u0bb9\u0bcd','6_nasal':u'\u0ba8\u0bcd',
        '7_fist':u'\u0bb0\u0bcd','7_thumb_out':u'\u0bb1\u0bcd',
        '8_fist':u'\u0bb2\u0bcd','8_thumb_out':u'\u0bb3\u0bcd','8_index_out':u'\u0bb4\u0bcd',
        '9_fist':u'\u0b9a\u0bcd','9_thumb_out':u'\u0bb8\u0bcd','9_index_out':u'\u0bb7\u0bcd'}
        
        vowel = {
        # Vowels
        'a':u'\u0b85', 'e':u'\u0b87', 'u':u'\u0b89', 'ae':u'\u0b8e', 'i':u'\u0b90', 'o':u'\u0b92', 'au':u'\u0b94', 'ak':u'\u0b83'}
        
        vowel_dheerga = {
        # Vowel dheergas
        'a':u'\u0b86', 'e':u'\u0b88', 'u':u'\u0b8a', 'ae':u'\u0b8f', 'i':u'\u0b90', 'o':u'\u0b93', 'au':u'\u0b94', 'ak':u'\u0b83'}
    
        swar_cons = {
        # Consonant of CV
        '1_fist':u'\u0b95','1_thumb_out':u'\u0b95','1_index_out':u'\u0b95','1_thumb_index_out':u'\u0b95','1_nasal':u'\u0b99',
        '2_fist':u'\u0b9a','2_thumb_out':u'\u0b9a','2_index_out':u'\u0b9c','2_thumb_index_out':u'\u0b9c','2_nasal':u'\u0b9e',
        '3_fist':u'\u0b9f','3_thumb_out':u'\u0b9f','3_index_out':u'\u0b9f','3_thumb_index_out':u'\u0b9f','3_nasal':u'\u0ba3',
        '4_fist':u'\u0ba4','4_thumb_out':u'\u0ba4','4_index_out':u'\u0ba4','4_thumb_index_out':u'\u0ba4','4_nasal':u'\u0ba9',
        '5_fist':u'\u0baa','5_thumb_out':u'\u0baa','5_index_out':u'\u0baa','5_thumb_index_out':u'\u0baa','5_nasal':u'\u0bae',
        '6_fist':u'\u0baf','6_thumb_out':u'\u0bb5','6_index_out':u'\u0bb9','6_nasal':u'\u0ba8',
        '7_fist':u'\u0bb0','7_thumb_out':u'\u0bb1',
        '8_fist':u'\u0bb2','8_thumb_out':u'\u0bb3','8_index_out':u'\u0bb4',
        '9_fist':u'\u0b9a','9_thumb_out':u'\u0bb8','9_index_out':u'\u0bb7'}
        
        swar_vow = {
        # Vowel of CV
        'a':'', 'e':u'\u0bbf', 'u':u'\u0bc1', 'ae':u'\u0bc6', 'i':u'\u0bc8', 'o':u'\u0bca', 'au':u'\u0bcc', 'ak':''}
        
        swar_dh = {
        # Dheerga of CV
        'a':u'\u0bbe', 'e':u'\u0bc0', 'u':u'\u0bc2', 'ae':u'\u0bc7', 'i':u'\u0bc8', 'o':u'\u0bcb', 'au':u'\u0bcc', 'ak':''}
            
    elif flag == "hindi":
        cons = {
        # Consonants
        '1_fist':u'\u0915','1_thumb_out':u'\u0916','1_index_out':u'\u0917','1_thumb_index_out':u'\u0918','1_nasal':u'\u0919',
        '2_fist':u'\u091a','2_thumb_out':u'\u091b','2_index_out':u'\u091c','2_thumb_index_out':u'\u091d','2_nasal':u'\u091e',
        '3_fist':u'\u091f','3_thumb_out':u'\u0920','3_index_out':u'\u0921','3_thumb_index_out':u'\u0922','3_nasal':u'\u0923',
        '4_fist':u'\u0924','4_thumb_out':u'\u0925','4_index_out':u'\u0926','4_thumb_index_out':u'\u0927','4_nasal':u'\u0928',
        '5_fist':u'\u092a','5_thumb_out':u'\u092b','5_index_out':u'\u092c','5_thumb_index_out':u'\u092d','5_nasal':u'\u092e',
        '6_fist':u'\u092f','6_thumb_out':u'\u0935','6_index_out':u'\u0939','6_nasal':u'\u0928',
        '7_fist':u'\u0930','7_thumb_out':u'\u0930',
        '8_fist':u'\u0932','8_thumb_out':u'\u0933','8_index_out':u'\u0934',
        '9_fist':u'\u0936','9_thumb_out':u'\u0937','9_index_out':u'\u0938'}
        
        vowel = {
        # Vowels
        'a':u'\u0905', 'e':u'\u0907', 'u':u'\u0909', 'ae':u'\u090f', 'i':u'\u0910', 'o':u'\u0913', 'au':u'\u0914', 'am':u'\u0905\u0902', 'ah':u'\u0905\u0903'}
        
        vowel_dheerga = {
        # Vowel dheergas
        'a':u'\u0906', 'e':u'\u0908', 'u':u'\u090a', 'ae':u'\u090f', 'i':u'\u0910', 'o':u'\u0913', 'au':u'\u0914', 'am':u'\u0905\u0902', 'ah':u'\u0905\u0903'}
    
        swar_cons = {
        # Consonant of CV
        '1_fist':u'\u0915','1_thumb_out':u'\u0916','1_index_out':u'\u0917','1_thumb_index_out':u'\u0918','1_nasal':u'\u0919',
        '2_fist':u'\u091a','2_thumb_out':u'\u091b','2_index_out':u'\u091c','2_thumb_index_out':u'\u091d','2_nasal':u'\u091e',
        '3_fist':u'\u091f','3_thumb_out':u'\u0920','3_index_out':u'\u0921','3_thumb_index_out':u'\u0922','3_nasal':u'\u0923',
        '4_fist':u'\u0924','4_thumb_out':u'\u0925','4_index_out':u'\u0926','4_thumb_index_out':u'\u0927','4_nasal':u'\u0928',
        '5_fist':u'\u092a','5_thumb_out':u'\u092b','5_index_out':u'\u092c','5_thumb_index_out':u'\u092d','5_nasal':u'\u092e',
        '6_fist':u'\u092f','6_thumb_out':u'\u0935','6_index_out':u'\u0939','6_nasal':u'\u0928',
        '7_fist':u'\u0930','7_thumb_out':u'\u0930',
        '8_fist':u'\u0932','8_thumb_out':u'\u0933','8_index_out':u'\u0934',
        '9_fist':u'\u0936','9_thumb_out':u'\u0937','9_index_out':u'\u0938'}
        
        swar_vow = {
        # Vowel of CV
        'a':'', 'e':u'\u093f', 'u':u'\u0941', 'ae':u'\u0946', 'i':u'\u0948', 'o':u'\u094a', 'au':u'\u094c', 'am':u'\u0902', 'ah':u'\u0903'}
        
        swar_dh = {
        # Dheerga of CV
        'a':u'\u093e', 'e':u'\u0940', 'u':u'\u0942', 'ae':u'\u0947', 'i':u'\u0948', 'o':u'\u094b', 'au':u'\u094c', 'am':u'\u0902', 'ah':u'\u0903'}

    elif flag == "telugu":
        cons = {
        # Consonants
        '1_fist':u'\u0c15\u0c4d','1_thumb_out':u'\u0c16\u0c4d','1_index_out':u'\u0c17\u0c4d','1_thumb_index_out':u'\u0c18\u0c4d','1_nasal':u'\u0c19\u0c4d',
        '2_fist':u'\u0c1a\u0c4d','2_thumb_out':u'\u0c1b\u0c4d','2_index_out':u'\u0c1c\u0c4d','2_thumb_index_out':u'\u0c1d\u0c4d','2_nasal':u'\u0c1e\u0c4d',
        '3_fist':u'\u0c1f\u0c4d','3_thumb_out':u'\u0c20\u0c4d','3_index_out':u'\u0c21\u0c4d','3_thumb_index_out':u'\u0c22\u0c4d','3_nasal':u'\u0c23\u0c4d',
        '4_fist':u'\u0c24\u0c4d','4_thumb_out':u'\u0c25\u0c4d','4_index_out':u'\u0c26\u0c4d','4_thumb_index_out':u'\u0c27\u0c4d','4_nasal':u'\u0c28\u0c4d',
        '5_fist':u'\u0c2a\u0c4d','5_thumb_out':u'\u0c2b\u0c4d','5_index_out':u'\u0c2c\u0c4d','5_thumb_index_out':u'\u0c2d\u0c4d','5_nasal':u'\u0c2e\u0c4d',
        '6_fist':u'\u0c2f\u0c4d','6_thumb_out':u'\u0c35\u0c4d','6_index_out':u'\u0c39\u0c4d','6_nasal':u'\u0c28\u0c4d',
        '7_fist':u'\u0c30\u0c4d','7_thumb_out':u'\u0c31\u0c4d',
        '8_fist':u'\u0c32\u0c4d','8_thumb_out':u'\u0c33\u0c4d','8_index_out':u'\u0c34\u0c4d',
        '9_fist':u'\u0c36\u0c4d','9_thumb_out':u'\u0c37\u0c4d','9_index_out':u'\u0c38\u0c4d'}
        
        vowel = {
        # Vowels
        'a':u'\u0c05', 'e':u'\u0c07', 'u':u'\u0c09', 'ae':u'\u0c0e', 'i':u'\u0c10', 'o':u'\u0c12', 'au':u'\u0c14', 'am':u'\u0c05\u0c02', 'ah':u'\u0c05\u0c03'}
        
        vowel_dheerga = {
        # Vowel dheergas
        'a':u'\u0c06', 'e':u'\u0c08', 'u':u'\u0c0a', 'ae':u'\u0c0f', 'i':u'\u0c10', 'o':u'\u0c13', 'au':u'\u0c14', 'am':u'\u0c05\u0c02', 'ah':u'\u0c05\u0c03'}
    
        swar_cons = {
        # Consonant of CV
        '1_fist':u'\u0c15','1_thumb_out':u'\u0c16','1_index_out':u'\u0c17','1_thumb_index_out':u'\u0c18','1_nasal':u'\u0c19',
        '2_fist':u'\u0c1a','2_thumb_out':u'\u0c1b','2_index_out':u'\u0c1c','2_thumb_index_out':u'\u0c1d','2_nasal':u'\u0c1e',
        '3_fist':u'\u0c1f','3_thumb_out':u'\u0c20','3_index_out':u'\u0c21','3_thumb_index_out':u'\u0c22','3_nasal':u'\u0c23',
        '4_fist':u'\u0c24','4_thumb_out':u'\u0c25','4_index_out':u'\u0c26','4_thumb_index_out':u'\u0c27','4_nasal':u'\u0c28',
        '5_fist':u'\u0c2a','5_thumb_out':u'\u0c2b','5_index_out':u'\u0c2c','5_thumb_index_out':u'\u0c2d','5_nasal':u'\u0c2e',
        '6_fist':u'\u0c2f','6_thumb_out':u'\u0c35','6_index_out':u'\u0c39','6_nasal':u'\u0c28',
        '7_fist':u'\u0c30','7_thumb_out':u'\u0c31',
        '8_fist':u'\u0c32','8_thumb_out':u'\u0c33','8_index_out':u'\u0c34',
        '9_fist':u'\u0c36','9_thumb_out':u'\u0c37','9_index_out':u'\u0c38'}
        
        swar_vow = {
        # Vowel of CV
        'a':'', 'e':u'\u0c3f', 'u':u'\u0c41', 'ae':u'\u0c46', 'i':u'\u0c48', 'o':u'\u0c4a', 'au':u'\u0c4c', 'am':u'\u0c02', 'ah':u'\u0c03'}
        
        swar_dh = {
        # Dheerga of CV
        'a':u'\u0c3e', 'e':u'\u0c40', 'u':u'\u0c42', 'ae':u'\u0c47', 'i':u'\u0c48', 'o':u'\u0c4b', 'au':u'\u0c4c', 'am':u'\u0c02', 'ah':u'\u0c03'}
  
    punc = {
    # Punctuations
    'period':'.', 'comma':',', 'space':'_', 'question':'?', 'exclamation':'!', 'doublequotes':'"', 'semicolon':';'}

    return cons,vowel,vowel_dheerga,swar_cons,swar_vow,swar_dh,punc