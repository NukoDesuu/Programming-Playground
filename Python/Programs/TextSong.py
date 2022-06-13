import LyricsMapper as lp
import time as t

SongFolder = "E:\\Nono\\Programming\\ONLINE SYNCED SOURCES\\Programming-Playground\\Python\\Song lyrics\\"
SongName = input("Please input song file name : ")
multi = (input("Speed (if not given, the song starts with 1.00x speed) : "))
if multi == '':
    multi = 1.00
else:
    multi = float(multi)

lyricf = SongFolder + SongName + 'Lyrics.txt'
beatf = SongFolder + SongName + 'Beats.txt'
atrf = SongFolder + SongName + 'Atr.txt'

with open(lyricf, 'r') as lf:
    syllables = [s for s in lf]
    syllables = "".join(syllables)
    syllables = syllables.replace(",", "").replace("\n", "")

with open(beatf, 'r') as bf:
    beats = [b for b in bf]
    beats = "".join(beats)
    beats = beats.replace(" ", "").replace("\n", "")

with open(atrf, 'r') as af:
    attributes = [a for a in af]
    Name = attributes[0]
    bpm = float(attributes[1])

syllables = syllables.split('/')
beats = beats.split(',')

bpm_v = bpm * multi

Title = "\nSong name : " + Name + "BPM : " + str(bpm_v) + "\n"
print(Title)
lp.Player.Play(bpm_v, syllables, beats)
print("\n-- Song done! --")