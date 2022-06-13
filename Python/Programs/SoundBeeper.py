import winsound as ws
import time as t

i = 0
bw = 0

while True:
    if bw == 0:
        print((" " * i) + "o")
    else:
        print((" " * (40 - i)) + "o")
    i += 1
    if i == 40:
        if bw == 0:
            bw = 1
        else:
            bw = 0
        i = 0
    t.sleep(0.001)