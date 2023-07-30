import pandas as pd
T_hour_ori = pd.read_excel('C:\\Users\\11535\\Desktop\\MScproject\\OneDrive_2023-06-19\\YDelta.xlsx', usecols=[4], names=None)
T_cycle1_ori = pd.read_excel('C:\\Users\\11535\\Desktop\\MScproject\\OneDrive_2023-06-19\\YDelta.xlsx', usecols=[5], names=None)

T_hour = T_hour_ori.dropna()
T_cycle = T_cycle1_ori.dropna()
T_hour = T_hour.reset_index(drop=True)
T_cycle = T_cycle.reset_index(drop=True)

# normalization
T_hour = (T_hour) / (T_hour.max())
T_cycle = (T_cycle) / (T_cycle.max())





