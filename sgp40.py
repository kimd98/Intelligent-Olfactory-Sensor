import os
import sys
import time
import board
import busio
import adafruit_sgp40
import numpy as np

# reading # of sample for each dataset
sample = 300
i2c = busio.I2C(board.SCL, board.SDA)
sgp = adafruit_sgp40.SGP40(i2c)
data_arr = np.empty(shape=(sample,16), dtype=np.int8)

def decimalToBinary(n):
    return bin(n).replace("0b", "")

# shows a 16-bit raw signal real-time data
def data():
    while True:
        print("Raw Gas: ", decimalToBinary(sgp.raw))
        print("")
        time.sleep(1)

# automatically save a dataset into the directory
def stat(dataNum):
    global data_arr
    print("Samples being collected... Please wait")
    for x in range(dataNum):
        raw = sgp.raw
        raw = format(raw, '016b')
        print(raw)
        for bit in range(16):
            data_arr[x, bit] = int(raw[bit])
        time.sleep(0.1)

# pick a proper datapath
type = input("Choose type (freshair/citrus/peppermint/fish/banana/garlic): ")
filepath = os.path.join('data', type)
condition = ' '

if type == 'banana':
    condition = input("Choose condition (BA_container/BA_air): ")
if type == 'garlic':
    condition = input("Choose condition (garlic_container/garlic_air): ")
if type == 'freshair':
    condition = input("Choose condition (FA_room/FA_outside/FA_outtoin/FA_intoout): ")
if type == 'fish':
    condition = input("Choose condition (fish_container/fish_withair): ")
if type == 'citrus' :
    condition = input("Choose condition (citrus_perfume/citrus_mandarine): ")
if type == 'peppermint':
    condition = input("Choose condition (PM_container/PM_air): ")

filepath = os.path.join(filepath, condition)

# csv file name represents the data type
filepath = os.path.join(filepath, type)
stat(sample)
saved = np.asarray(data_arr)
i = 0
while os.path.exists(filepath + "%s.csv" % i):
    i = i + 1

filename = filepath + str(i) + '.csv'
np.savetxt(filename, saved, delimiter=',')
print("Data file created ! Please check",  filename)
