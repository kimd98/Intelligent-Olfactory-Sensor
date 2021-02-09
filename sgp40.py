import os
import sys
import time
import board
import busio
import adafruit_sgp40
# from collections import Counter
import numpy as np

sample = 16
i2c = busio.I2C(board.SCL, board.SDA)
sgp = adafruit_sgp40.SGP40(i2c)
data_arr = np.empty(shape=(sample,16), dtype=np.int8)

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def data():
    while True:
        print("Raw Gas: ", decimalToBinary(sgp.raw))
        print("")
        time.sleep(1)

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

type = input("Choose type (freshair/citrus/peppermint/fish): ")
stat(sample)
saved = np.asarray(data_arr)
filepath = 'data'

i = 0
while os.path.exists(filepath + '/' + type + "%s.csv" % i):
    i = i + 1

filename = type + str(i) + '.csv'
np.savetxt(os.path.join(filepath, filename), saved, delimiter=',')
print("Data file created !")
