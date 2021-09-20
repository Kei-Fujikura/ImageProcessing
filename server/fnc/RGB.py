from fastapi import FastAPI
from lib.Struct import *
import cv2
import numpy as np

def get_RGB_rectangle_area(image_path : ImagePath, roi : ROIList):
    function_result = 0
    result_values = []
    error_message = ""
    temp_message = ""
    im = cv2.imread(image_path.name)

    for cnt,l in enumerate(roi.ROIlist):
        try:
            x, y, w, h = l.x, l.y, l.w, l.h
            m = im[y:(y+h),x:(x+w)]
            b_mean = np.mean(m[:,:,0])
            g_mean = np.mean(m[:,:,1])
            r_mean = np.mean(m[:,:,2])
            result_values.append({
                "R" : r_mean,
                "G" : g_mean,
                "B" : b_mean,
            })
        finally:
            temp_message += " {%d}"%cnt
    
    if len(roi.ROIlist) < len(result_values):
        error_message = u"some points have error : " + temp_message
        function_result = -2

    return {
        "result" : function_result,
        "error_message" : error_message,
        "value" : result_values
    }
