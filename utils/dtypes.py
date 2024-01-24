#-*- coding:utf-8 -*-
from enum import IntEnum, Enum

class LabelEnum(IntEnum):
    BACKGROUND = 0
   # TUMORAREA = 2
   # BRAINAREA = 1
   # BS = 1
   # CBM = 2
   # CSF = 3
   # GM = 4
   # LV = 5
   # SGM = 6
   # WM = 7
    FLUID = 1
    CORTEX = 2
    REST = 3

class FilterMethods(Enum):
    CUBIC = "CUBIC"
    LANCZOS2 = "LANCZOS2"
    LANCZOS3 = "LANCZOS3"
    BOX = "BOX"
    LINEAR = "LINEAR"
