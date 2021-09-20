from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import cv2
import numpy as np
import pathlib
import os

if os.path.isdir(".\\result") is False:
    os.mkdir(".\\result")

app = FastAPI()

def isImageFile(file_path:str):
    if os.path.isfile(file_path):
        print("is file")
        return True
    return False

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/pin")
def check_pinbending():
    return {"pin":"bend"}

@app.get("/result_image/{num}")
def get_resut_image(num : str):
    flist = list(pathlib.Path(".").glob("result/*"))
    flist.sort(key=os.path.getmtime, reverse=True)
    print(flist)
    last_image = flist[0]
    
    for x in flist:
        print(x)
        last_image = x
    
    return { 
        "image" : last_image
    }

@app.get("/customFunction")
def CalcCustomFunction( list_function : list ):
    pass

@app.get("/object_detection/OneTemplateMatch")
def CheckTemplateMaching(target_image_path: str = "image.png", template_image_path: str = "template.png", output_image_path : str = "matched.bmp"):
    res = {
        "in_image_path" : target_image_path,
        "out_image_path" : output_image_path,
        "pos" : { "x" : -1, "y": -1 }, 
        "error_message" : ""
    }

    if not isImageFile(target_image_path):
        res.error_message = "target image is not File"
        return res

    if not isImageFile(template_image_path):
        res.error_message = "template image is not File"
        return res
    
    im_tgt = cv2.imread(target_image_path)
    im_tmp = cv2.imread(template_image_path)

    result = cv2.matchTemplate(im_tgt, im_tmp, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

    tl = maxLoc[0], maxLoc[1]
    br = maxLoc[0] + im_tmp.shape[1], maxLoc[1] + im_tmp.shape[0]

    im_cropped = im_tgt[ tl[1]:br[1], tl[0]:br[0], : ]
    cv2.imwrite(output_image_path,im_cropped)

    res["pos"] = {
        "x" : (br[1] - tl[1])/2.0,
        "y" : (br[0] - tl[0])/2.0
    }

    return res


@app.get("/Filter/AdaptiveThreshold")
def CaclAdaptiveThreshold(target_image_path: str = "sato.jpg", output_image_path : str = "threshold.bmp", adaptiveMethod : str = "gauss", thresholdType: int = 0, blocksize: int = 5, C : int = 20):
    res = {
        "in_image_path" : target_image_path,
        "out_image_path" : output_image_path,
        "error_message" : ""
    }

    if not isImageFile(target_image_path):
        res.error_message = "target image is not File"
        return res

    im_tgt = cv2.imread(target_image_path, cv2.IMREAD_GRAYSCALE)

    if adaptiveMethod == "mean":
        admethod = cv2.ADAPTIVE_THRESH_MEAN_C
    else:
        admethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    
    if thresholdType == 0:
        thtype = cv2.THRESH_BINARY
    else:
        thtype = cv2.THRESH_BINARY_INV

    im_out = cv2.adaptiveThreshold(im_tgt, 255, admethod,thtype, blocksize, C)
    cv2.imwrite(output_image_path, im_out)

    return res