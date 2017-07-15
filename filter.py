#!/usr/bin/python

import numpy as np
from scipy.signal import savgol_filter
import multiprocessing

def load_data(filename):
  time = list()
  Ubatt = list()
  discharge = list()
  with open(filename, "r") as rfile:
    for line in rfile:
      fields = line.split(',');  
      time.append(float(fields[0]))
      Ubatt.append(float(fields[1]))
      if fields[2].strip() == "None":
        discharge.append(None)
      else:
        discharge.append(float(fields[2]))
  return np.array(time), np.array(Ubatt), np.array(discharge)


def save_data(filename, time, Ubatt, discharge):
  with open(filename, "w") as wfile:
    for x,y,z in np.c_[time,Ubatt,discharge]:
      wfile.write("{},{},{}\n".format(x,y,z))  
 
 
def filter(args):
 filename, window_length = args
 print("process {}".format(filename))
 t, U, d = load_data("{}.csv".format(filename))
 U = savgol_filter(U, window_length, 1)
 save_data("{}-savgol{}.csv".format(filename, window_length), t, U, d)


if __name__ == "__main__":
  files = [
    ["49.6ohm_cont_lipo", 21],
    ["24.8ohm_10min_50min_lipo", 21],
    ["24.8ohm_1s_1s_lipo", 7],
    ["24.8ohm_40min_80min_lipo", 21],
    ["24.8ohm_500ms_500ms_lipo", 7],
    ["24.8ohm_50s_50s_lipo", 7],
    ["24.8ohm_cont_lipo", 21],
    ["6.2ohm_1s_1s_lipo", 7],
    ["6.2ohm_1s_7s_lipo", 7],
    ["6.2ohm_50s_50s_lipo", 7],
    ["6.2ohm_cont_lipo", 21],
    ["49.6ohm_cont_alkaline", 21],
    ["24.8ohm_1s_1s_alkaline", 7],
    ["24.8ohm_60min_90min_alkaline", 7],
    ["6.2ohm_1s_7s_alkaline", 7]
  ]
  pool = multiprocessing.Pool()
  pool.map(filter, files)
