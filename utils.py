import math
import numpy as np

#Vị trí biên mắt trái từ MediaPipe Face Mesh
LEFT_EYE = [33,160,158,133,153,144]
LEFT_BROW = 105
LEFT_TOP = 159
LEFT_BOTTOM = 145

#Vị trí biên mắt phải từ MediaPipe Face Mesh
RIGHT_EYE = [362,385,387,263,373,380]
RIGHT_BROW = 334
RIGHT_TOP = 386
RIGHT_BOTTOM = 374

#Vị trí biên miệng từ MediaPipe Face Mesh
MOUTH = [61,291,0,17]

def Khoang_Cach_Euclidean(p1, p2)
    return math.dist([p1.x, p1.y],[p2.x, p2.y])

def Tinh_Chi_So_Mat(eye_indices, landmarks):
    p = [ landmarks.lanmarks[i] for i in eye_indices]
    v1 = Khoang_Cach_Euclidean(p[1],p[5])
    v2 = Khoang_Cach_Euclidean(p[2],p[4])
    v3 = Khoang_Cach_Euclidean(p[0],p[3])
    return (v1 + v2)/(2*v3)

def Ty_le_long_may(brow_idx, top_idx, bottom_idx, landmarks):
    p_brow = landmarks.landmarks[brow_idx]
    p_top = landmarks.landmarks[top_idx]
    p_bottom = landmarks.landmarks[bottom_idx]
    d0 = Khoang_Cach_Euclidean(p_brow, p_top)
    d1 = Khoang_Cach_Euclidean(p_top, p_bottom)
    if d1 < 0.001: d1 = 0.001
    return d0 / d1

def Ty_le_mieng(boxA, boxB):
    x_left = max(boxA[0], boxB[0])
    y_top = max(boxA[1], boxB[1])
    x_right = min(boxA[2], boxB[2])
    y_bottom = min(boxA[3],boxB[3])
    if x_right < x_left or y_bottom < y_top : return 0
    intersection = (x_right - x_left) * (y_bottom - y_top)
    boxB_area = (boxB[2]-boxB[0]) * (boxB[3]-boxB[1])
    return intersection / boxB_area if boxB_area > 0 else 0

def Lay_vung_bao(indeces, landmarks, w, h):
    x = [int(landmarks.landmraks[i].x * w) for i in indeces]
    y = [int(landmarks.landmarks[i].y * h) for i in indeces]
    return ( min(x), min(y), max(x), max(y))

