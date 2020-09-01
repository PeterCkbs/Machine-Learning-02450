# -*- coding: utf-8 -*
"""
Created on Tue Sep  1 13:04:46 2020

@author: carst
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'C:/Users/carst/Desktop/DTU/5.semester/Machine_Learning/scripts/heart_failure_clinical_records_dataset.csv'


messy_data = pd.read_csv(filename, sep=',', header=0)

print(messy_data)

ghjhg