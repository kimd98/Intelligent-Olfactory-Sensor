import os
import sys
import time
import board
import busio
import adafruit_sgp40
import numpy as np

# reading # of sample for each dataset
sample = 60
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
type = input("Choose type (freshair/citrus/peppermint/fish): ")
if type == 'freshair':
    condition = input("Choose condition (FA_room/FA_outside/FA_outtoin/FA_intoout): ")

stat(sample)
saved = np.asarray(data_arr)
filepath = 'data/' + type + '/' + condition
i = 0
while os.path.exists(filepath + "%s.csv" % i):
    i = i + 1

filename = type + str(i) + '.csv'
np.savetxt(os.path.join(filepath, filename), saved, delimiter=',')
print("Data file created !")
