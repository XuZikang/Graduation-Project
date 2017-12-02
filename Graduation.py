# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:48:35 2017

@author: KangKang
"""

import wfdb
import numpy as np

root='C:/Users/KangKang/Desktop/Graduation-Project/Dataset/'
root1='Subject1_AccTempEDA'
root2='Subject1_SpO2HR'
def ReadData(root1,root2):
    
    #Read Annotation
    ATE_ann = wfdb.rdann(root+root1, 'atr')
    ATE_ann_sample = ATE_ann.sample
    #ATE_ann_symbol = ATE_ann.symbol
    #ATE_ann_aux_note = ATE_ann.aux_note

    #Read ATE_Data
    ATE_dat = wfdb.rdsamp(root+root1)
    ATE_dat_sig = ATE_dat.p_signals
    #ATE_dat_fs = ATE_dat.fs
    #ATE_dat_units = ATE_dat.units
    #ATE_dat_signame = ATE_dat.signame
    #ATE_dat_comments = ATE_dat.comments

    #Read SH_Data
    SH_dat = wfdb.rdsamp(root+root2)
    SH_dat_sig = SH_dat.p_signals
    #SH_dat_fs = SH_dat.fs
    #SH_dat_units = SH_dat.units
    #SH_dat_signame = SH_dat.signame
    
    comments = SH_dat.comments
    age = int(comments[0].split(': ')[1])
    gender = int(comments[1].split(': ')[1] == 'M')
    height = int(comments[2].split(': ')[1])
    weight = int(comments[3].split(': ')[1])
    const_info = np.array([age,gender,height,weight])
    return (ATE_ann_sample, ATE_dat_sig, SH_dat_sig, const_info)

# Constant Value
Constant_Value = {
       'ATE_ann_aux_note': ['Relax', 'PhysicalStress', 'Relax','EmotionalStress', 
                'CognitiveStress', 'Relax', 'EmotionalStress', 'Relax'],
        'ATE_dat_fs': 8,  
         'SH_dat_fs': 1,       
        'ATE_dat_units': ['NU', 'NU', 'NU', 'degC', 'NU'],
         'SH_dat_units': ['%', 'bpm'],
        'ATE_dat_signame': ['ax', 'ay', 'az', 'temp', 'EDA'],
         'SH_dat_signame': ['SpO2', 'hr']
         }

# Variable Value
Origin_Data = ReadData(root1, root2)

#Plot Data
#wfdb.plotrec(ATE_dat, annotation = ATE_ann, figsize = (10,10))
#wfdb.plotrec(SH_dat, figsize = (10,10))
