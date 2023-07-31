# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:25:37 2023

@author: admin
"""
from pydantic import BaseModel
#2. Class which describes Bank Notes measurents
class WaterAnalysis(BaseModel):
    ph	: float
    Hardness : float	
    Solids	: float
    Chloramines	:float
    Sulfate : float	
    Conductivity: float	
    Organic_carbon: float
    Trihalomethanes	 : float
    Turbidity	: float