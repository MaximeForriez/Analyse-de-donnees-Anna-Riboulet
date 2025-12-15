#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv 

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023

with open("data/resultats-elections-presidentielles-2022-1er-tour.csv", newline='') as csvfile:
    resultats = pd.read_csv(csvfile, delimiter=",")
    print(resultats["Abstentions","Votants"])  
        
 # Abstentions Inscrits Votants Blancs Nuls Exprimés Voix