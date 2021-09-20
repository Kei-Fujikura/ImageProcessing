from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import cv2
import pathlib
import os

class Position(BaseModel):
    """ This class can controls"""
    x : int = 10 
    y : int = 10

class PositionList(BaseModel):
    """ this class handle multiple "Position" by arrayList format. """
    name: Optional[str] = ""
    description: Optional[str] = ""
    ROIlist : List[Position]

class Rectangle(BaseModel):
    """ This class can controls"""
    x : int = 10 
    y : int = 10
    w : int = 20
    h : int = 20

class ROIList(BaseModel):
    """ this class handle multiple "Rectangle" by arrayList format. """
    name: Optional[str] = ""
    description: Optional[str] = ""
    ROIlist : List[Rectangle]

class ImagePath(BaseModel):
    name : Optional[str] = "helpme"
    path : str = "c:\\test_image\\sample_image.png"

