# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 16:31:21 2018

@author: qiyi1
"""
import cv2
import numpy as np

def clean_lines(cv_img):
    cv_img_copy=cv_img.copy()
    gray = cv2.cvtColor(cv_img_copy,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(3,3),0)
    height,width=gray.shape
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    minLineLength = 30
    maxLineGap = 15
    lines = cv2.HoughLinesP(edges,1,np.pi/180,45,minLineLength,maxLineGap)
    for line in lines:
        x1,y1,x2,y2=line[0]
        if np.abs(x2-x1)>minLineLength:
            cv2.line(cv_img_copy,(0,y1),(width,y2),(255,255,255),6) #BGR
        else:
            cv2.line(cv_img_copy,(x1,0),(x2,height),(255,255,255),6)
    return cv_img_copy        

def highlight_lines(cv_img):
    cv_img_copy=cv_img.copy()
    gray = cv2.cvtColor(cv_img_copy,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(3,3),0)
    height,width=gray.shape
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    minLineLength = 30
    maxLineGap = 15
    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,minLineLength,maxLineGap)
    for line in lines:
        x1,y1,x2,y2=line[0]
        if np.abs(x2-x1)>minLineLength:
            cv2.line(cv_img_copy,(0,y1),(width,y2),(0,255,0),6) #BGR
        else:
            cv2.line(cv_img_copy,(x1,0),(x2,height),(0,255,0),6)
    return cv_img_copy        

if __name__=='__main__':
    from glob import glob
    import imageio
    wk_dir='C:/Users/qiyi1/OneDrive/Local Files/Engagements/1 script library/Miscs/ComputerVision/line_cleaning/'
    file_dir=wk_dir+'nw_im_crop/'
    input_dir=wk_dir+'input2/'
    output_dir=wk_dir+'output2/'
    #file_name='070473355 - Approved Example EY_Redacted-1-aligned-Unnamed2.jpg'
    #file_name='070473355 - Approved Example EY_Redacted-1-aligned-Unnamed10.jpg'
    #cv_img= cv2.imread(file_dir+file_name)
    img_list=glob(input_dir+'*')
    demo_img_hl=[]
    demo_img_clean=[]
    for path in img_list:
        file_name=path.split('\\')[-1]
        cv_img=cv2.imread(path)
        #cv_img_hlight=highlight_lines(cv_img)
        cv_img_clean=clean_lines(cv_img)
        #vis_hl = np.concatenate((cv_img,cv_img_hlight), axis=0)
        vis_cl=np.concatenate((cv_img,cv_img_clean),axis=0)
        cv2.imwrite(output_dir+file_name,cv_img_clean)
        #demo_img_hl.append(vis_hl)
        demo_img_clean.append(vis_cl)
    #imageio.mimsave(output_dir+'demo_hlight.gif', demo_img_hl, 'GIF', duration=1)
    imageio.mimsave(output_dir+'demo_clean.gif', demo_img_clean, 'GIF', duration=1)



