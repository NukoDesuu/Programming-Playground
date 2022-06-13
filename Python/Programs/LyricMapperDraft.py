import LyricsMapper as lp

def multiOf(max_val, mul):
    multiples = []
    for n in range(max_val):
        if n % mul == 0:
            multiples.append(n)
    return multiples

multiples4 = multiOf

bpm = int(input("BPM : "))
bdv = int(input("Beat measures : "))
song_length = int(input("Number of beats : "))
test_inputs = list()

multiples4 = multiOf(song_length + 1, bdv)

for k in range(1,song_length + 1):
    bd = k // bdv
    if k in multiples4:
        i = str(bdv)
    else:
        i = str(k - (bdv*bd))
    test_inputs.append(i)

sylla = test_inputs
waits = ['b']*song_length

lp.Player.Play(bpm, sylla, waits)